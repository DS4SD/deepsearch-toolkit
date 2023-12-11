from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING, List, Optional, Union

from pydantic.v1 import BaseModel

import deepsearch.cps.apis.user
from deepsearch.cps.apis.user.models.token_response import TokenResponse

if TYPE_CHECKING:
    from deepsearch.cps.client import CpsApi


class RoleEnum(str, Enum):
    viewer = "viewer"
    editor = "editor"
    owner = "owner"


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

    def assign_user(
        self,
        project: Union[Project, str],
        username: str,
        role: RoleEnum = RoleEnum.viewer,
    ) -> None:
        """Assign a user to a project

        Args:
            project (Union[Project, str]): project (instance or key) to assign user to
            username (str): email of the grantee
            role (RoleEnum, optional): role to grant. Defaults to RoleEnum.viewer.
        """

        proj_key = project.key if isinstance(project, Project) else project
        assign_data = {
            "username": username,
            "role": role,
        }
        self.sw_api.add_user(proj_key=proj_key, data=assign_data)

    def remove(self, project: Union[Project, str]) -> None:
        """Remove a project

        Args:
            project (Union[Project, str]): project (instance or key) to remove
        """
        proj_key = project.key if isinstance(project, Project) else project
        token_resp: TokenResponse = self.sw_api.get_delete_confirmation_token(
            proj_key=proj_key
        )
        del_token: str = token_resp.token
        self.sw_api.delete(proj_key=proj_key, confirmation_token=del_token)

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


class QAGenAIResource(BaseModel):
    proj_key: str

    def to_resource(self):
        return {
            "type": "qa_genai",
            "proj_key": self.proj_key,
            "integration_id": "genai",
            "instance_id": "qa_api",
        }
