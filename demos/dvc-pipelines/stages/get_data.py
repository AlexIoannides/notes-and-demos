"""
Stage that gets a dataset for training a ML model.
"""
import numpy as np
import pandas as pd

from config import DATASET_FILENAME


def run_stage() -> None:
    x = np.random.standard_normal(1000)
    y = 2.0 * x + 0.1 * np.random.standard_normal(1000)
    df = pd.DataFrame({"y": y, "x": x})
    df.to_csv(DATASET_FILENAME, index=False)


if __name__ == "__main__":
    run_stage()
