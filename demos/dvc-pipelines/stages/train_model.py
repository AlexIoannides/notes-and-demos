"""
Train regression model on dataset
"""
import joblib
import json
import pandas as pd
import yaml
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

from config import DATASET_FILENAME, METRICS_FILENAME, MODEL_FILENAME


def run_stage() -> None:
    params = yaml.safe_load(open("params.yaml"))["train"]
    data = pd.read_csv(DATASET_FILENAME)
    X_train, X_test, y_train, y_test = train_test_split(
        data[["x"]], data["y"], random_state=params["random_state"]
    )
    model = LinearRegression()
    model.fit(X_train, y_train)
    joblib.dump(model, MODEL_FILENAME)

    y_test_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_test_pred)
    with open(METRICS_FILENAME, "w") as metrics_file:
        json.dump({"MAE": mae}, metrics_file, indent=4)


if __name__ == "__main__":
    run_stage()
