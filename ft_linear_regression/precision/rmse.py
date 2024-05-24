import pandas as pd


def rmse(data: pd.DataFrame):
    """
    Calculate the root mean squared error.
    :param data:
    :return:
    """
    return ((data['price'] - data['predict']) ** 2).mean() ** 0.5
