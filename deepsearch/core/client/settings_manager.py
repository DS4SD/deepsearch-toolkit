import os
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Dict, List, Optional

import platformdirs
from pydantic.v1 import ValidationError

from deepsearch.core.cli.profile_utils import (
    MSG_AMBIGUOUS_SUCCESSOR,
    MSG_NO_PROFILE_SELECTED,
    MSG_NO_PROFILES_DEFINED,
)
from deepsearch.core.client.config import DeepSearchConfig, DeepSearchKeyAuth
from deepsearch.core.client.settings import MainSettings, ProfileSettings

FALLBACK_PRFL_NAME = "ds"
MAIN_DOTENV_FILENAME = "main.env"
PROFILES_DIR_NAME = "profiles"
LEGACY_CFG_FILENAME = "deepsearch_toolkit.json"


class KnownProfile(str, Enum):
    SDS = "sds"
    DS_EXPERIENCE = "ds-experience"
    DS_INTERNAL = "ds-internal"


HOST_BY_PROFILE = {
    KnownProfile.SDS.value: "https://sds.app.accelerate.science",
    KnownProfile.DS_EXPERIENCE.value: "https://deepsearch-experience.res.ibm.com",
    KnownProfile.DS_INTERNAL.value: "https://cps.foc-deepsearch.zurich.ibm.com",
}


@dataclass
class ProfileSettingsEntry:
    path: Path
    settings: ProfileSettings


class SettingsManager:
    def __init__(self) -> None:
        """Initialize a SettingsManager instance. We allow cases with no selected profile
        despite available ones to go through initialization; these have to get handled
        as needed, when needed."""
        self.config_root_path = Path(
            platformdirs.user_config_dir(
                appname="DeepSearch",
                appauthor="IBM",
                ensure_exists=True,
            )
        )
        self._main_path = self.config_root_path / MAIN_DOTENV_FILENAME
        self._main_settings = MainSettings(_env_file=self._main_path)  # type: ignore
        # suppressing due to known Pydantic bug https://github.com/pydantic/pydantic/issues/3072

        self._profile_root_path = self.config_root_path / PROFILES_DIR_NAME
        self._profile_root_path.mkdir(exist_ok=True)

        # initialize internal profile cache from Pydantic Settings based on dotenv
        self._profile_cache: Dict[str, ProfileSettingsEntry] = {}
        paths_to_remove: List[Path] = []
        for f in os.listdir(self._profile_root_path):
            file_path = self._profile_root_path / f
            if file_path.suffix == ".env":
                profile_name = file_path.stem
                try:
                    profile_settings = ProfileSettings(_env_file=file_path)  # type: ignore
                    # suppressing due to known Pydantic bug https://github.com/pydantic/pydantic/issues/3072

                    self._profile_cache[profile_name] = ProfileSettingsEntry(
                        path=file_path,
                        settings=profile_settings,
                    )
                except ValidationError:
                    paths_to_remove.append(file_path)

        # handle any invalid profiles
        if paths_to_remove:
            for path_to_rem in paths_to_remove:
                path_to_rem.unlink()
            profile_names = ", ".join([f'"{p.stem}"' for p in paths_to_remove])
            err_msg = f"Following profiles were invalid and have been removed: {profile_names}; if needed please re-add"
            raise RuntimeError(err_msg)

        # reset any stale active profile config
        if (
            self._main_settings.profile is not None
            and self._main_settings.profile not in self._profile_cache
        ):
            prfl_attr_name = [
                name
                for name, value in vars(self._main_settings).items()
                if value == self._main_settings.profile
            ][0]
            prfl_env_var = self._main_settings.get_env_var_name(prfl_attr_name)
            # if value coming from sth else than env var, i.e. from dotenv file
            # (to prevent unnecessarily updating the dotenv file)
            if self._main_settings.profile != os.getenv(prfl_env_var):
                self._persist_main_settings(profile_name=None)

        # automatically set active profile in case of single available profile
        if self._main_settings.profile is None and len(self._profile_cache) == 1:
            self.activate_profile(profile_name=str(next(iter(self._profile_cache))))

        self._migrate_legacy_config()

    def _migrate_legacy_config(self) -> None:
        if self._main_settings.profile is None:
            legacy_cfg_path = self.config_root_path / LEGACY_CFG_FILENAME
            if legacy_cfg_path.exists():
                legacy_cfg = DeepSearchConfig.parse_file(legacy_cfg_path)
                if isinstance(legacy_cfg.auth, DeepSearchKeyAuth):
                    new_cfg = ProfileSettings(
                        host=legacy_cfg.host,
                        username=legacy_cfg.auth.username,
                        api_key=legacy_cfg.auth.api_key,  # type: ignore[arg-type]
                        verify_ssl=legacy_cfg.verify_ssl,
                    )
                    self.save_settings(
                        profile_settgs=new_cfg,
                        profile_name=FALLBACK_PRFL_NAME,
                        activate_profile=True,
                    )
                    legacy_cfg_path.unlink()  # remove legacy config file

    def _get_profile_path(self, profile_name: str) -> Path:
        return self._profile_root_path / f"{profile_name}.env"

    def get_all_profile_settings(self) -> Dict[str, ProfileSettings]:
        return {k: self._profile_cache[k].settings for k in self._profile_cache}

    def get_active_profile(self) -> Optional[str]:
        return self._main_settings.profile

    def get_profile_name_suggestion(self) -> str:
        return self._main_settings.profile or FALLBACK_PRFL_NAME

    def get_profile_settings(
        self, profile_name: Optional[str] = None
    ) -> ProfileSettings:
        prfl_name = profile_name or self.get_active_profile()
        if prfl_name is None:
            try:  # try to instantiate from environment alone
                return ProfileSettings()  # type: ignore[call-arg]
            except ValidationError:
                if len(self._profile_cache) == 0:
                    raise RuntimeError(MSG_NO_PROFILES_DEFINED)
                else:
                    raise RuntimeError(MSG_NO_PROFILE_SELECTED)
        else:
            return self._safe_get_profile_entry(profile_name=prfl_name).settings

    def save_settings(
        self,
        profile_settgs: ProfileSettings,
        profile_name: str,
        activate_profile: bool,
    ) -> None:
        profile_path = self._get_profile_path(profile_name=profile_name)
        profile_settgs.dump(target=profile_path)

        self._profile_cache[profile_name] = ProfileSettingsEntry(
            path=profile_path,
            settings=profile_settgs,
        )

        # activate also if first profile
        if activate_profile or len(self._profile_cache) == 1:
            self.activate_profile(profile_name=profile_name)

    def _persist_main_settings(self, profile_name: Optional[str]) -> None:
        self._main_settings.profile = profile_name
        self._main_settings.dump(self._main_path)

    def activate_profile(self, profile_name: str) -> None:
        self._validate_existing_profile_name(profile_name=profile_name)
        self._persist_main_settings(profile_name=profile_name)

    def _safe_get_profile_entry(self, profile_name: str) -> ProfileSettingsEntry:
        try:
            return self._profile_cache[profile_name]
        except KeyError:
            if url := HOST_BY_PROFILE.get(profile_name):
                msg = f'Profile "{profile_name}" not configured. To set up, go to: {url}/credentials'
            else:
                msg = f'No profile "{profile_name}" configured. To set up, check: `deepsearch profile config --help`'
            raise ValueError(msg)

    def _validate_existing_profile_name(self, profile_name: str) -> None:
        _ = self._safe_get_profile_entry(profile_name=profile_name)

    def remove_profile(self, profile_name: str) -> None:
        self._validate_existing_profile_name(profile_name=profile_name)
        num_profiles = len(self._profile_cache)
        if num_profiles == 1:
            self._persist_main_settings(profile_name=None)
        elif num_profiles == 2:
            successor = None
            for k in self._profile_cache:
                if k != profile_name:
                    successor = k
                    break
            if successor is None:
                raise RuntimeError("Internal error: cannot determine profile successor")
            self.activate_profile(profile_name=successor)
        elif self._main_settings.profile == profile_name:
            raise ValueError(MSG_AMBIGUOUS_SUCCESSOR)

        prfl_settgs_entry = self._profile_cache.pop(profile_name)  # update cache
        prfl_settgs_entry.path.unlink()  # remove file
