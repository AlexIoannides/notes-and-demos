"""Config schema defined using Pydantic."""
from typing import Literal

from pydantic import BaseModel, ValidationError

_VERSION = "0.1"

class Config(BaseModel):
    """Schema for PROJECT config values."""

    SCHEMA_VERSION: Literal[_VERSION]
    PROJECT_ID: int
    PROJECT_ENV: Literal["dev", "test", "prod"]


if __name__ == "__main__":
    config_instance = {
        "SCHEMA_VERSION": "0.1",
        "PROJECT_ID": 123,
        "PROJECT_ENV": "devv"
    }
    try:
        config = Config(**config_instance)
        print(config.model_dump_json(indent=2))
    except ValidationError as e:
        for error in e.errors():
            print(f"ERROR: {error['loc'][0]} --> {error['msg']}")
