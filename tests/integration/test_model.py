from ts_diffusion.model import Sample
from ts_diffusion.data import DataFrameDataset, collate_convert_tensor
from torch.utils.data import DataLoader
import pandas as pd

import pytest


@pytest.fixture
def input_length():
    return 3


@pytest.fixture
def horizon():
    return 2


def test_sample(ecb_path, horizon, input_length):

    df = pd.read_csv(ecb_path).drop("Date", axis=1)
    ds = DataFrameDataset(dataframe=df, input_length=input_length, horizon=horizon)

    dl = DataLoader(dataset=ds, batch_size=2, collate_fn=collate_convert_tensor)

    s = Sample()
    for b in dl:
        s(b)
