from __future__ import annotations

import asyncio
import inspect
import logging
import os
import time
from datetime import datetime
from typing import Coroutine, Dict, Union

import uvicorn
from anyio import CapacityLimiter
from anyio.lowlevel import RunVar
from fastapi import FastAPI, HTTPException, Request
from fastapi.concurrency import run_in_threadpool
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette import status

from deepsearch.model.base.base_annotator import BaseAnnotator
from deepsearch.model.server.request_schemas import AnnotateRequestModel

logger = logging.getLogger("cps-fastapi")


class DeepSearchAnnotatorApp:
    def __init__(self):
        self.annotators_list: Dict[str, BaseAnnotator] = {}
        # Start the fast API app
        self.app = FastAPI()
        self.annotate_controller = self.AnnotateController(self.annotators_list)
        _log = logging.getLogger(__name__)

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
                key: self.annotate_controller.get_annotator_info(key)
                for key in self.annotators_list
            }

        # Will Require an API key
        @self.app.get("/annotator/{annotator_name}")
        async def get_annotator_specs(annotator_name: str) -> dict:
            return self.annotate_controller.get_annotator_info(annotator_name)

        @self.app.post("/annotator/{annotator_name}/predict", response_model=None)
        async def annotator_process(
            annotator_name: str, request: AnnotateRequestModel
        ) -> Union[JSONResponse, Coroutine]:
            # TODO pydantic models for return
            request_body = request.dict()

            request_arrival_time = time.time()
            failure_headers = {
                "X-Request-Arrival-Time": str(request_arrival_time),
                "X-Request-Attempt-Number": request_body.get("metadata", {})
                .get("annotations", {})
                .get("deepsearch_res_ibm_com_x_attempt_number"),
                "X-Request-Transaction-Id": request_body.get("metadata", {})
                .get("annotations", {})
                .get("deepsearch_res_ibm_com_x_transaction_id"),
            }

            try:
                cur_time = request_arrival_time
                deadline = datetime.strptime(
                    request_body["metadata"]["annotations"][
                        "deepsearch_res_ibm_com_x_deadline"
                    ],
                    "%Y-%m-%dT%H:%M:%S.%f%z",
                )
                deadline_ts = float(deadline.timestamp())

                compute_min_deadline_ts = (
                    cur_time
                    + self.annotators_list[annotator_name].expected_compute_time
                )

                if compute_min_deadline_ts - deadline_ts > 0:
                    raise HTTPException(
                        status_code=400,
                        detail="Deadline can not be lower than annotator expected compute time",
                    )
                # raise HTTPException(status_code=408,
                #                     detail="Dummy Failure")
                result = await asyncio.wait_for(
                    run_in_process(annotate_process, annotator_name, request_body),
                    timeout=deadline_ts - cur_time,
                )

                try:
                    if isinstance(result, Coroutine):
                        raise KeyError("Unresolved corroutine")
                except KeyError as e:
                    # Handle the exception here
                    raise e

                result.headers["X-Processing-Pod-Id"] = os.getenv(
                    "MY_POD_NAME", "local"
                )
                result.headers["X-Request-Arrival-Time"] = str(request_arrival_time)
                result.headers["X-Request-Attempt-Number"] = (
                    request_body.get("metadata", {})
                    .get("annotations", {})
                    .get("deepsearch_res_ibm_com_x_attempt_number")
                )
                result.headers["X-Request-Transaction-Id"] = (
                    request_body.get("metadata", {})
                    .get("annotations", {})
                    .get("deepsearch_res_ibm_com_x_transaction_id")
                )

                return result
            except asyncio.TimeoutError:
                print("Timed tasked out")
                failure_headers["X-Processing-Pod-Id"] = os.getenv(
                    "MY_POD_NAME", "local"
                )
                failure_headers["X-Request-Reject-Time"] = str(time.time())
                raise HTTPException(status_code=429, headers=failure_headers)
            except HTTPException as e:
                failure_headers["X-Processing-Pod-Id"] = os.getenv(
                    "MY_POD_NAME", "local"
                )
                failure_headers["X-Request-Reject-Time"] = str(time.time())
                e.headers = failure_headers
                raise e

        async def run_in_process(
            fn, *args
        ) -> Coroutine[Union[JSONResponse, HTTPException]]:
            return await run_in_threadpool(fn, *args)

        def annotate_process(
            annotator_name: str, request: Request
        ) -> Union[JSONResponse, HTTPException]:
            start_time = time.time()
            try:
                # print(request.dict())
                result = self.annotate_controller.run_annotator(annotator_name, request)
            except HTTPException as exc:
                raise exc
            end_time = time.time()
            process_time = end_time - start_time
            headers = {
                "X-start-time": str(start_time),
                "X-end-time": str(end_time),
                "X-time-total": str(process_time),
            }
            if "id" in request.keys():
                headers["X-request-id"] = str(request["id"])
            return JSONResponse(content=result, headers=headers)

    def register_annotator(
        self, cls: BaseAnnotator, name: Union[str, None] = None
    ) -> None:
        annotator_name = name if name is not None else cls.name
        try:
            if inspect.isclass(cls):
                raise TypeError(annotator_name)
            self.annotators_list[annotator_name] = cls
        except TypeError as e:
            logger.error(
                f" Raised {e.__class__.__name__}, for {e} object of register_annotator must be an object instance"
            )
            exit(-1)

    def run(self, host: str = "127.0.0.1", port: int = 8000, **kwargs) -> None:
        uvicorn.run(self.app, host=host, port=port, **kwargs)

    class AnnotateController:
        def __init__(self, app_annotators):
            self.app_annotators: dict = app_annotators

        def get_annotator_info(self, annot: str) -> dict:
            if not (annot in self.app_annotators):
                raise HTTPException(
                    status_code=404, detail=f"Invalid annotator {annot}", headers={}
                )
            return self.app_annotators[annot].get_annotator_info()

        def run_annotator(self, annot: str, body) -> dict:
            if not (annot in self.app_annotators):
                raise HTTPException(
                    status_code=404, detail=f"Invalid annotator {annot}", headers={}
                )
            annotator_instance = self.app_annotators[annot]

            if "findEntities" in body["spec"]:
                find_entities_part = body["spec"]["findEntities"]

                items = self._validate_and_parse_input(
                    find_entities_part, annotator_instance
                )
                try:
                    entities = annotator_instance.annotate_batched_entities(
                        find_entities_part["objectType"],
                        items,
                        find_entities_part["entityNames"],
                    )
                except HTTPException as e:
                    raise e
                # Key annotation functionn, depends on object_type (text, table etc.)

                # print("Result returned from '_run_annotator': ")
                # pprint.pprint({'entities': entities})
                return {"entities": entities}

            if "findRelationships" in body["spec"]:
                find_relationships_part = body["spec"]["findRelationships"]

                items = self._validate_and_parse_input(
                    find_relationships_part, annotator_instance
                )
                try:
                    relationships = annotator_instance.annotate_batched_relationships(
                        find_relationships_part["objectType"],
                        items,
                        find_relationships_part["entities"],
                        find_relationships_part["relationshipNames"],
                    )
                except HTTPException as e:
                    raise e

                return {"relationships": relationships}

            if "findProperties" in body["spec"]:
                find_properties_part = body["spec"]["findProperties"]

                items = self._validate_and_parse_input(
                    find_properties_part, annotator_instance
                )

                try:
                    if isinstance(items, dict):
                        if find_properties_part.get("entities", None) is None:
                            find_properties_part["entities"] = [{}] * len(items)
                    else:
                        raise KeyError("items is not a dictionary")
                except (HTTPException, KeyError) as e:
                    # Handle the exception here
                    print(f"Encountered an exception: {e}")

                try:
                    properties = annotator_instance.annotate_batched_properties(
                        find_properties_part["objectType"],
                        items,
                        find_properties_part["entities"],
                        find_properties_part["propertyNames"],
                    )
                except HTTPException as e:
                    raise e

                return {"properties": properties}

            raise HTTPException(
                status_code=500, detail=f"Internal Server Error", headers={}
            )

        @staticmethod
        def _validate_and_parse_input(body_part, annot) -> Union[HTTPException, dict]:
            # Input: body_part is the part of the request body indexed by the main command, e.g., body['find_entities']
            #        ann_cls is one of the Annotator classes in this repository.
            # Output: "items", i.e., a list of texts, tables, or images, if the request passed validation
            # Connexion seems to fail to validate the polymorphic inputs, so we need to do it ourselves :(
            object_type = body_part.get("objectType", "text")

            expected = ("text", "image", "table")

            if object_type not in expected:
                raise HTTPException(
                    status_code=400,
                    detail=f"Invalid object type. Expected one of: {expected}",
                )

            if object_type not in annot.supports:
                raise HTTPException(
                    status_code=400,
                    detail=f"Unsupported object type for this annotator. Supports: {annot.supports}",
                )

            if object_type == "text":
                if not isinstance(body_part.get("texts"), list):
                    raise HTTPException(
                        status_code=400, detail="Invalid input: Missing 'texts'"
                    )
                return body_part["texts"]

            if object_type == "image":
                if not isinstance(body_part.get("images"), list):
                    raise HTTPException(
                        status_code=400, detail="Invalid input: Missing 'images'"
                    )

                return body_part["images"]

            if object_type == "table":
                if not isinstance(body_part.get("tables"), list):
                    raise HTTPException(
                        status_code=400, detail="Invalid input: Missing 'tables'"
                    )

                return body_part["tables"]

            raise HTTPException(
                status_code=500,
                detail=f"Internal Server Error",
            )
