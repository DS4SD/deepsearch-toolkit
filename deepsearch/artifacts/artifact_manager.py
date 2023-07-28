import json
import os
import shutil
import tempfile
from pathlib import Path
from typing import Dict, List, Optional
from urllib.parse import urlparse

import requests
from tqdm import tqdm

from deepsearch.artifacts.settings import ArtifactSettings


class ArtifactManager:
    def __init__(self, settings: Optional[ArtifactSettings] = None):
        self._settings = settings or ArtifactSettings()
        self._index_path = Path(self._settings.index_path)
        self._cache_path = Path(self._settings.cache_path)
        self._cache_path.mkdir(parents=True, exist_ok=True)

    def get_cache_path(self) -> Path:
        return self._cache_path

    def get_index_path(self) -> Path:
        return self._index_path

    def get_artifact_path_in_cache(self, artifact_name: str) -> Path:
        artifact_path = self._cache_path / artifact_name
        if not artifact_path.exists():
            raise FileNotFoundError(f'Artifact "{artifact_name}" not in cache')
        return artifact_path

    def download_artifact_to_cache(
        self,
        artifact_name: str,
    ) -> None:
        artifact_path = self._cache_path / artifact_name
        if artifact_path.exists():
            if self._settings.hit_strategy == ArtifactSettings.HitStrategy.RAISE:
                raise ValueError(f'Artifact "{artifact_name}" already in cache')
            elif self._settings.hit_strategy == ArtifactSettings.HitStrategy.PASS:
                return
            elif self._settings.hit_strategy == ArtifactSettings.HitStrategy.OVERWRITE:
                shutil.rmtree(artifact_path)
            else:
                raise RuntimeError(
                    f'Unexcpected value "{self._settings.hit_strategy=}"'
                )

        artifact_path.mkdir(exist_ok=False)

        # read metadata from file
        meta_path = self._index_path / artifact_name / self._settings.meta_filename
        with open(meta_path, "r") as meta_file:
            artifact_meta = json.load(meta_file)
        download_url = artifact_meta[self._settings.meta_url_field]

        with tempfile.TemporaryDirectory() as temp_dir:
            download_path = self._download_file(
                artifact_name=artifact_name,
                download_url=download_url,
                download_root_path=Path(temp_dir),
                with_progress_bar=self._settings.progress_bar,
            )
            self._finalize_download(
                download_path=download_path,
                target_path=artifact_path,
                unpack_archives=self._settings.unpack_archives,
            )

    def get_artifacts_in_index(self) -> List[str]:
        artifacts = []
        for entry in os.scandir(self._index_path):
            artifact_name = entry.name
            meta_file_path = (
                self._index_path / artifact_name / self._settings.meta_filename
            )
            if meta_file_path.exists():
                artifacts.append(artifact_name)
        return artifacts

    def get_artifacts_in_cache(self) -> List[str]:
        artifacts = []
        for entry in os.scandir(self._cache_path):
            artifact_name = entry.name
            artifact_path = self._cache_path / artifact_name
            if artifact_path.is_dir():
                artifacts.append(artifact_name)
        return artifacts

    def _download_file(
        self,
        artifact_name: str,
        download_url: str,
        download_root_path: Path,
        with_progress_bar: bool,
    ) -> Path:
        response = requests.get(download_url, stream=True)
        response.raise_for_status()

        dl_filename = None

        # try to get filename from response header
        cont_disposition = response.headers.get("Content-Disposition")
        if cont_disposition:
            disp_params = cont_disposition.strip().split(";")
            for par in disp_params:
                split_param = par.split("=")
                # currently only handling directive "filename" (not "*filename")
                if len(split_param) > 0 and split_param[0].strip() == "filename":
                    dl_filename = "=".join(split_param[1:]).strip().strip("'\"")
                    break

        # otherwise, use name from URL:
        if dl_filename is None:
            parsed_url = urlparse(download_url)
            dl_filename = Path(parsed_url.path).name

        total_size = int(response.headers.get("content-length", 0))
        block_size = 1024  # 1 KB
        if with_progress_bar:
            progress_bar = tqdm(total=total_size, unit="B", unit_scale=True)
            progress_bar.set_description(
                f'Downloading "{dl_filename}" ("{artifact_name}")'
            )

        download_path = download_root_path / dl_filename
        with open(download_path, "wb") as file:
            for data in response.iter_content(block_size):
                file.write(data)
                if with_progress_bar:
                    progress_bar.update(len(data))

        if with_progress_bar:
            progress_bar.close()

        return download_path

    def _finalize_download(
        self,
        download_path: Path,
        target_path: Path,
        unpack_archives: bool = True,
    ) -> None:

        dl_filename = download_path.name
        dl_path_str = str(download_path.resolve())
        attempt_unpack = False
        if unpack_archives:
            unpack_formats = shutil.get_unpack_formats()
            unpack_extensions = [
                e for unpk_frmt in unpack_formats for e in unpk_frmt[1]
            ]
            for ext in unpack_extensions:
                if dl_filename.endswith(ext):
                    attempt_unpack = True

        if attempt_unpack:
            shutil.unpack_archive(dl_path_str, target_path)
        else:
            shutil.move(dl_path_str, target_path / "")

    def _get_artifact_meta(self, artifact_name: str) -> Dict:
        file_path = self._index_path / artifact_name / self._settings.meta_filename
        if not file_path.exists():
            raise FileNotFoundError(f'File "{file_path}" does not exist')
        with open(file_path, "r") as file:
            meta_info = json.load(file)
        return meta_info
