import pandas as pd


def zscore_normalization(data: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize the data using z-score normalization
    ref: https://en.wikipedia.org/wiki/Standard_score
    Parameters
    ----------
    data : DataFrame
        The data to normalize

    Returns
    -------
    DataFrame
        The normalized data
    """
    normalized_data = data.copy()

    # Check if header contains two column and 'km' and 'price'
    if len(normalized_data.columns) != 2 or 'km' not in normalized_data.columns or 'price' not in normalized_data.columns:
        raise ValueError("The data must contain two columns named 'km' and 'price'")

    # Apply z-score normalization
    normalized_data = normalized_data.apply(lambda x: (x - x.mean()) / x.std())

    return normalized_data
