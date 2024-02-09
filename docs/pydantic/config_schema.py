"""Config file schema defined using Pydantic."""

from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict, FilePath, HttpUrl


class _UserCert(BaseModel):
    """Schema for User certificate config components."""

    secret_resource_name: HttpUrl
    filename: FilePath


class ConfigV1(BaseModel):
    """Schema for PROJECT config values."""

    model_config = ConfigDict(
        frozen=True, extra="allow"
    )  # make immutable and allow extra fields

    SCHEMA_VERSION: Literal["0.1"]
    PROJECT_ID: int
    PROJECT_ENV: Literal["dev", "test", "prod"]
    USER_CERT: _UserCert
    USER_TAG: Optional[str] = None
