import pytest
import pandas as pd


@pytest.fixture
def dataframe_length():
    return 10


@pytest.fixture
def input_length():
    return 3


@pytest.fixture
def horizon():
    return 2


def test_a(input_length):
    pass


@pytest.fixture
def dataframe(dataframe_length):

    return pd.DataFrame(
        {
            "date": [
                d.toordinal()
                for d in pd.date_range("2021-01-01", periods=dataframe_length)
            ],
            "target": list(range(dataframe_length)),
        }
    )
