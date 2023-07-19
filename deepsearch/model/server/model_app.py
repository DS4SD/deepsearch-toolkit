import asyncio
import logging
import os
import time
from typing import Dict, Optional

import uvicorn
from anyio import CapacityLimiter
from anyio.lowlevel import RunVar
from fastapi import Depends, FastAPI, HTTPException, Request, Security, status
from fastapi.concurrency import run_in_threadpool
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.security import APIKeyHeader

from deepsearch.model.base.controller import BaseController
from deepsearch.model.base.model import BaseDSModel
from deepsearch.model.server.config import Settings
from deepsearch.model.server.controller_factory import ControllerFactory
from deepsearch.model.server.inference_types import AppModelInfoOutput, AppPredInput

logger = logging.getLogger("cps-fastapi")


class ModelApp:
    def __init__(self, settings: Settings):
        self._settings = settings

        self.app = FastAPI()
        self._controllers: Dict[str, BaseController] = {}
        self._contr_factory = ControllerFactory()

        @self.app.on_event("startup")
        async def startup_event():
            # do some initialization here
            RunVar("_default_thread_limiter").set(CapacityLimiter(1))

        @self.app.exception_handler(RequestValidationError)
        async def validation_exception_handler(
            request: Request, exc: RequestValidationError
        ):
            return JSONResponse(
                content=jsonable_encoder({"errors": exc.errors()}),
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            )

        @self.app.get("/health")
        async def health_check() -> dict:
            return {"message": "HealthCheck"}

        @self.app.get("/")
        async def get_definitions(
            api_key=Depends(self._auth),
        ) -> Dict[str, AppModelInfoOutput]:
            return {
                name: controller.get_info()
                for name, controller in self._controllers.items()
            }

        @self.app.get("/model/{model_name}")
        async def get_model_specs(
            model_name: str, api_key=Depends(self._auth)
        ) -> AppModelInfoOutput:
            controller = self._get_controller(model_name=model_name)
            return controller.get_info()

        @self.app.post("/model/{model_name}/predict", response_model=None)
        async def predict(
            model_name: str, request: AppPredInput, api_key=Depends(self._auth)
        ) -> JSONResponse:
            request_arrival_time = time.time()
            try:
                controller = self._get_controller(model_name=model_name)

                curr_time = request_arrival_time
                deadline = (
                    request.metadata.annotations.deepsearch_res_ibm_com_x_deadline
                )
                deadline_ts = float(deadline.timestamp())
                if deadline_ts < curr_time:
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail="Requested deadline lies in the past",
                    )

                expected_completion_ts = curr_time + controller.get_model_exec_time()
                if deadline_ts < expected_completion_ts:
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail="Expected completion time lies beyond requested deadline",
                    )

                result = await asyncio.wait_for(
                    _run_in_process(_inference_process, model_name, request),
                    timeout=deadline_ts - curr_time,
                )

                result.headers["X-Processing-Pod-Id"] = os.getenv(
                    "MY_POD_NAME", "local"
                )
                result.headers["X-Request-Arrival-Time"] = str(request_arrival_time)
                result.headers[
                    "X-Request-Attempt-Number"
                ] = request.metadata.annotations.deepsearch_res_ibm_com_x_attempt_number
                result.headers[
                    "X-Request-Transaction-Id"
                ] = request.metadata.annotations.deepsearch_res_ibm_com_x_transaction_id

                return result
            except (asyncio.TimeoutError, HTTPException) as e:
                headers = {
                    "X-Request-Arrival-Time": str(request_arrival_time),
                    "X-Request-Attempt-Number": request.metadata.annotations.deepsearch_res_ibm_com_x_attempt_number,
                    "X-Request-Transaction-Id": request.metadata.annotations.deepsearch_res_ibm_com_x_transaction_id,
                    "X-Processing-Pod-Id": os.getenv("MY_POD_NAME", "local"),
                    "X-Request-Reject-Time": str(time.time()),
                }
                if isinstance(e, asyncio.TimeoutError):
                    raise HTTPException(
                        status_code=status.HTTP_429_TOO_MANY_REQUESTS, headers=headers
                    )
                else:
                    raise HTTPException(
                        status_code=e.status_code, detail=e.detail, headers=headers
                    )

        async def _run_in_process(fn, *args) -> JSONResponse:
            return await run_in_threadpool(fn, *args)

        def _inference_process(model_name: str, request: AppPredInput) -> JSONResponse:
            request_dict = request.dict()
            start_time = time.time()
            controller = self._get_controller(model_name=model_name)

            self._validate_request_kind(request=request, controller=controller)

            result = controller.dispatch_predict(request.spec)

            end_time = time.time()
            process_time = end_time - start_time
            headers = {
                "X-start-time": str(start_time),
                "X-end-time": str(end_time),
                "X-time-total": str(process_time),
            }
            if "id" in request_dict.keys():
                headers["X-request-id"] = str(request_dict["id"])
            return JSONResponse(content=jsonable_encoder(result), headers=headers)

    def _auth(self, header_api_key: str = Security(APIKeyHeader(name="Authorization"))):
        request_api_key = (
            header_api_key.replace("Bearer ", "")
            .replace("bearer ", "")
            .replace("Bearer: ", "")
            .replace("bearer: ", "")
            .strip()
        )
        if request_api_key != self._settings.api_key.get_secret_value():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API key"
            )

    def _get_controller(self, model_name: str) -> BaseController:
        controller = self._controllers.get(model_name)
        if controller is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Invalid model '{model_name}'",
                headers={},
            )
        return controller

    def register_model(
        self,
        model: BaseDSModel,
        name: Optional[str] = None,
        controller: Optional[BaseController] = None,
    ) -> None:
        """Registers a model with the app.

        Args:
            model (BaseDSModel): the model to register.
            name (Optional[str], optional): an optional name under which to register the model; if not set, the model's default name is used.
            controller (Optional[BaseController], optional): an optional custom controller to use; if not set, the default controller for the kind is used.
        """
        contr = controller or self._contr_factory.create_controller(model=model)
        self._validate_controller_kind(controller=contr, model=model)
        key = name or contr.get_model_name()
        self._controllers[key] = contr

    def run(self, host: str = "127.0.0.1", port: int = 8000, **kwargs) -> None:
        uvicorn.run(self.app, host=host, port=port, **kwargs)

    def _validate_controller_kind(
        self, controller: BaseController, model: BaseDSModel
    ) -> None:
        if controller.get_kind() != model.get_config().kind:
            raise RuntimeError("Controller kind does not match model")

    def _validate_request_kind(
        self, request: AppPredInput, controller: BaseController
    ) -> None:
        if request.kind != controller.get_kind():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Request kind does not match controller",
            )
