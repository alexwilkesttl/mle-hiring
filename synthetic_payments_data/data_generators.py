import numpy as np
import pandas as pd


def payment_currency_code(n):
    return np.random.choice(
        ["EUR", "GBP", "USD", "DKR", "AUD"],
        n
    )


def payment_attempt_dt(n):
    diffs = np.random.normal(0, 20, n)
    centre_date = pd.Timestamp.now() - pd.Timedelta(days=90)

    return np.array(
        [
            pd.Timedelta(days=diff) + centre_date
            for diff in diffs
        ]
    )


def payment_provider(n):
    return np.random.choice(
        ["provider1", "provider2"],
        n
    )


def payment_method(n):
    return np.random.choice(
        ["Card", "ApplePay"],
        n
    )


def card_used_before(n):
    return np.random.choice(
        [1.0, np.nan],
        n
    )


def card_expiry_year(n):
    current_year = pd.Timestamp.now().year

    return np.random.choice(
        [current_year, current_year + 1, current_year + 2, current_year + 3],
        n,
        p=[0.1, 0.2, 0.4, 0.3]
    )


def card_expiry_month(n):
    current_year = pd.Timestamp.now().year

    return np.random.choice(np.arange(1, 13), n)


def generate_features(n):
    return pd.DataFrame(
        {
            "payment_currency_code": payment_currency_code(n),
            "payment_attempt_dt": payment_attempt_dt(n),
            "payment_provider": payment_provider(n),
            "payment_method": payment_method(n),
            "card_used_before": card_used_before(n),
            "card_expiry_year": card_expiry_year(n),
            "card_expiry_month": card_expiry_month(n),
        }
    )