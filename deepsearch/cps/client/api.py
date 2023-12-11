from __future__ import annotations

from typing import Optional

import requests
from pydantic.v1 import ValidationError

import deepsearch.cps.apis.user
from deepsearch.core.client import (
    DeepSearchBearerTokenAuth,
    DeepSearchConfig,
    DeepSearchKeyAuth,
)
from deepsearch.core.client.settings import ProfileSettings
from deepsearch.core.client.settings_manager import SettingsManager
from deepsearch.cps.apis import public as sw_client
from deepsearch.cps.client.components import (
    CpsApiDataCatalogs,
    CpsApiDataIndices,
    CpsApiElastic,
    CpsApiKnowledgeGraphs,
    CpsApiProjects,
    CpsApiQueries,
    CpsApiTasks,
    DSApiDocuments,
)
from deepsearch.cps.client.components.uploader import DSApiUploader


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
    documents: DSApiDocuments
    uploader: DSApiUploader

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
        self.documents = DSApiDocuments(self)
        self.uploader = DSApiUploader(self)

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
    def from_env(cls, profile_name: Optional[str] = None) -> CpsApi:
        """Create an API object resolving the required settings from the environment if possible, otherwise from a stored profile.

        Args:
            profile_name (Optional[str], optional): profile to use if resolution from environment not possible. Defaults to None (active profile).

        Returns:
            CpsApi: the created API object
        """
        try:
            settings = ProfileSettings()  # type: ignore[call-arg]
        except ValidationError:
            settings_mgr = SettingsManager()
            settings = settings_mgr.get_profile_settings(profile_name=profile_name)
        return cls.from_settings(settings=settings)

    @classmethod
    def from_settings(cls, settings: ProfileSettings) -> CpsApi:
        """Create an API object from the provided settings.

        Args:
            settings (ProfileSettings): the settings to use.

        Returns:
            CpsApi: the created API object
        """
        auth = DeepSearchKeyAuth(
            username=settings.username,
            api_key=settings.api_key.get_secret_value(),
        )
        config = DeepSearchConfig(
            host=settings.host,
            auth=auth,
            verify_ssl=settings.verify_ssl,
        )
        client = CpsApiClient(config)
        return cls(client)
