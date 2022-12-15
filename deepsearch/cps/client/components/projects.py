from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, List, Optional

import deepsearch.cps.apis.user
from deepsearch.cps.apis.user.models.token_response import TokenResponse

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

    def create(self, name: str) -> Project:
        create_data = {"name": name}
        proj: deepsearch.cps.apis.user.Project = self.sw_api.create(data=create_data)
        return self._load(proj)

    def remove(self, proj_key: str) -> Project:
        token_resp: TokenResponse = self.sw_api.get_delete_confirmation_token(
            proj_key=proj_key
        )
        del_token: str = token_resp.token
        return self.sw_api.delete(proj_key=proj_key, confirmation_token=del_token)

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
