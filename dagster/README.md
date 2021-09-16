# Python Job Orchestration with Dagster

Data engineering and machine learning often require some level of pipeline orchestration - e.g. for ETL or training models. [Dagster](https://www.dagster.io) is an alternative to orchestration tools such as Airflow.

This toy project defines a pipeline in the `pipelines/*` folder, which is added to the repository in `repository.py`, that is part of the workspace configured in `workspace.yaml`. If you run,

```
$ dagit
```

The pipelines configured in `workspace.yaml` will be available to run in the UI at `http://localhost:3000`. Alternatively, individual pipelines can be run directly from the command line - for example,

```
$ python pipelines/example_pipeline.py
```

Or,

```
$ dagster pipeline execute -f pipelines/example_pipeline.py
```

Refer to the [Dagster docs](https://docs.dagster.io/getting-started) for more information - e.g. how to define schedules or triggers, etc.

## Tests

Example tests (using PyTest) for both Dagster solids and pipelines, can be found in the `tests/*` folder. To run them, use,

```
pytest
```

## Dependencies

All 3rd party Python packages required to run the notebook are contained in the `requirements.txt` file. We recommend that they are installed into a new virtual environment - e.g. with the following sequence of commands executed from your terminal,

```shell
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ jupyter lab
```
