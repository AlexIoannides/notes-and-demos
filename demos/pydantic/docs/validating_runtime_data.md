# Validating Runtime Data

The data model can be imported and used to validate config loaded from YAML files. Two different approaches to runtime validation are demonstrated:

```python title="demos/pydantic/load_config.py"
--8<-- "demos/pydantic/load_config.py"
```

Given a config file,

```yaml title="demos/pydantic/config.yaml"
--8<-- "demos/pydantic/config.yaml"
```

The output from `load_config.py` is,

```text
(1) config as ConfigV1 object:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{ 'PROJECT_ENV': 'prod',
  'PROJECT_ID': 5349,
  'PROJECT_URL': 'http://foo.com/bar.html',
  'SCHEMA_VERSION': '0.1',
  'USERNAME': {'env_var': 'foo-bar-1'},
  'USER_CERT': { 'filename': PosixPath('README.md'),
                 'secret_resource_name': Url('http://foo.com/secrets/')},
  'USER_TAG': None}

(2) config as dict:
~~~~~~~~~~~~~~~~~~~
{ 'PROJECT_ENV': 'prod',
  'PROJECT_ID': 5349,
  'PROJECT_URL': 'http://foo.com/bar.html',
  'SCHEMA_VERSION': '0.1',
  'USERNAME': {'env_var': 'foo-bar-1'},
  'USER_CERT': { 'filename': 'README.md',
                 'secret_resource_name': 'http://foo.com/secrets/'}}
```

Note how config not defined in the schema has been allowed to pass through when valudating the config data held in a dictionary. When instantiating the data model it is silently ignored.

If we manually invalidate a couple of the config values then we can also take a look at how errors are formatted:

```text
(1) config as ConfigV1 object:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
2 validation errors for ConfigV1
PROJECT_ENV
  Input should be 'dev', 'test' or 'prod' [type=literal_error, input_value='run', input_type=str]
    For further information visit https://errors.pydantic.dev/2.6/v/literal_error
USER_CERT.filename
  Path does not point to a file [type=path_not_file, input_value='README.mdz', input_type=str]
```
