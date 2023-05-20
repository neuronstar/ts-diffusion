from pathlib import Path
import pytest


@pytest.fixture
def data_folder_path():
    location = Path(__file__).parent.resolve()
    return location / "data"


@pytest.fixture
def expected_folder_path():
    location = Path(__file__).parent.resolve()
    return location / "expected"


@pytest.fixture
def ecb_path(data_folder_path):
    return data_folder_path / "ecb_exchange_rate.csv"
