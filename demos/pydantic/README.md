# Runtime Type Validation with Pydantic

[Pydantic](https://docs.pydantic.dev/latest/) is a framework for executing runtime type validation - e.g., for validating data sent to an API against a pre-defined data model.

This demo shows how Pydantic can be used to validate a config file (written in YAML), against a pre-defined schema.

## Demo Objectives

* Define a data model.
* Use the data model to validate config loaded from a YAML file.
* Show the difference between validating data in a `dict` and as part of data model instatiation.
* Demonstrate how validation errors can be handled and reported to Users.

## Running the Demo

This demo is contained in a single Python module, `load_config.py`, that can be run using,

```text
$ python -m load_config
```
