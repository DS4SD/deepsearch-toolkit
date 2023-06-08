from __future__ import annotations

import asyncio
import inspect
import logging
import os
import time
from datetime import datetime
from typing import Coroutine, Dict, Optional, Union

import uvicorn
from anyio import CapacityLimiter
from anyio.lowlevel import RunVar
from fastapi import FastAPI, HTTPException, Request
from fastapi.concurrency import run_in_threadpool
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette import status

from deepsearch.model.controllers.base_controller import BaseController
from deepsearch.model.examples.simple_text_geography_annotator.simple_text_geography_annotator import (
    SimpleTextGeographyAnnotator,
)
from deepsearch.model.factories.base_model_factory import BaseModelFactory
from deepsearch.model.server.request_schemas import InferenceRequest

logger = logging.getLogger("cps-fastapi")


class ModelApp:
    def __init__(self):
        self.app = FastAPI()
        self._controllers: Dict[str, BaseController] = {}

        @self.app.on_event("startup")
        async def startup_event():
            # do some initialization here
            RunVar("_default_thread_limiter").set(CapacityLimiter(1))

        # Register some exception handlers
        @self.app.exception_handler(RequestValidationError)
        async def validation_exception_handler(
            request: Request, exc: RequestValidationError
        ):
            print(exc)

            content = {"status_code": 10422, "message": exc, "data": None}
            return JSONResponse(
                content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
            )

        # Register endpoints for the app
        @self.app.exception_handler(RequestValidationError)
        async def validation_exception_handler(
            request: Request, exc: RequestValidationError
        ):
            exc_str = f"{exc}".replace("\n", " ").replace("   ", " ")
            # or logger.error(f'{exc}')
            print(exc_str)
            content = {"status_code": 10422, "message": exc_str, "data": None}
            return JSONResponse(
                content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
            )

        @self.app.get("/health")
        async def health_check() -> dict:
            return {"message": "HealthCheck"}

        @self.app.get("/")
        async def get_definitions() -> dict:
            return {
                name: controller.get_info()
                for name, controller in self._controllers.items()
            }

        # Will Require an API key
        @self.app.get("/annotator/{model_name}")
        async def get_model_specs(model_name: str) -> dict:
            controller = self._get_controller(model_name=model_name)
            return controller.get_info()

        @self.app.post("/annotator/{model_name}/predict", response_model=None)
        async def predict(
            model_name: str,
            request: InferenceRequest,
        ) -> Union[JSONResponse, Coroutine]:
            request_arrival_time = time.time()
            try:
                cur_time = request_arrival_time
                deadline = datetime.strptime(
                    request.metadata.annotations.deepsearch_res_ibm_com_x_deadline,
                    "%Y-%m-%dT%H:%M:%S.%f%z",
                )
                deadline_ts = float(deadline.timestamp())

                controller = self._get_controller(model_name=model_name)
                compute_min_deadline_ts = (
                    cur_time + controller.get_model().expected_compute_time
                )

                if compute_min_deadline_ts - deadline_ts > 0:
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail="Deadline can not be lower than model expected compute time",
                    )

                result = await asyncio.wait_for(
                    run_in_process(inference_process, model_name, request),
                    timeout=deadline_ts - cur_time,
                )

                try:
                    if isinstance(result, Coroutine):
                        raise KeyError("Unresolved corroutine")
                except KeyError as e:  # FIXME remove?
                    # Handle the exception here
                    raise e

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

        async def run_in_process(
            fn, *args
        ) -> Coroutine[Union[JSONResponse, HTTPException]]:
            return await run_in_threadpool(fn, *args)

        def inference_process(
            model_name: str, request: InferenceRequest
        ) -> JSONResponse:
            request_dict = request.dict()
            start_time = time.time()
            controller = self._get_controller(model_name=model_name)
            if (model_kind := controller.get_model().kind) != request.kind:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Requested kind ('{request.kind}') not matching actual one ('{model_kind}')",
                )
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
            return JSONResponse(content=result, headers=headers)

    def register_model_factory(
        self, factory: BaseModelFactory, name: Optional[str] = None
    ):
        model = factory.create_model()
        key = name or model.name
        self._controllers[key] = factory.create_controller(model=model)

    def _get_controller(self, model_name: str) -> BaseController:
        controller = self._controllers.get(model_name)
        if controller is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Invalid model '{model_name}'",
                headers={},
            )
        return controller

    def run(self, host: str = "127.0.0.1", port: int = 8000, **kwargs) -> None:
        uvicorn.run(self.app, host=host, port=port, **kwargs)
