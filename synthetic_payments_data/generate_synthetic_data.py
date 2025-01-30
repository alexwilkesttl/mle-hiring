import numpy as np
import pandas as pd
from pandas import DataFrame

from synthetic_payments_data.data_generators import generate_features


def generate_score(row: pd.Series) -> float:
    score = 0

    if row['payment_provider'] == "provider2":
        score += 1

    if row['payment_currency_code'] == "GBP" and \
            row['payment_provider'] == "provider2":
        score += 1

    if row['payment_method'] == "ApplePay":
        score += 1

    # Add Noise
    score += np.random.normal(0, 1)

    return score


def add_target_col(df: DataFrame) -> DataFrame:
    scores = df.apply(generate_score, axis=1)
    threshold = scores.quantile(0.05)
    df["payment_accepted"] = scores > threshold

    return df


def summarise_data(df: DataFrame) -> DataFrame:
    print("Overall distribution")
    print("-" * 30)
    print(df.payment_accepted.value_counts())
    print("\n")

    for col in df:
        if col != "payment_accepted":
            print(f"Grouped by {col}")
            print("-" * 30)
            print(df.groupby(col)["payment_accepted"].mean())
            print("\n")


if __name__ == "__main__":
    df = generate_features(5000)
    df = add_target_col(df)
    summarise_data(df)
