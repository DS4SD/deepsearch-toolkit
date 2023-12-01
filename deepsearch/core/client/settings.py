from __future__ import annotations

from getpass import getpass
from pathlib import Path
from typing import Dict, Optional, Union

from pydantic.v1 import BaseSettings, SecretStr


class DumpableSettings(BaseSettings):
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


class ProfileSettings(DumpableSettings):
    host: str
    username: str
    api_key: SecretStr
    verify_ssl: bool = True

    class Config:
        env_prefix = "DEEPSEARCH_"

    @classmethod
    def from_cli_prompt(cls) -> ProfileSettings:
        return cls(
            host=input("Host: "),
            username=input("Username: "),
            api_key=getpass("API key: "),  # type: ignore[arg-type]
            verify_ssl=input("SSL verification [y/n]: "),  # type: ignore[arg-type]
        )


class MainSettings(DumpableSettings):
    profile: Optional[str] = None

    class Config:
        env_prefix = "DEEPSEARCH_"


class CLISettings(DumpableSettings):
    show_cli_stack_traces: bool = False

    class Config:
        env_prefix = "DEEPSEARCH_"
