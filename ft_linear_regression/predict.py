from .data import get_thetas


def predict(thetas: tuple[float, float]):
    mileage = ''
    theta0, theta1 = thetas

    while not mileage.isdigit():
        mileage = input("Enter the mileage of the car: ")
        if not mileage.isdigit():
            print("Please enter a valid number.")

    print(f"The estimated price of the car is: {theta0 + theta1 * int(mileage)}")
