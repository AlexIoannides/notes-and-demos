## Machine Learning Lifecycle Management using MLflow

The machine learning lifecycle covers the following stages of a machine learning engineering project:

* data preparation
* training
* deployment

[MLflow](https://mlflow.org) is an open-source framework that helps to track training metrics, manage models and assist with model deployment. This the `mlflow_basics.ipynb` notebook in this repository demonstrates how to setup MLflow and use to manage the lifecycle of a simple classification model.

## Dependencies

All 3rd party Python packages required to run the notebook are contained in the `requirements.txt` file. We recommend that they are installed into a new virtual environment - e.g. with the following sequence of commands executed from your terminal,

```shell
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ jupyter lab
```
