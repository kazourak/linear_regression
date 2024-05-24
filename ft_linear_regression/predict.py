def predict(thetas: tuple[float, float], mileage_to_predict: int = None) -> float:
    """
    Predict the price of a car given its mileage.
    If no mileage is provided, ask the user for it.

    Formula used to predict: ``y=theta0+theta1*mileage``
    :param thetas:
    :param mileage_to_predict:
    :return prediction:
    """
    theta0, theta1 = thetas

    # If mileage is provided as an argument, use it. Otherwise, ask the user for it.
    if mileage_to_predict is not None:
        mileage = mileage_to_predict
    else:
        _mileage = input("Please enter the mileage of the car you want to predict: ")
        while not _mileage.isdigit():
            _mileage = input("Please enter a valid mileage: ")
        mileage = int(_mileage)

    return theta0 + theta1 * mileage
