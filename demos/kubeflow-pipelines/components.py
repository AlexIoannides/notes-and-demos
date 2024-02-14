"""Patterrns for developing reusable KFP pipeline components."""
import shutil
from pathlib import Path
from unittest.mock import Mock

import numpy as  np
from kfp import dsl, local

_BASE_IMAGE = "python3.10"
_REQUIREMENTS = Path("requirements.txt").read_text().splitlines()


@dsl.component(base_image=_BASE_IMAGE, packages_to_install=_REQUIREMENTS)
def make_data(n_rows: int, n_cols: int, data: dsl.Output[dsl.Dataset]) -> None:
    """Synthetic dataset generation pipeline component. """
    from numpy import save
    from numpy.random import default_rng

    rng = default_rng(42)
    data_arr = rng.standard_normal((n_rows, n_cols))
    save(data.path, data_arr)


def test_make_data_component():
    output_dataset_file = "foo.npy"
    mock_dataset = Mock()
    mock_dataset.path = output_dataset_file
    try:
        make_data.execute(n_rows=3, n_cols=2, data=mock_dataset)
        output_dataset = np.load(output_dataset_file)
        assert output_dataset.shape == (3, 2)
    except Exception:
        assert False
    finally:
        data_filepath = Path(output_dataset_file)
        if data_filepath.exists():
            data_filepath.unlink()


def test_make_data_component_integration():
    kfp_root_dir = "./kfp_outputs"
    local.init(runner=local.SubprocessRunner(use_venv=True), pipeline_root=kfp_root_dir)
    try:
        task = make_data(n_rows=3, n_cols=2)
        output_dataset = np.load(f"{task.outputs['data'].path}.npy")
        assert output_dataset.shape == (3, 2)
    except Exception:
        assert False
    finally:
        shutil.rmtree(kfp_root_dir, ignore_errors=True)
    