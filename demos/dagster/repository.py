"""
This module defines the Dagster pipeline repository.
"""
from dagster import repository

from pipelines.example_pipeline import cereal_data_pipeline


@repository
def team_one():
    return {
        "pipelines": {
            "cereal_data_pipeline": lambda: cereal_data_pipeline
        }
    }
