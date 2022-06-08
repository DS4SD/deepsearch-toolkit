import csv
import datetime
import glob
import os
import pathlib
import time
from pathlib import Path
from typing import Any, List

import typer

from .common_routines import WELCOME


def report_urls(
    root_dir: Path, urls: List[str], statuses: List[str], task_ids: List[str]
):
    """
    Function to create report when DeepSearch is converting urls.
    """
    report_name = os.path.join(root_dir, "report.csv")
    time_s = os.path.basename(os.path.abspath(root_dir)).lstrip("results_")
    time_start = time.mktime(
        datetime.datetime.strptime(time_s, "%Y-%m-%d_%Hh%Mm%Ss").timetuple()
    )
    total_time = time.time() - time_start

    pad = 35
    typer.echo(f"\n{'Total online documents:':<{pad}}{len(urls):04}")
    typer.echo(
        f"""{'Successfully converted documents:':<{pad}}{statuses.count('SUCCESS'):04}({int(100*statuses.count('SUCCESS')/len(urls))}%)"""
    )
    if total_time < 60:
        typer.echo(f"{'Run time:':<{pad}}{total_time:.2f} seconds")
    elif total_time > 60 and total_time < 3600:
        typer.echo(f"{'Run time:':<{pad}}{total_time/60:.2f} minutes")
    else:
        typer.echo(f"{'Run time:':<{pad}}{total_time/3600:.2f} hours")

    with open(report_name, mode="a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["s. no.", "task_id", "status", "url"])
        for index in range(len(task_ids)):
            writer.writerow([index + 1, task_ids[index], statuses[index], urls[index]])

    return


def report_docs(
    root_dir: Path,
    batched_files: List[List[str]],
    statuses: List[str],
    task_ids: List[str],
    local_file: Path,
):
    """
    Function to create report when DeepSearch is converting local documents.
    """
    report_name = os.path.join(root_dir, "report.csv")
    time_s = os.path.basename(os.path.abspath(root_dir)).lstrip("results_")
    time_start = time.mktime(
        datetime.datetime.strptime(time_s, "%Y-%m-%d_%Hh%Mm%Ss").timetuple()
    )
    total_time = time.time() - time_start

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

    if root_dir is not None:
        files_tmpzip = glob.glob(
            os.path.join(root_dir, "tmpzip/**/*.zip"), recursive=True
        )
        files_zip = files_zip + files_tmpzip
    # catch document names from batched_files
    # docs = []
    # for file, batch in batched_files:
    #     if batch in files_zip:
    #         doc.append(file)
    #     else:
    #         doc.append()
    # doc_file, batch_name = zip(*batched_files)

    pad = 35
    typer.echo(f"\n{'Total files (pdf+zip):':<{pad}}{count_total_docs:04}")
    typer.echo(f"{'Total batches:':<{pad}}{len(files_zip):04}")
    typer.echo(
        f"""{'Successfully converted batches:':<{pad}}{statuses.count('SUCCESS'):04}({int(100*statuses.count('SUCCESS')/len(files_zip))}%)"""
    )
    if total_time < 60:
        typer.echo(f"{'Run time:':<{pad}}{total_time:.2f} seconds")
    elif total_time > 60 and total_time < 3600:
        typer.echo(f"{'Run time:':<{pad}}{total_time/60:.2f} minutes")
    else:
        typer.echo(f"{'Run time:':<{pad}}{total_time/3600:.2f} hours")
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
