import pandas as pd
import sys
from .predict import predict
from .data import set_thetas
import matplotlib.pyplot as plt


def plot_data(data: pd.DataFrame, theta: tuple[float, float]):
    """
    Plot the data and the linear regression line.
    :param data:
    :param theta:
    :return:
    """
    plt.plot(data['km'], data['price'], 'ro')
    plt.plot(data['km'], theta[0] + theta[1] * data['km'], 'b')
    plt.xlabel('km')
    plt.ylabel('price')
    plt.title('Linear regression')
    plt.show()


def gradient_descent(data: pd.DataFrame, theta: list, learning_rate: float):
    """
    Perform gradient descent on the data.
    :param data:
    :param theta:
    :param learning_rate:
    """
    m = len(data)
    thetas = (theta[0], theta[1])

    # Update theta
    theta0 = (learning_rate * (1 / m) * sum([predict(thetas, data['km'][i]) - data['price'][i] for i in range(m)]))
    theta1 = (learning_rate * (1 / m) * sum([(predict(thetas, data['km'][i]) - data['price'][i]) * data['km'][i] for i in range(m)]))
    return theta0, theta1


def linear_regression(data: pd.DataFrame, data_normalized: pd.DataFrame):
    """
    Perform linear regression on the data.

    Parameters
    ----------
    data : DataFrame
        The original data
    data_normalized : DataFrame
        The normalized data
    """
    theta = [0, 0]

    # Perform gradient descent 10,000 times
    for _ in range(10000):
        thetas_tmp = gradient_descent(data_normalized, theta, learning_rate=0.1)

        # Update theta values
        theta[0] = theta[0] - thetas_tmp[0]
        theta[1] = theta[1] - thetas_tmp[1]

    # Unnormalize the thetas
    t1 = theta[1] * (data['price'].std() / data['km'].std())
    t0 = data['price'].mean() + data['price'].std() * (theta[0] - (theta[1] * (data['km'].mean() / data['km'].std())))

    # Plot the data and the linear regression line
    if len(sys.argv) == 2 and sys.argv[1] == "--plot":
        plot_data(data, (t0, t1))

    print(f"theta0: {t0}, theta1: {t1}")
    set_thetas(t0, t1)
