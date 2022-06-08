from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List, Optional

from deepsearch.cps.apis import public as sw_client
from deepsearch.cps.apis.public.models.bag_backend_aware import BagBackendAware
from deepsearch.cps.apis.public.models.bag_flavour_full_data import BagFlavourFullData
from deepsearch.cps.apis.public.models.project_flavours import ProjectFlavours
from deepsearch.cps.apis.public.models.project_task import ProjectTask
from deepsearch.cps.apis.public.models.resume_knowledge_graph_options import (
    ResumeKnowledgeGraphOptions,
)
from deepsearch.cps.apis.public.models.suspend_knowledge_graph_options import (
    SuspendKnowledgeGraphOptions,
)
from deepsearch.cps.client.components.api_object import ApiConnectedObject

if TYPE_CHECKING:
    from deepsearch.cps.client import CpsApi


class CpsApiKnowledgeGraphs:
    def __init__(self, api: CpsApi) -> None:
        self.api = api
        self.sw_api = sw_client.KnowledgeGraphsApi(self.api.client.swagger_client)
        self._system_sw_api = sw_client.SystemApi(self.api.client.swagger_client)

    def list(self, project: str) -> List[CpsApiKg]:
        bags: list[BagBackendAware] = self.sw_api.backend_list_project_kgs(project)
        return [self._load(b) for b in bags]

    def get(self, project: str, key: str) -> Optional[CpsApiKg]:
        kgs = self.list(project)
        return next((kg for kg in kgs if kg.key == key), None)

    def _load(self, bag: BagBackendAware) -> CpsApiKg:
        return CpsApiKg(
            api=self.api,
            project=bag.proj_key,
            key=bag.bag_key,
            name=bag.name,
        )

    def list_flavours(self, project: str) -> List[BagFlavourFullData]:
        """List Knowledge Graph flavours."""

        result: ProjectFlavours = self._system_sw_api.list_flavours_by_project(project)

        return result.flavours


KgTopology = Any
KgStatus = Any


@dataclass
class KgSnapshot:
    id: str


@dataclass
class CpsApiKg(ApiConnectedObject):
    project: str
    key: str

    name: str

    def get_topology(self):
        client = self.api.client

        response = client.session.get(
            f"{client.config.host}/api/cps/kg/v1/project/{self.project}/bags/{self.key}/description"
        )

        response.raise_for_status()

        return response.json()

    def resume_empty(self):
        body = ResumeKnowledgeGraphOptions(reset=True)
        task: ProjectTask = (
            self.api.knowledge_graphs.sw_api.resume_project_knowledge_graph(
                self.project, self.key, body
            )
        )

        return self.api.tasks.wait_for(self.project, task.task_id)

    def resume_from(self, snapshot: KgSnapshot):
        body = ResumeKnowledgeGraphOptions(snapshot_to_restore_id=snapshot.id)
        task: ProjectTask = (
            self.api.knowledge_graphs.sw_api.resume_project_knowledge_graph(
                self.project, self.key, body
            )
        )

        return self.api.tasks.wait_for(self.project, task.task_id)

    def suspend(self):
        body = SuspendKnowledgeGraphOptions(force=True)
        task: ProjectTask = (
            self.api.knowledge_graphs.sw_api.suspend_project_knowledge_graph(
                self.project, self.key, body
            )
        )

        return self.api.tasks.wait_for(self.project, task.task_id)

    def to_resource(self) -> Dict[str, Any]:
        return {"type": "bag", "proj_key": self.project, "bag_key": self.key}

    def save_snapshot_of_data_flow(
        self,
        flavours: Dict[str, str],
        load_after_assembled: bool = False,
        name: Optional[str] = None,
    ):
        """Re-create the snapshot for a KG, using the last-assembled data-flow as a base"""

        body = {
            "snapshot": {
                "backend_flavours": flavours,
                "load_into_kg_after_created": load_after_assembled,
            }
        }

        # Annoying: the API doesn't distinguish undefined from null
        if name is not None:
            body["snapshot"]["name"] = name

        task: ProjectTask = self.api.knowledge_graphs.sw_api.backend_create_project_kg_snapshot_from_data_flow_assembly(
            proj_key=self.project,
            bag_key=self.key,
            body=body,
        )

        return task
