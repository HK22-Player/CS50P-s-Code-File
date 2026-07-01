import pytest
import pandas as pd
from Project import data_validation, statistic_descriptive, linear_regression

@pytest.fixture
def data():
    return pd.DataFrame({
        "X": [1.0, 2.0, 3.0, 4.0, 5.0],
        "Y": [10.0, 20.0, 30.0, 40.0, 50.0]
    })

def test_data_validation_and_invalidation():
    data1 = pd.DataFrame({
        "X": [1.0, 2.0],
        "Y": [10.0,20.0]
        })
    with pytest.raises(ValueError):
        data_validation(data1)

    No_data = pd.DataFrame({
        "X": [1, None, 3],
        'Y': [10, 20, 30]
    })
    with pytest.raises(ValueError):
        data_validation(No_data)

    object_data = pd.DataFrame({
        "X": [1.0,2.0,3.0],
        "Y": ['ten','twenty','thirty']
    })
    with pytest.raises(ValueError):
        data_validation(object_data)

    perfect_data = pd.DataFrame({
        "X": [1.0, 2.0, 3.0],
        "Y": [10.0, 20.0, 30.0]
    })
    result = data_validation(perfect_data)
    assert result is not None
    assert len(result) == 3

def test_statistic_descriptive(data):
    mean_x, median_x, std_x = statistic_descriptive(data, "X")
    assert mean_x == 3.0
    assert median_x == 3.0
    assert std_x > 0

    mean_y, median_y, std_y = statistic_descriptive(data, "Y")
    assert mean_y == 30.0
    assert median_y == 30.0
    assert std_y > 0

    with pytest.raises(ValueError):
        statistic_descriptive(data, "FalseColumn")

def test_linear_regression(data):
    result = linear_regression(data, "X", "Y")
    assert result["slope"] == 10.0
    assert result["intercept"] == 0.0
    assert result["r_squared"] == 1.0
