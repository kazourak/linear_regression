import joblib


DATA_PATH = "../../data/processed/thetas.pkl"


def get_thetas() -> tuple[float, float]:
    """
    Load thetas from a binary file and return them
    :return tuple[float, float]:
    """
    try:
        coef_ = joblib.load(DATA_PATH)
        return coef_[0], coef_[1]
    except FileNotFoundError:
        print("No thetas found, please train with 'make train' first.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return 0, 0


def set_thetas(theta0: float, theta1: float):
    """
    Save thetas to a binary file
    :param theta0:
    :param theta1:
    """
    try:
        joblib.dump((theta0, theta1), DATA_PATH)
    except Exception as e:
        print(f"An error occurred: {e}")
