import json
import os
import shutil
import tarfile
import zipfile
from typing import Dict, List

import requests
from tqdm import tqdm

default_cache_location = "/".join(__file__.split("/")[:-1]) + "/model_cache"
default_download_directory = "/".join(__file__.split("/")[:-1]) + "/temp_downloads"

def infer_target_directory() -> str:
    env = os.getenv("DEEPSEARCH_ARTIFACT_INDEX")
    return os.getcwd() if env is None else env


def check_artifact_index(target_directory: str) -> str:
    file_path = os.path.join(target_directory, "index.info")

    try:
        with open(file_path, "r") as file:
            data = json.load(file)

            if "artifact_index" in data:
                artifact_index = data["artifact_index"]
            else:
                raise Exception(
                    "The current working directory is not an artifact store."
                )
    except FileNotFoundError:
        raise Exception(
            "index.info file not found, could not deduce artifact store from current context"
        )
    return artifact_index


def get_artifacts_in_store(artifact_store: str) -> List:
    directories = []

    for entry in os.scandir(artifact_store):
        if entry.is_dir():
            full_path = os.path.join(artifact_store, entry.name)
            folder_name = entry.name
            directories.append(
                {
                    "full_path": full_path,
                    "folder_name": folder_name,
                }
            )

    return directories


def get_model_meta(artifact_store: str, model_name: str) -> Dict:
    folder_path = os.path.join(artifact_store, model_name)
    file_path = os.path.join(folder_path, "meta.info")

    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"The meta.info file does not exist in the folder {model_name}."
        )

    with open(file_path, "r") as file:
        meta_info = json.load(file)

    return meta_info


def download_file(model_info: Dict, directory: str) -> str:
    # Create the directory if it doesn't exist
    os.makedirs(directory, exist_ok=True)

    # Get the filename from the URL
    filename = model_info["model_filename"]
    file_path = os.path.join(directory, filename)

    # Download the file
    response = requests.get(model_info["static_url"], stream=True)
    response.raise_for_status()  # Check if the request was successful

    total_size = int(response.headers.get("content-length", 0))
    block_size = 1024  # 1 KB
    progress_bar = tqdm(total=total_size, unit="B", unit_scale=True)

    with open(file_path, "wb") as file:
        for data in response.iter_content(block_size):
            file.write(data)
            progress_bar.update(len(data))

    progress_bar.close()
    print(f"File downloaded successfully to: {file_path}")
    return file_path


def process_downloaded_file(downloaded_file: str, target_folder: str, basename: str, origin_store: str):
    # Extract the filename and the extension
    filename = os.path.basename(downloaded_file)
    _, extension = os.path.splitext(filename)

    # Create the target folder with the same name as the file (without extension)
    folder_name = os.path.join(target_folder, basename)
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
        information = {
            "from_store": origin_store
        }

        with open(folder_name + "/origin.info", "w") as fp:
            json.dump(information, fp)

    print("File processed successfully.")


def get_artifacts_in_cache(cache_dir: str) -> List:
    directories = []

    for entry in os.scandir(cache_dir):
        if entry.is_dir():
            full_path = os.path.join(cache_dir, entry.name)
            folder_name = entry.name
            with open(full_path + "/origin.info", "r") as fp:
                model_origin = json.load(fp)
            directories.append(
                {"full_path": full_path,
                 "folder_name": folder_name,
                 "origin_info": model_origin
                }
            )

    return directories

def infer_cache_directory() -> str:
    # TODO

    return default_cache_location
    env = os.getenv("DEEPSEARCH_ARTIFACT_INDEX")
    return os.getcwd() if env is None else env

def get_artifact_location_in_cache(artifact_name: str=None) -> str:
    cache_directory = infer_cache_directory()
    artifacts_in_cache = get_artifacts_in_cache(cache_directory)
    for artifact in artifacts_in_cache:
        if "folder_name" in artifact and artifact["folder_name"] == artifact_name:
            print(artifact_name)


get_artifact_location_in_cache("plotemy_v1.0.5")



