## Object Relation Mapping using SQL Alchemy and Alembic

[SQL Alchemy](https://docs.sqlalchemy.org/en/14/index.html) is a common approach to working with data models (in a database) using Python objects - i.e. [Object-Relational Mapping](https://en.wikipedia.org/wiki/Object–relational_mapping). [Alembic](https://alembic.sqlalchemy.org/en/latest/) is a Python package for managing database migrations based on the data models implied by the SQL Alchemy models - i.e. Python classes.

## Dependencies

All 3rd party Python packages required to run the notebook are contained in the `requirements.txt` file. We recommend that they are installed into a new virtual environment - e.g. with the following sequence of commands executed from your terminal,

```shell
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ jupyter lab
```
