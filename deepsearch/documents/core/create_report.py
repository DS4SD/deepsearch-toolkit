import csv
import glob
import os
import pathlib
import tempfile
from pathlib import Path
from typing import Any, List

from .utils import batch_single_files


def report_urls(
    result_dir: Path, urls: List[str], statuses: List[str], task_ids: List[str]
):
    """
    Function to create report when DeepSearch is converting urls.
    """
    report_name = os.path.join(result_dir, "report.csv")
    info = {
        "Total online documents": len(urls),
        "Successfully converted documents": statuses.count("SUCCESS"),
    }

    with open(report_name, mode="a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["s. no.", "task_id", "status", "url"])
        for index in range(len(task_ids)):
            writer.writerow([index + 1, task_ids[index], statuses[index], urls[index]])

    return info


def report_docs(
    result_dir: Path,
    statuses: List[str],
    task_ids: List[str],
    source_path: Path,
):
    """
    Function to create report when DeepSearch is converting local documents.
    """
    report_name = os.path.join(result_dir, "report.csv")

    with tempfile.TemporaryDirectory() as tmpdir:
        batched_files = batch_single_files(
            source_path=source_path, root_dir=Path(tmpdir)
        )
        # batched_files only contains information about single pdfs
        # user zips are collected again
        files_zip: List[Any] = []
        if os.path.isdir(source_path):
            files_zip = glob.glob(os.path.join(source_path, "**/*.zip"), recursive=True)
        elif os.path.isfile(source_path):
            file_extension = pathlib.Path(source_path).suffix
            if file_extension == ".zip":
                files_zip = [source_path]

        count_total_docs = len(batched_files) + len(files_zip)

        # count batched zips
        files_tmpzip = glob.glob(
            os.path.join(tmpdir, "tmpzip/**/*.zip"), recursive=True
        )
        files_zip = files_zip + files_tmpzip
        # if report generation is called after results are stored, they may appear as zip files.
        # we remove them from out list.
        files_zip = [item for item in files_zip if str(result_dir) not in item]

    info = {
        "Total files (pdf+zip)": count_total_docs,
        "Total batches": len(files_zip),
        "Successfully converted batches": statuses.count("SUCCESS"),
    }

    batch_done = []
    with open(report_name, mode="a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["s. no.", "task_id", "status", "document"])

        # following part prints report pdf by pdf
        count = 1
        for file, batch in batched_files:
            writer.writerow(
                [
                    count,
                    task_ids[files_zip.index(batch)],
                    statuses[files_zip.index(batch)],
                    file,
                ]
            )
            count += 1
            batch_done.append(batch)
        for batch in files_zip:
            if batch not in batch_done:
                writer.writerow(
                    [
                        count,
                        task_ids[files_zip.index(batch)],
                        statuses[files_zip.index(batch)],
                        batch,
                    ]
                )
            count += 1
            batch_done.append(batch)
    return info
