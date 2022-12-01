# Repositories & Workspaces

Dagster repositories and workspaces provide a mechanism for managing pipelines easier when operating at scale - e.g., across multiple teams within an organisation all sharing the same Dagster cluster.

Repositories can be defined in code as follows:

```python title="demos/dagster/repository.py"
--8<-- "demos/dagster/repository.py"
```

And workspaces are configured via:

```yanl title="demos/dagster/workspace.yaml"
--8<-- "demos/dagster/workspace.yaml"
```

At a basic level the above example shows how to associate an execution environment (i.e., a Python virtual environment), with a given team's pipeline repository. This enables teams to specify their own Python requirements - e.g., a ML engineering team may want to use a newer version of NumPy than that used by an adjacent data engineering team.
