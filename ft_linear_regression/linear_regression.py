import pandas as pd
from .rescaling import minmax_normalization


def linear_regression(data_path: str):
    """
    Perform linear regression on the data

    The CSV file must contain two columns named ``'km'`` and ``'price'``
    Parameters
    ----------
    data_path : str
        The path to the data
    """
    # Load the data
    data = pd.read_csv(data_path, dtype=float, usecols=["km", "price"])

    # Normalize the data
    data_normalized = minmax_normalization(data)
    print(data_normalized)
