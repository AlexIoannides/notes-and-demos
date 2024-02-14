"""Reusable pipeline components."""
from kfp import dsl


@dsl.component(base_image="python3.10", packages_to_install=["numpy==1.26.*"])
def make_data(n_rows: int, n_cols: int, data: dsl.Output) -> None:
    """Generate data using random number generation."""
    from numpy.random import default_rng

    rng = default_rng(42)
    data_arr = rng.standard_normal((n_rows, n_cols))
    data_arr.tofile(data.path)
