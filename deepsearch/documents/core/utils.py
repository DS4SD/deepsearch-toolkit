import datetime
import glob
import os
import pathlib
import urllib
import zipfile as z
from pathlib import Path
from typing import Any, List

import requests
from tqdm import tqdm

from deepsearch.cps.client.api import CpsApi

from .common_routines import progressbar


class URLNavigator:
    def __init__(self, api: CpsApi) -> None:
        self.api = api
        self.url_host = self.api.client.swagger_client.configuration.host
        self.url_linked_ccs = urllib.parse.urljoin(self.url_host, "/api/linked-ccs")
        self.url_user_management = "/user/v1"
        self.url_public_apis = "/public/v4"

    def url_request_status(self, ccs_proj_key: str, task_id: str):
        wait = 5
        return f"{self.url_linked_ccs}{self.url_public_apis}/projects/{ccs_proj_key}/tasks/{task_id}/status?wait={wait}"

    def url_convert(self, ccs_proj_key: str):
        return f"{self.url_linked_ccs}{self.url_public_apis}/projects/{ccs_proj_key}/pipelines/convert"

    def url_result(self, ccs_proj_key: str, task_id: str):
        return f"{self.url_linked_ccs}{self.url_public_apis}/projects/{ccs_proj_key}/document_conversions/{task_id}/result"


def batch_single_files(
    source_path: Path, root_dir: Path, progress_bar=False
) -> List[List[str]]:
    """
    Batch individual pdfs into zip files.
    """
    MAX_BATCH_SIZE = 20 * 1e6  # 20 Mb
    zipdir = os.path.join(root_dir, "tmpzip/")
    # create directory for batches
    if not os.path.isdir(zipdir):
        os.makedirs(zipdir)

    # clear previous tmpzips
    previous_tmpzips = glob.glob(os.path.join(zipdir, "**/*.zip"), recursive=True)
    for f in previous_tmpzips:
        os.remove(os.path.abspath(f))

    # set up zip archive
    zipfilenumber = 0
    zipfilename = f"{0:04}{zipfilenumber}.zip"
    current_zipbatch = zipdir + zipfilename

    # get input pdf files
    files_pdf: List[Any] = []
    if os.path.isdir(source_path):
        files_pdf = glob.glob(os.path.join(source_path, "**/*.pdf"), recursive=True)
    elif os.path.isfile(source_path):
        file_extension = pathlib.Path(source_path).suffix
        if file_extension == ".pdf":
            files_pdf = [source_path]

    # catch all filenames and batch names
    batched_files = []
    if len(files_pdf) != 0:
        with tqdm(
            total=len(files_pdf),
            desc=f"{'Processing input:': <{progressbar.padding}}",
            disable=not (progress_bar),
            colour=progressbar.colour,
            bar_format=progressbar.bar_format,
        ) as progress:
            # loop over pdfs
            for single_doc in files_pdf:
                # check size of current zip file
                try:
                    if os.path.getsize(current_zipbatch) > MAX_BATCH_SIZE:
                        zipfilenumber += 1
                        zipfilename = f"{0:04}{zipfilenumber}.zip"
                        current_zipbatch = zipdir + zipfilename
                except FileNotFoundError:
                    pass
                # build name to avoid duplicate names inside batch
                if len(files_pdf) > 1:
                    arcname = str(single_doc)[
                        len(os.path.commonpath(files_pdf)) + 1 :
                    ].replace("/", "__")
                else:
                    arcname = os.path.basename(single_doc)

                with z.ZipFile(current_zipbatch, mode="a") as zipf:
                    zipf.write(filename=single_doc, arcname=arcname)
                # store batch/file name for creating report
                batched_files.append([arcname, current_zipbatch])
                progress.update(1)

    return batched_files


def create_root_dir() -> Path:
    """
    Creates root directory labelled with timestamp
    """
    # get timestamp
    ts = datetime.datetime.now().strftime("%Y-%m-%d_%Hh%Mm%Ss")
    root_dir = Path(f"./results_{ts}/")
    root_dir.mkdir(parents=True)

    return root_dir


def cleanup(root_dir: Path):
    """
    Clean temporarily created zip batches.
    """
    import shutil

    zipdir = os.path.join(root_dir, "tmpzip")
    try:
        shutil.rmtree(zipdir)
    except OSError:
        pass

    # check if rootdir is empty. if yes, then delete it
    if len(os.listdir(root_dir)) == 0:
        shutil.rmtree(root_dir)

    return


def download_url(url: str, save_path: Path, chunk_size=128):
    """
    Download contents from a url.
    """
    r = requests.get(url, stream=True, verify=False)
    with open(save_path, "wb") as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)
    return


def get_urls(url_path: Path) -> List[str]:
    """
    Returns list of url from input file.
    """

    lines = url_path.read_text()
    urls = [line.strip() for line in lines.split("\n") if line.strip() != ""]
    return urls
