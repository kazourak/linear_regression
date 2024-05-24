import ft_linear_regression as ft
import pandas as pd


def main():

    # Load the data
    data = pd.read_csv("data/raw/data.csv", dtype=float, usecols=["km", "price"])

    # Normalize the data
    data_normalized = ft.zscore_normalization(data)

    ft.linear_regression(data, data_normalized)


if __name__ == "__main__":
    main()
