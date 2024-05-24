import pandas as pd


def determine_r2(data: pd.DataFrame) -> float:
    """
    Calculate the R2 value.
    :param data:
    :return:
    """
    return 1 - ((data['price'] - data['predict']) ** 2).sum() / ((data['price'] - data['price'].mean()) ** 2).sum()
