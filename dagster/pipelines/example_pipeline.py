"""
Example Dagster solids and pipeline from the Dagster tutorial.
"""
import csv
from typing import Any, Dict, List

import requests
from dagster import execute_pipeline, pipeline, solid
from dagster.core.execution.context.compute import SolidExecutionContext


@solid
def download_data(context: SolidExecutionContext) -> List[Dict[str, Any]]:
    """Download dataset."""
    response = requests.get("https://docs.dagster.io/assets/cereal.csv")
    lines = response.text.split("\n")
    cereals = [row for row in csv.DictReader(lines)]
    context.log.info(f"Found {len(cereals)} cereals")
    return cereals


@solid
def find_max_sugar_cereal(
    context: SolidExecutionContext, cereals: List[Dict[str, Any]]
) -> str:
    """X"""
    sorted_by_sugar = sorted(cereals, key=lambda cereal: cereal["sugars"])
    max_sugar_cereal = sorted_by_sugar[-1]["name"]
    context.log.info(f"{max_sugar_cereal} has the greatest amount of sugar.")
    return max_sugar_cereal


@pipeline
def cereal_data_pipeline() -> str:
    return find_max_sugar_cereal(download_data())


if __name__ == "__main__":
    result = execute_pipeline(cereal_data_pipeline)
