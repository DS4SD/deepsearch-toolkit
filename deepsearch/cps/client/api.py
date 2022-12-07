from __future__ import annotations

import requests

import deepsearch.cps.apis.user
from deepsearch.core.client import (
    DeepSearchBearerTokenAuth,
    DeepSearchConfig,
    DeepSearchKeyAuth,
)
from deepsearch.core.util.config_paths import config_file_path
from deepsearch.cps.apis import public as sw_client
from deepsearch.cps.client.components import (
    CpsApiDataCatalogs,
    CpsApiDataIndices,
    CpsApiElastic,
    CpsApiKnowledgeGraphs,
    CpsApiProjects,
    CpsApiQueries,
    CpsApiTasks,
)


class CpsApiClient:
    def __init__(self, config: DeepSearchConfig) -> None:
        self.config = config

        if isinstance(self.config.auth, DeepSearchKeyAuth):
            self.bearer_token_auth = DeepSearchBearerTokenAuth(
                bearer_token=self._authenticate_with_api_key(
                    self.config.host,
                    self.config.auth.username,
                    self.config.auth.api_key,
                )
            )
        else:  # config.auth is of type DeepSearchAuth, which is either DeepSearchKeyAuth or DeepSearchBearerTokenAuth
            self.bearer_token_auth = self.config.auth

        auth = f"Bearer {self.bearer_token_auth.bearer_token}"

        sw_config = sw_client.Configuration(
            host=f"{self.config.host}/api/cps/public/v1",
            api_key={"Authorization": auth},
        )
        sw_config.verify_ssl = self.config.verify_ssl

        # Disable client-side validation, because our APIs lie.
        sw_config.client_side_validation = False

        # print(sw_config, sw_config.client_side_validation)

        self.swagger_client = sw_client.ApiClient(sw_config)

        sw_user_conf = deepsearch.cps.apis.user.Configuration(
            host=f"{self.config.host}/api/cps/user/v1",
            api_key={"Authorization": auth},
        )
        sw_user_conf.verify_ssl = self.config.verify_ssl

        # Disable client-side validation, because our APIs lie.
        sw_user_conf.client_side_validation = False

        self.user_swagger_client = deepsearch.cps.apis.user.ApiClient(sw_user_conf)

        self.session = requests.Session()
        self.session.headers["Authorization"] = auth
        self.session.verify = self.config.verify_ssl

    @staticmethod
    def _authenticate_with_api_key(host: str, username: str, api_key: str) -> str:
        user_api_conf = deepsearch.cps.apis.user.Configuration()
        user_api_conf.host = f"{host}/api/cps/user/v1"
        user_api_conf.verify_ssl = False
        user_api_conf.api_key_prefix = {}
        user_api_conf.username = username
        user_api_conf.password = api_key

        api = deepsearch.cps.apis.user.UsersApi(
            api_client=deepsearch.cps.apis.user.ApiClient(configuration=user_api_conf)
        )

        try:
            access_token = api.get_access_token(options={"admin": False}).access_token
        except deepsearch.cps.apis.user.exceptions.ApiException as e:
            raise RuntimeError("The API Key or User is invalid.") from e

        return access_token


class CpsApi:
    projects: CpsApiProjects
    knowledge_graphs: CpsApiKnowledgeGraphs
    queries: CpsApiQueries
    tasks: CpsApiTasks
    data_catalogs: CpsApiDataCatalogs
    elastic: CpsApiElastic
    data_indices: CpsApiDataIndices

    def __init__(self, client: CpsApiClient) -> None:
        self.client = client
        self._create_members()

    def _create_members(self):
        self.projects = CpsApiProjects(self)
        self.knowledge_graphs = CpsApiKnowledgeGraphs(self)
        self.queries = CpsApiQueries(self)
        self.tasks = CpsApiTasks(self)
        self.data_catalogs = CpsApiDataCatalogs(self)
        self.elastic = CpsApiElastic(self)
        self.data_indices = CpsApiDataIndices(self)

    def refresh_token(self, admin: bool = False):
        """Refresh access token

        Args:
            admin (bool, optional): controls whether an admin token should be requested. Defaults to False.

        Raises:
            RuntimeError: raised in case API Key or User is invalid
        """
        auth_header_val = f"Bearer {self.client.bearer_token_auth.bearer_token}"
        user_api_conf = deepsearch.cps.apis.user.Configuration(
            host=f"{self.client.config.host}/api/cps/user/v1",
            api_key={"Authorization": auth_header_val},
        )
        user_api_conf.verify_ssl = self.client.config.verify_ssl
        user_api_conf.client_side_validation = False

        api = deepsearch.cps.apis.user.UsersApi(
            api_client=deepsearch.cps.apis.user.ApiClient(configuration=user_api_conf)
        )

        try:
            access_token = api.get_access_token(options={"admin": admin}).access_token
        except deepsearch.cps.apis.user.exceptions.ApiException as e:
            raise RuntimeError("The API Key or User is invalid.") from e

        bearer_token_auth = DeepSearchBearerTokenAuth(bearer_token=access_token)
        ds_config = DeepSearchConfig(
            host=self.client.config.host,
            auth=bearer_token_auth,
            verify_ssl=self.client.config.verify_ssl,
        )
        self.client = CpsApiClient(ds_config)
        self._create_members()  # propagate updated token

    @classmethod
    def default_from_env(cls) -> "CpsApi":
        """
        Connect to CPS's API using a configured environment file
        """

        config_file = config_file_path()
        if not config_file.exists():
            raise RuntimeError(
                f"Config file {config_file} does not exist. Please configure your default authentication with `$ deepsearch login`"
            )
        config = DeepSearchConfig.parse_file(config_file)

        client = CpsApiClient(config)

        return cls(client)
