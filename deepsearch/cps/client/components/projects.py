from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, List, Optional

import deepsearch.cps.apis.user

if TYPE_CHECKING:
    from deepsearch.cps.client import CpsApi


class CpsApiProjects:
    def __init__(self, api: CpsApi) -> None:
        self.api = api
        self.sw_api = deepsearch.cps.apis.user.ProjectsApi(
            self.api.client.user_swagger_client
        )

    def list(self) -> List[Project]:
        # TODO: change for using details method
        bags: list[deepsearch.cps.apis.user.Project] = self.sw_api.list_projects()
        return [self._load(b) for b in bags]

    def get(self, key: str) -> Optional[Project]:
        projects = self.list()
        return next((proj for proj in projects if proj.key == key), None)

    def _load(self, project: deepsearch.cps.apis.user.Project) -> Project:
        return Project(
            # api=self.api,
            key=project.proj_key,
            name=project.name,
        )


@dataclass
class Project:
    key: str
    name: str
