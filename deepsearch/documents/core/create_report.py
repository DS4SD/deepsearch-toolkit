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

    pad = 35
    print(f"\n{'Total online documents:':<{pad}}{len(urls):04}")
    print(
        f"""{'Successfully converted documents:':<{pad}}{statuses.count('SUCCESS'):04}({int(100*statuses.count('SUCCESS')/len(urls))}%)"""
    )
    with open(report_name, mode="a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["s. no.", "task_id", "status", "url"])
        for index in range(len(task_ids)):
            writer.writerow([index + 1, task_ids[index], statuses[index], urls[index]])

    return


def report_docs(
    result_dir: Path,
    statuses: List[str],
    task_ids: List[str],
    local_file: Path,
):
    """
    Function to create report when DeepSearch is converting local documents.
    """
    report_name = os.path.join(result_dir, "report.csv")

    with tempfile.TemporaryDirectory() as tmpdir:
        batched_files = batch_single_files(local_file=local_file, root_dir=tmpdir)

        # batched_files only contains information about single pdfs
        # user zips are collected again
        files_zip: List[Any] = []
        if os.path.isdir(local_file):
            files_zip = glob.glob(os.path.join(local_file, "**/*.zip"), recursive=True)
        elif os.path.isfile(local_file):
            file_extension = pathlib.Path(local_file).suffix
            if file_extension == ".zip":
                files_zip = [local_file]

        count_total_docs = len(batched_files) + len(files_zip)

        # count batched zips
        files_tmpzip = glob.glob(
            os.path.join(tmpdir, "tmpzip/**/*.zip"), recursive=True
        )
        files_zip = files_zip + files_tmpzip

    pad = 35
    print(f"\n{'Total files (pdf+zip):':<{pad}}{count_total_docs:04}")
    print(f"{'Total batches:':<{pad}}{len(files_zip):04}")
    print(
        f"""{'Successfully converted batches:':<{pad}}{statuses.count('SUCCESS'):04}({int(100*statuses.count('SUCCESS')/len(files_zip))}%)"""
    )

    batch_done = []
    with open(report_name, mode="a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["s. no.", "task_id", "status", "document", "batch"])
        # following part prints report batch by batch
        # for index in range(len(files_zip)):
        # if files_zip[index] in batch_name:
        #     writer.writerow(
        #         [
        #             index + 1,
        #             task_ids[index],
        #             statuses[index],
        #             doc_file[batch_name.index(files_zip[index])],
        #             files_zip[index],
        #         ]
        #     )
        # else:
        #     writer.writerow(
        #         [
        #             index + 1,
        #             task_ids[index],
        #             statuses[index],
        #             os.path.basename(files_zip),
        #             files_zip[index],
        #         ]
        #     )
        # following part prints report pdf by pdf
        count = 1
        for file, batch in batched_files:
            writer.writerow(
                [
                    count,
                    task_ids[files_zip.index(batch)],
                    statuses[files_zip.index(batch)],
                    file,
                    batch,
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
                        batch,
                    ]
                )
            count += 1
            batch_done.append(batch)
    return
