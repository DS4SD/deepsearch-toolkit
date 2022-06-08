import ipython_blocking
import ipywidgets as widgets
from IPython.display import display

import deepsearch.cps.apis.kg.query
import deepsearch.cps.apis.user
import deepsearch.cps.ipython
from deepsearch.cps.client.api import CpsApi


class KGSelector:
    def __init__(self, api: CpsApi):
        self.api = api

    def interactive(self):
        """
        Select the KG using the interacting widget components
        """

        self._init_interactive()

        display(self.box)

        ctx = ipython_blocking.CaptureExecution(replay=True)
        with ctx:
            while True:
                if self._button_clicked:
                    break
                ctx.step()  # handles all other messages that aren't 'execute_request' including widget value changes

        for kg in self._kgs:
            if kg.key == self.kg_selector.value:
                status = self.check_knowledge_graph_status(
                    self.proj_selector.value, kg.key
                )
                self.out.append_stdout(
                    f"Selected proj={self.proj_selector.value}, kg={kg.name}, status={status}\n"
                )
                if status != "READY":
                    self.out.append_stdout(
                        "\n⚠️ WARNING ⚠️\nThe KG selected is *not* flagged as READY. Some operations will not be possible. Please re-execute the current Notebook cell to select another KG."
                    )
                return kg

    def check_knowledge_graph_status(self, proj_key, bag_key):
        return "READY"
        # with cps.apis.public.ApiClient(self.cps_configuration) as api_client:
        #     api_instance = cps.apis.public.KnowledgeGraphsApi(api_client)

        #     try:
        #         result = api_instance.get_project_knowledge_graph_status(proj_key, bag_key)
        #         return result.status
        #     except CPSApiException as e:
        #         print("Exception when calling KnowledgeGraphsApi->get_project_knowledge_graph_status: %s\n" % e)
        #         return "ERROR"

    def _init_interactive(self):

        default_args = deepsearch.cps.ipython.get_notebook_args()

        selected_proj = default_args["proj_key"]
        selected_kg = default_args["bag_key"]

        self._projects = self.api.projects.list()
        if selected_proj is None and self._projects:
            selected_proj = self._projects[0].key

        self._kgs = (
            self.api.knowledge_graphs.list(selected_proj) if selected_proj else []
        )
        if selected_kg is None and self._kgs:
            selected_kg = self._kgs[0].key

        widget_projects = [(proj.name, proj.key) for proj in self._projects]
        widget_kgs = [(kg.name, kg.key) for kg in self._kgs]

        # Widgets
        self.proj_selector = widgets.Dropdown(
            options=widget_projects,
            value=selected_proj,
            description="Project:",
        )
        self.proj_selector.observe(self.on_proj_change, names="value")

        self.kg_selector = widgets.Dropdown(
            options=widget_kgs,
            value=selected_kg,
            description="KG:",
        )

        self.btn = widgets.Button(
            description="Select KG",
            disabled=False,
            button_style="primary",  # 'success', 'info', 'warning', 'danger' or ''
        )
        self._button_clicked = False
        self.btn.on_click(self.on_click)

        self.out = widgets.Output()

        self.box = widgets.VBox(
            [widgets.Box([self.proj_selector, self.kg_selector, self.btn]), self.out]
        )

    def on_proj_change(self, change):
        self._kgs = self.api.knowledge_graphs.list(change["new"])
        widget_kgs = [(kg.name, kg.key) for kg in self._kgs]
        self.kg_selector.options = widget_kgs

    def on_click(self, _change):
        self.out.clear_output()
        # self.out.append_stdout('Clicked at ' + str(datetime.datetime.now()))
        self.btn.on_click(self.on_click, remove=True)
        self.btn.disabled = True
        self.proj_selector.disabled = True
        self.kg_selector.disabled = True
        self._button_clicked = True
