from __future__ import annotations

from enum import Enum
from getpass import getpass
from pathlib import Path
from typing import Dict, Union

import platformdirs
from pydantic import BaseSettings, SecretStr

CFG_ROOT_PATH = Path(
    platformdirs.user_config_dir(
        appname="DeepSearch",
        appauthor="IBM",
        ensure_exists=True,
    )
)


class SubPrefix(str, Enum):
    # NOTE: to prevent conflicts, values must not be substring of one another
    PROFILE = "PROFILE_"  # reserved for ProfileSettings
    PRFL_MGR = "PRM_"  # reserved for PrflManagerSettings
    MODEL_APP = "MODELAPP_"  # reserved for ModelAppSettings
    ARTIFACT = "ARTIFACT_"  # reserved for ArtifactSettings
    CLI = "CLI_"  # reserved for CLISettings


class DSSettings(BaseSettings):
    class Literals:
        PREFIX = "DEEPSEARCH_"

    @classmethod
    def build_prefix(cls, sub_prefix: SubPrefix) -> str:
        return DSSettings.Literals.PREFIX + sub_prefix

    @classmethod
    def get_env_var_name(cls, attr_name) -> str:
        return cls.Config.env_prefix + attr_name.upper()

    def _get_serializable_dict(self) -> Dict[str, str]:
        result = {}
        model_dict = self.dict()
        for k in model_dict:
            new_key = self.get_env_var_name(attr_name=k)
            if isinstance((old_val := model_dict[k]), SecretStr):
                new_val = old_val.get_secret_value()
            else:
                new_val = old_val
            result[new_key] = new_val
        return result

    def dump(self, target: Union[str, Path]) -> None:
        target_path = Path(target)
        ser_dict = self._get_serializable_dict()
        with open(target_path, "w") as target_file:
            for k in ser_dict:
                if (val := ser_dict[k]) is not None:  # only dump existing values
                    target_file.write(f'{k}="{val}"\n')


class ProfileSettings(DSSettings):
    class Config:
        env_prefix = DSSettings.build_prefix(sub_prefix=SubPrefix.PROFILE)

    host: str
    username: str
    api_key: SecretStr
    verify_ssl: bool = True

    @classmethod
    def from_cli_prompt(cls) -> ProfileSettings:
        return cls(
            host=input("Host: "),
            username=input("Username: "),
            api_key=getpass("API key: "),
            verify_ssl=input("SSL verification [y/n]: "),
        )
