# Pipeline Orchestration with Dagster

Data engineering and ML often require some level of pipeline orchestration - e.g., for ETL or training models. [Dagster](https://www.dagster.io) is an alternative to orchestration tools such as Airflow.

## Demo Objectives

We aim to demonstrate how to:

* Define a pipeline with multiple stages.
* Test pipelines and stages.
* Add pipelines to a Dagster repository.
* Configure pipelines within a Dagster workspace.

## Running the Demo

If you run

```text
$ dagit
...
```

The pipelines configured in `workspace.yaml` will be available to run in the UI at `http://localhost:3000`. Alternatively, individual pipelines can be run directly from the command line - e.g.,

```text
$ python demos/dagster/pipelines/example_pipeline.py
...
```

Alternatively, they can be executed via the Dagster CLI

```text
$ dagster pipeline execute -f demos/dagster/pipelines/example_pipeline.py
...
```

Refer to the [Dagster docs](https://docs.dagster.io/getting-started) for more information - e.g. how to define schedules or triggers, etc.

### Running Tests

Example tests (using PyTest) can be found in the `demos/dagster/tests` folder and can be executed by running

```text
$ pytest
...
```
