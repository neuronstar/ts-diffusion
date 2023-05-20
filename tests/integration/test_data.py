from ts_diffusion.data import collate_convert_tensor, DataFrameDataset
import pandas as pd
import pickle
import pytest
from torch.testing import assert_allclose


@pytest.fixture
def input_length():
    return 3


@pytest.fixture
def horizon():
    return 2


def test_dataframe_dataset(ecb_path, input_length, horizon, expected_folder_path):

    is_regenerate_artefact = False

    expected_data_path = expected_folder_path / "ecb_dataframe_dataset.pickle"

    df = pd.read_csv(ecb_path).drop("Date", axis=1)
    ds = DataFrameDataset(dataframe=df, input_length=input_length, horizon=horizon)

    if is_regenerate_artefact:
        with open(expected_data_path, "wb+") as fp:
            pickle.dump(ds, fp)
        raise Exception(f"regeneration set to True, please set it to False")

    with open(expected_data_path, "rb") as fp:
        ds_expected = pickle.load(fp)

    for de, d in zip(list(ds_expected), list(ds)):
        for de_, d_ in zip(de, d):
            assert_allclose(de_, d_)
