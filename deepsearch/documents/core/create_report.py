import csv
import logging
import os
from pathlib import Path
from typing import Any, List, Union

import requests
from tqdm import tqdm

from deepsearch.core.util.ccs_utils import get_ccs_project_key
from deepsearch.cps.client.api import CpsApi
from deepsearch.documents.core.common_routines import ERROR_MSG, progressbar
from deepsearch.documents.core.utils import URLNavigator

logger = logging.getLogger(__name__)


def get_single_report(api: CpsApi, cps_proj_key: str, task_id: str):
    """
    Get report of document conversion per individual task id
    """
    # get ccs project key and collection name
    ccs_proj_key, collection_name = get_ccs_project_key(
        api=api, cps_proj_key=cps_proj_key
    )
    try:
        request_report = api.client.session.get(
            url=URLNavigator(api).url_report_metrics(
                ccs_proj_key=ccs_proj_key, task_id=task_id
            )
        )
        request_report.raise_for_status()

        # we do not expose the full report but filter it a bit:
        keys = [
            "document_count",
            "failed_document_count",
            "page_count",
            "created",
            "completed",
        ]
        report = {key: request_report.json()[key] for key in keys}
        return report

    except requests.exceptions.HTTPError as err:
        # TODO Group all errors in the toolkit into proper classes
        logger.error(f"HTTPError {err}.\n{ERROR_MSG}\nAborting!")
        raise


def get_multiple_reports(
    api: CpsApi,
    cps_proj_key: str,
    task_ids: List[str],
    source_files: Union[List[List[str]], List[str], Any],
    result_dir: Path,
    progress_bar=False,
):
    """
    Generates reports for multiple tasks_ids and associated documents.
    """
    reports = []
    count, count_doc, count_failed_doc, = (
        0,
        0,
        0,
    )
    # start disk writing
    report_name = os.path.join(result_dir, "report.csv")
    with open(report_name, mode="a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["batch_number", "task_id", "status", "document"])

        # start loop
        with tqdm(
            total=len(task_ids),
            desc=f"{'Generating report:': <{progressbar.padding}}",
            disable=not (progress_bar),
            colour=progressbar.colour,
            bar_format=progressbar.bar_format,
        ) as progress:
            # loop over all files
            for index in range(len(task_ids)):
                count += 1
                report = get_single_report(
                    api=api, cps_proj_key=cps_proj_key, task_id=task_ids[index]
                )
                count_doc += report["document_count"]
                count_failed_doc += report["failed_document_count"]

                # batches which have partial failures are identified:
                if report["failed_document_count"] == 0:
                    status = "SUCCESS"
                elif report["failed_document_count"] < report["document_count"]:
                    status = "PARTIAL_SUCCESS"
                elif report["failed_document_count"] == report["document_count"]:
                    status = "FAILURE"
                else:
                    status = "ERROR"  # empty reports are marked as errors

                # update disk report
                if source_files == None:
                    writer.writerow(
                        [
                            count,
                            task_ids[index],
                            status,
                        ]
                    )
                else:
                    writer.writerow(
                        [count, task_ids[index], status, source_files[index]]
                    )
                reports.append(report)
                progress.update(1)

    # generate cumulative report
    info = {
        "Total documents": count_doc,
        "Successfully converted documents": count_doc - count_failed_doc,
    }

    return info
