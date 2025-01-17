import csv
import logging
import os
from pathlib import Path

from tqdm import tqdm

from deepsearch.documents.core.common_routines import progressbar

logger = logging.getLogger(__name__)


def generate_report_csv(
    task_result: dict, task_id: str, result_dir: Path, progress_bar=False
):
    """
    Generate report of a document conversion task id and saves in a csv file
    """

    # we do not expose the full report but filter it a bit:
    keys = ["total_pages", "processed_pages", "truncated_pages"]
    report = {key: task_result[key] for key in keys}

    report_name = os.path.join(result_dir, "report.csv")
    with open(report_name, mode="a", newline="") as csvfile:
        with tqdm(
            total=1,
            desc=f"{'Generating report:': <{progressbar.padding}}",
            disable=not (progress_bar),
            colour=progressbar.colour,
            bar_format=progressbar.bar_format,
        ) as progress:
            writer = csv.writer(csvfile)
            writer.writerow(
                ["task_id", "total_pages", "processed_pages", "truncated_pages"]
            )
            writer.writerow(
                [
                    task_id,
                    report["total_pages"],
                    report["processed_pages"],
                    report["truncated_pages"],
                ]
            )
            progress.update(1)

    return report
