"""Demoing how to use Pydantic to get schema-valid config from a YAML file."""

from pathlib import Path
from pprint import pprint
from typing import Any

import yaml
from pydantic import ValidationError

from config_schema import ConfigV1


def get_config(file: Path = Path.cwd() / "config.yaml") -> ConfigV1:
    """Get validated config as an instance of the data model."""
    with open(file) as f:
        raw_config: dict[str, Any] = yaml.safe_load(f)
    return ConfigV1(**raw_config)


def get_config_as_dict(file: Path = Path.cwd() / "config.yaml") -> dict[str, Any]:
    """Get config as a dictionary that has been validated against the data model."""
    with open(file) as f:
        raw_config: dict[str, Any] = yaml.safe_load(f)
    ConfigV1.model_validate(raw_config)
    return raw_config


if __name__ == "__main__":
    try:
        print("\n(1) config as ConfigV1 object:")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        config = get_config()
        pprint(config.model_dump(), indent=2)

        print("\n(2) config as dict:")
        print("~~~~~~~~~~~~~~~~~~~")
        config_dict = get_config_as_dict()
        pprint(config_dict, indent=2)

    except ValidationError as e:
        print(e)
