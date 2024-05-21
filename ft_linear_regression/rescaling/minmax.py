import pandas as pd


def rescaling(series):
    """
    Rescale the series using min-max normalization

    Notes
    -----
    formula : ``(x-min(x))/(max(x)-min(x))``
    """
    return (series - series.min()) / (series.max() - series.min())


def minmax_normalization(data: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize the data using min-max normalization

    Notes
    --------
    min-max normalization : source https://en.wikipedia.org/wiki/Feature_scaling#Rescaling_(min-max_normalization)

    Parameters
    ----------
    data : DataFrame
        The data to normalize
    """
    data_normalized = data.copy()

    # Check if header contains two column and 'km' and 'price'
    if len(data_normalized.columns) != 2 or 'km' not in data_normalized.columns or 'price' not in data_normalized.columns:
        raise ValueError("The data must contain two columns named 'km' and 'price'")

    data_normalized = data_normalized.apply(rescaling)
    return data_normalized
