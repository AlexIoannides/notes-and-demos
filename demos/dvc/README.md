# Managing ML Artefacts with DVC

Data Version Control (DVC) is a command line tool that enables version control for ML artefacts (e.g., models and training datasets), using a Git repository and a filesystem (e.g., cloud object storage).

This demo is based around version control for a dataset, but it would work in exactly the same way for any ML model serialised to a file.

## Demo Objectives

* How to initialise version control for a dataset stored on AWS S3.
* How to update a dataset.
* How to fetch any versions of dataset.

## Running the Demo

This demo is contained within a single Jupyter notebook - `demos/dvc/data_and_model_versioning.ipynb`. Make sure you have the necessary Python package requirements installed into a Jupyter kernel for it to run successfully.
