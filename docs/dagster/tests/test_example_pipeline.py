"""
Unit tests for the example pipeline.
"""
from io import BytesIO
from unittest.mock import MagicMock, patch

from dagster import execute_pipeline, build_solid_context
from dagster.core.execution.context.compute import SolidExecutionContext
from pytest import fixture
from requests import Response

from pipelines.example_pipeline import cereal_data_pipeline, download_data


@fixture(scope="session")
def test_data() -> BytesIO:
    with open("tests/test_data.csv", "r+b") as f:
        file_bytes = f.read()
    return BytesIO(file_bytes)


@fixture(scope="session")
def context() -> SolidExecutionContext:
    return build_solid_context()


@patch("pipelines.example_pipeline.requests")
def test_download_data_downloads_data(
    mock_requests: MagicMock, test_data: BytesIO, context: SolidExecutionContext
):
    mock_response = Response()
    mock_response.raw = test_data
    mock_requests.get.return_value = mock_response
    dataset = download_data(context)
    assert len(dataset) == 77
    assert len(dataset[0].keys()) == 16


def test_cereal_data_pipeline():
    result = execute_pipeline(cereal_data_pipeline)
    assert result.success
