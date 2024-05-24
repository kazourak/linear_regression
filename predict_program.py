import ft_linear_regression as ft
import argparse


def parse_args() -> argparse.ArgumentParser:
    """
    Parse the arguments for the program with argparse
    :return:
    """
    parser = argparse.ArgumentParser(prog="predict_program.py", description="Linear regression program - Predict part", epilog="42 AI project")
    parser.add_argument("--theta", nargs=2, type=float, help="Thetas to use for prediction")
    parser.add_argument("--mileage", nargs=1, type=int, help="Mileage of the car to predict")
    parser.add_argument("--save", action="store_true", help="Save thetas")
    return parser


def get_thetas(args: argparse.Namespace) -> tuple[float, float]:
    """
    Get the thetas to use for prediction.
    If thetas are provided as arguments, return them.
    Otherwise, get the thetas from the file.

    :param args:
    :return:
    """
    if args.theta is not None:
        return args.theta[0], args.theta[1]
    return ft.get_thetas()


def main():
    # Get and parse the arguments
    parser = parse_args()
    args = parser.parse_args()

    # Get the thetas. If thetas are provided as arguments, use them. Otherwise, get the thetas from the file
    thetas = get_thetas(args)

    # Save the thetas if the save argument is provided
    if args.save is not None and args.theta is not None:
        ft.set_thetas(args.theta[0], args.theta[1])

    # Use the mileage provided as argument if it is provided
    mileage = args.mileage[0] if args.mileage is not None else None

    prediction = ft.predict(thetas, mileage)
    print(f"The predicted price is {prediction}")


if __name__ == "__main__":
    main()
