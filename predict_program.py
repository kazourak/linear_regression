import ft_linear_regression as ft
import argparse


def parse_args() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="predict_program.py", description="Linear regression program - Predict part", epilog="42 AI project")
    parser.add_argument("--theta", nargs=2, type=float, help="Thetas to use for prediction")
    parser.add_argument("--mileage", nargs=1, type=int, help="Mileage of the car to predict")
    parser.add_argument("--save", action="store_true", help="Save thetas")
    return parser


def get_thetas(args: argparse.Namespace) -> tuple[float, float]:
    if args.theta is not None:
        return args.theta[0], args.theta[1]
    return ft.get_thetas()


def main():
    parser = parse_args()
    args = parser.parse_args()
    thetas = get_thetas(args)

    if args.save is not None and args.theta is not None:
        ft.set_thetas(args.theta[0], args.theta[1])

    mileage = args.mileage[0] if args.mileage is not None else None
    ft.predict(thetas, mileage)


if __name__ == "__main__":
    main()
