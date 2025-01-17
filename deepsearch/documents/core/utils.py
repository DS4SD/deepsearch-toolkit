import datetime
import glob
import os
import pathlib
import zipfile as z
from pathlib import Path
from typing import Any, List

import requests
from tqdm import tqdm

from .common_routines import progressbar

ALLOWED_FILE_EXTENSIONS = [".pdf", ".jpg", ".jpeg", ".tiff", ".tif", ".png", ".gif"]


def batch_single_files(
    source_path: Path, root_dir: Path, progress_bar=False
) -> List[List[str]]:
    """
    Batch individual input files into zip files.

    Output
        bfiles: List[List[str]]
        outer list corresponds to each batch
        inner list corresponds to individual file in a batch
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

    # get input files
    files_to_upload: List[Any] = []
    if os.path.isdir(source_path):
        for ext in ALLOWED_FILE_EXTENSIONS:
            files_to_upload.extend(
                glob.glob(os.path.join(source_path, f"**/*{ext}"), recursive=True)
            )
    elif os.path.isfile(source_path):
        file_extension = pathlib.Path(source_path).suffix
        if file_extension in ALLOWED_FILE_EXTENSIONS:
            files_to_upload = [source_path]

    # catch all filenames and batch names
    batched_files = []

    if len(files_to_upload) != 0:
        with tqdm(
            total=len(files_to_upload),
            desc=f"{'Processing input:': <{progressbar.padding}}",
            disable=not (progress_bar),
            colour=progressbar.colour,
            bar_format=progressbar.bar_format,
        ) as progress:
            # loop over input files
            for single_doc in files_to_upload:
                # check size of current zip file
                try:
                    if os.path.getsize(current_zipbatch) > MAX_BATCH_SIZE:
                        zipfilenumber += 1
                        zipfilename = f"{0:04}{zipfilenumber}.zip"
                        current_zipbatch = zipdir + zipfilename
                except FileNotFoundError:
                    pass
                # build name to avoid duplicate names inside batch
                if len(files_to_upload) > 1:
                    arcname = str(single_doc)[
                        len(os.path.commonpath(files_to_upload)) + 1 :
                    ].replace("/", "__")
                else:
                    arcname = os.path.basename(single_doc)

                # write file in batch
                with z.ZipFile(current_zipbatch, mode="a") as zipf:
                    zipf.write(filename=single_doc, arcname=arcname)
                # store batch/file name for creating report
                batched_files.append([arcname, current_zipbatch])
                progress.update(1)

    # get batched files out in the format we need i.e. list of sublist
    bfiles = []
    index = 0
    while index < len(batched_files):
        files = []
        previous_batch = batched_files[index][1]
        while batched_files[index][1] == previous_batch:
            files.append(batched_files[index][0])
            index += 1
            if index == len(batched_files):
                break
        bfiles.append(files)

    # add existing zip files to bfiles (for reporting purposes)
    files_zip = []
    if os.path.isdir(source_path):
        files_zip = glob.glob(os.path.join(source_path, "**/*.zip"), recursive=True)
    elif os.path.isfile(source_path):
        file_extension = pathlib.Path(source_path).suffix
        if file_extension == ".zip":
            files_zip = [str(source_path)]

    if len(files_zip) > 0:
        files_zip = [os.path.basename(item) for item in files_zip]
        bfiles = bfiles + [[item] for item in files_zip]

    return bfiles


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


def read_lines(file_path: Path) -> List[str]:
    """
    Returns list of lines from input file.
    """

    lines = file_path.read_text()
    line = [line.strip() for line in lines.split("\n") if line.strip() != ""]
    return line


def write_taskids(result_dir: Path, list_to_write: List[str]) -> None:
    """
    Write lines in result_dir
    """
    with open(result_dir.joinpath("task_ids.txt").absolute(), "w") as text_file:
        for t in list_to_write:
            text_file.write(t + "\n")
    return
