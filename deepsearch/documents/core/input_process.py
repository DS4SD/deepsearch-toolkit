import glob
import os
import pathlib
import zipfile as z
from pathlib import Path
from typing import Any, List

import typer
import urllib3
from tqdm import tqdm

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from .common_routines import ERROR_MSG, progressbar_padding, success_message
from .convert import (
    check_status_running_tasks,
    download_converted_docs,
    send_files_for_conversion,
    send_urls_for_conversion,
)
from .create_report import report_docs, report_urls

# set up basic urls
url_user_management = "/user/v1"
url_public_apis = "/public/v4"


def process_local_input(cps_proj_key: str, local_file: Path):
    """
    Classify the user provided local input and take appropriate action.
    """
    if not os.path.exists(local_file):
        typer.echo("Error: File not found. Check input.")
    else:
        root_dir = create_root_dir()
        batched_files = batch_single_files(local_file=local_file, root_dir=root_dir)
        task_ids = send_files_for_conversion(
            cps_proj_key=cps_proj_key, local_file=local_file, root_dir=root_dir
        )
        statuses = check_status_running_tasks(
            cps_proj_key=cps_proj_key, task_ids=task_ids
        )
        download_converted_docs(
            cps_proj_key=cps_proj_key, task_ids=task_ids, root_dir=root_dir
        )
        typer.echo(f"{success_message}\nResults: {os.path.abspath(root_dir)}")
        report_docs(
            root_dir=root_dir,
            batched_files=batched_files,
            task_ids=task_ids,
            statuses=statuses,
            local_file=local_file,
        )
        cleanup(root_dir=root_dir)
        return


def create_root_dir() -> Path:
    """
    Creates root directory labelled with timestamp
    """
    import datetime
    import time

    # get timestamp
    ts_now = time.time()
    ts = datetime.datetime.fromtimestamp(ts_now).strftime("%Y-%m-%d_%Hh%Mm%Ss")
    root_dir = Path(f"./results_{ts}/")

    if not os.path.isdir(root_dir):
        os.makedirs(root_dir)

    return root_dir


def batch_single_files(local_file: Path, root_dir: Path) -> List[List[str]]:
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
    if os.path.isdir(local_file):
        files_pdf = glob.glob(os.path.join(local_file, "**/*.pdf"), recursive=True)
    elif os.path.isfile(local_file):
        file_extension = pathlib.Path(local_file).suffix
        if file_extension == ".pdf":
            files_pdf = [local_file]

    # catch all filenames and batch names
    batched_files = []
    if len(files_pdf) != 0:
        with tqdm(
            total=len(files_pdf),
            desc=f'{"Processing input:":<{progressbar_padding}}',
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
                # Following is for python 3.9^
                # arcname = (
                #     str(single_doc)
                #     .removeprefix(os.path.commonpath(files_pdf) + "/")
                #     .replace("/", "__")
                # )
                # Otherwise:
                arcname = str(single_doc)[
                    len(os.path.commonpath(files_pdf)) + 1 :
                ].replace("/", "__")
                with z.ZipFile(current_zipbatch, mode="a") as zipf:
                    zipf.write(filename=single_doc, arcname=arcname)
                # store batch/file name for creating report
                batched_files.append([arcname, current_zipbatch])
                progress.update(1)

    return batched_files


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


def process_url_input(cps_proj_key: str, url: str):
    """
    Classify user provided url(s) and take appropriate action.
    """
    if not os.path.isfile(url):
        # deal with single url input
        urls = [url]
    elif os.path.isfile(url):
        # deal with file
        urls = get_urls(url)
    root_dir = create_root_dir()
    task_ids = send_urls_for_conversion(cps_proj_key=cps_proj_key, urls=urls)
    statuses = check_status_running_tasks(cps_proj_key=cps_proj_key, task_ids=task_ids)
    download_converted_docs(
        cps_proj_key=cps_proj_key, task_ids=task_ids, root_dir=root_dir
    )
    typer.echo(f"{success_message}\nResults: {os.path.abspath(root_dir)}")
    report_urls(root_dir=root_dir, urls=urls, task_ids=task_ids, statuses=statuses)
    return


def get_urls(url: str) -> List[str]:
    """
    Returns list of url from input file.
    """
    with open(file=url, mode="r") as f:
        lines = f.read()

    urls = [line for line in lines.split("\n") if line.strip() != ""]
    return urls
