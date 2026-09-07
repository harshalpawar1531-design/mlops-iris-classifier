import argparse
import logging
import sys

import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

logger = logging.getLogger("validate")

EXPECTED_COLUMNS = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)",
    "species",
    "sepal_area",
    "petal_area",
    "sepal_to_petal_length_ratio",
    "petal_length_bin",
]

VALID_SPECIES = {"setosa", "versicolor", "virginica"}


def validate(path: str) -> None:
    df = pd.read_csv(path)

    # Check columns
    if list(df.columns) != EXPECTED_COLUMNS:
        raise ValueError(
            f"Unexpected columns: {list(df.columns)}"
        )

    # Check null values
    if df.isna().any().any():
        raise ValueError("Null values detected")

    # Check species
    if not set(df["species"]).issubset(VALID_SPECIES):
        raise ValueError("Invalid species value detected")

    # Check numeric ranges
    for col in [
        "sepal length (cm)",
        "sepal width (cm)",
        "petal length (cm)",
        "petal width (cm)",
    ]:
        if not df[col].between(0, 10).all():
            raise ValueError(
                f"Values out of range in {col}"
            )

    logger.info(
        "Validation PASSED: %d rows, %d columns, all checks satisfied",
        len(df),
        len(df.columns)
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--input",
        default="data/processed/iris_features.csv"
    )

    args = parser.parse_args()

    try:
        validate(args.input)
    except Exception as exc:
        logger.error("Validation FAILED: %s", exc)
        sys.exit(1)