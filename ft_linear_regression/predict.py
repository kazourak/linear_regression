def predict():
    mileage = ''

    while not mileage.isdigit():
        mileage = input("Enter the mileage of the car: ")
        if not mileage.isdigit():
            print("Please enter a valid number.")
