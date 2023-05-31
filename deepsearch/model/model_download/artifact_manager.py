import json
import os
import shutil
import tarfile
import tempfile
import zipfile
from pathlib import Path
from typing import Any, Dict, List, Optional

import platformdirs
import requests
from appdirs import *
from tqdm import tqdm


class ArtifactManager:
    def __init__(self):
        if os.getenv("DEEPSEARCH_ARTIFACT_INDEX"):
            self.infered_store_directory = os.getenv("DEEPSEARCH_ARTIFACT_INDEX")
        else:
            self.infered_store_directory = os.getcwd()
        if os.getenv("DEEPSEARCH_ARTIFACT_CACHE"):
            self.infered_cache_directory = os.getenv("DEEPSEARCH_ARTIFACT_CACHE")
        else:
            self.infered_cache_directory = platformdirs.user_cache_dir(
                "DeepSearch", "IBM"
            )
            if not Path(self.infered_cache_directory).is_dir():
                Path(self.infered_cache_directory).mkdir(parents=True)

    def get_artifact_location_in_cache(self, artifact_name: str):
        artifacts_in_cache = self.get_artifact_cache_list()
        for artifact in artifacts_in_cache:
            if "folder_name" in artifact and artifact["folder_name"] == artifact_name:
                return artifact

    def delete_artifact_from_cache(self, model: str):
        target_artifacts = []
        for artifact in self.get_artifact_cache_list():
            if "folder_name" in artifact and artifact["folder_name"] == model:
                target_artifacts.append(artifact)

        for artifact in target_artifacts:
            shutil.rmtree(artifact["full_path"])

    def download_artifact_to_cache(self, model: str, with_progess_bar: bool = False):
        model_meta = self._get_model_meta(self.infered_store_directory, model)
        temp_file = tempfile.TemporaryDirectory()
        downloaded_file_path = self._download_file(
            model_meta, temp_file, with_progess_bar
        )
        self._process_downloaded_file(downloaded_file_path, model)
        temp_file.cleanup()

    def get_artifact_cache_list(self) -> List:
        directories = []

        for entry in os.scandir(self.infered_cache_directory):
            if entry.is_dir():
                full_path = os.path.join(self.infered_cache_directory, entry.name)
                folder_name = entry.name
                directories.append(
                    {
                        "full_path": full_path,
                        "folder_name": folder_name,
                    }
                )

        return directories

    def get_artifact_store_list(self):
        directories = []

        for entry in os.scandir(self.infered_store_directory):
            if entry.is_dir():
                full_path = os.path.join(self.infered_store_directory, entry.name)
                folder_name = entry.name
                scanned_folder = {
                    "full_path": full_path,
                    "folder_name": folder_name,
                    "contents": [entry.name for entry in os.scandir(full_path)],
                }
                if not "meta.info" in scanned_folder["contents"]:
                    continue

                directories.append(
                    {
                        k: v
                        for k, v in scanned_folder.items()
                        if k in ["full_path", "folder_name"]
                    }
                )

        return directories

    def _process_downloaded_file(self, downloaded_file: str, basename: str):
        # Extract the filename and the extension
        filename = os.path.basename(downloaded_file)
        _, extension = os.path.splitext(filename)

        # Create the target folder with the same name as the file (without extension)
        folder_name = os.path.join(self.infered_cache_directory, basename)
        os.makedirs(folder_name, exist_ok=True)

        # Check if the file is compressed
        if extension == ".zip":
            with zipfile.ZipFile(downloaded_file, "r") as zip_ref:
                zip_ref.extractall(folder_name)
        elif extension == ".tar" or extension == ".gz" or extension == ".bz2":
            with tarfile.open(downloaded_file, "r") as tar_ref:
                tar_ref.extractall(folder_name)
        else:
            # Move the file to the target folder
            destination = os.path.join(folder_name, filename)
            shutil.move(downloaded_file, destination)
            # information = {
            #     "from_store": origin_store
            # }

            # with open(folder_name + "/origin.info", "w") as fp:
            #     json.dump(information, fp)

        print("File processed successfully.")

    # TODO Type hinting a tempfile object?
    def _download_file(
        self, model_info: Dict, directory: Any, with_progress_bar: bool = False
    ) -> str:
        # Get the filename from the URL
        filename = model_info["model_filename"]
        file_path = directory.name + f"/{filename}"

        # Download the file
        response = requests.get(model_info["static_url"], stream=True)
        response.raise_for_status()  # Check if the request was successful

        total_size = int(response.headers.get("content-length", 0))
        block_size = 1024  # 1 KB
        if with_progress_bar:
            progress_bar = tqdm(total=total_size, unit="B", unit_scale=True)

        with open(file_path, "wb") as file:
            for data in response.iter_content(block_size):
                file.write(data)
                if with_progress_bar:
                    progress_bar.update(len(data))

        if with_progress_bar:
            progress_bar.close()
        return file_path

    def _get_model_meta(self, artifact_store: str, model_name: str) -> Dict:
        folder_path = os.path.join(artifact_store, model_name)
        file_path = os.path.join(folder_path, "meta.info")

        if not os.path.exists(file_path):
            raise FileNotFoundError(
                f"The meta.info file does not exist in the folder {folder_path}."
            )

        with open(file_path, "r") as file:
            meta_info = json.load(file)

        return meta_info


def main():
    test = ArtifactManager()
    test.infered_store_directory = (
        "/".join(__file__.split("/")[:-1]) + "/artifact_index_b"
    )
    print(f"infered cache dir: {test.infered_cache_directory}")
    print(f"infered store dir: {test.infered_store_directory}")

    artifacts = test.get_artifact_store_list()
    print("Artifacts in store dir: ")
    for value in artifacts:
        print(value)

    test.download_artifact_to_cache(
        os.getenv("DEEPSEARCH_ARTIFACT_MODEL_NAME"), with_progess_bar=True
    )
    print("downloaded artifact")

    artifacts = test.get_artifact_cache_list()
    print("Artifacts in cache dir:")
    for value in artifacts:
        print(value)
    print()

    print(
        f"Artifact location is: {test.get_artifact_location_in_cache(os.getenv('DEEPSEARCH_ARTIFACT_MODEL_NAME'))}"
    )

    test.delete_artifact_from_cache(os.getenv("DEEPSEARCH_ARTIFACT_MODEL_NAME"))
    print("deleted artifact")


if __name__ == "__main__":
    main()
