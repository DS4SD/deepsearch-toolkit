from __future__ import annotations

import time
from typing import TYPE_CHECKING, Any

from deepsearch.cps.apis import public as sw_client
from deepsearch.cps.apis.public.models.celery_task_promise import CeleryTaskPromise

if TYPE_CHECKING:
    from deepsearch.cps.client import CpsApi


class CpsApiTasks:
    def __init__(self, api: CpsApi) -> None:
        self.api = api
        self.sw_api = sw_client.TasksApi(self.api.client.swagger_client)

    def wait_for(self, project: str, task_id: str) -> Any:
        """Waits for a task and returns its result, or raises an exception in case of failure."""
        while True:
            task: CeleryTaskPromise = self.sw_api.get_project_celery_task(
                project, task_id
            )

            if task.task_status == "SUCCESS":
                return task.result

            if task.task_status in ("FAILURE", "REVOKED"):
                raise RuntimeError(f"Task failed with status {task.task_status!r}")

            time.sleep(1)
