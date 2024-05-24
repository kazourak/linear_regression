def predict(thetas: tuple[float, float], mileage_to_predict: int = None):
    mileage = 0
    theta0, theta1 = thetas

    if mileage_to_predict is not None:
        mileage = mileage_to_predict
    else:
        _mileage = input("Please enter the mileage of the car you want to predict: ")
        while not _mileage.isdigit():
            _mileage = input("Please enter a valid mileage: ")
        mileage = int(_mileage)

    print(f"The estimated price of the car is: {theta0 + theta1 * int(mileage)}")
