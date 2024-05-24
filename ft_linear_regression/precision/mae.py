import pandas as pd


def mae(data: pd.DataFrame):
    """
    Calculate the mean absolute error.
    :param data:
    :return:
    """
    return (data['price'] - data['predict']).abs().mean()
