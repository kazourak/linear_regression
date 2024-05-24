import ft_linear_regression as ft
import joblib
import pandas as pd


def evaluate_program():
    # Load the data
    data = pd.read_csv("data/raw/data.csv", dtype=float, usecols=["km", "price"])

    # Load theta values
    thetas = ft.get_thetas()

    # Predict all values
    data['predict'] = data['km'].apply(lambda x: ft.predict(thetas, x))

    print("Root mean squared error:", ft.rmse(data))
    print("Mean absolute error:", ft.mae(data))
    print("R2 score:", ft.determine_r2(data))


if __name__ == "__main__":
    evaluate_program()
