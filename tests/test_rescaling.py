import pandas as pd
import pytest
from ft_linear_regression import rescaling


def test_rescaling():

    # Create a pandas Series
    data = {'km': [2, 4, 4, 4, 5, 5, 7, 9], 'price': [200, 400, 400, 400, 500, 500, 700, 900]}
    df = pd.DataFrame(data)

    # Create the expected result
    expected = {'km': [0.000000, 0.333333, 0.333333, 0.333333, 0.500000, 0.500000, 0.833333, 1.000000], 'price': [0.000000, 0.333333, 0.333333, 0.333333, 0.500000, 0.500000, 0.833333, 1.000000]}
    expected_df = pd.DataFrame(expected)

    # Apply the function
    df_normalized = rescaling.zscore_normalization(df)

    # Compare the result
    assert df_normalized.equals(expected_df)


if __name__ == "__main__":
    pytest.main()
