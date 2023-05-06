from ts_diffusion.data import DataFrameDataset
import pytest
from torch.utils.data import DataLoader
from ts_diffusion.data import collate_convert_tensor


@pytest.fixture
def dataframe_dataset(dataframe, input_length, horizon):
    return DataFrameDataset(
        dataframe=dataframe, input_length=input_length, horizon=horizon
    )


def test_dataframe_dataset_length(dataframe_dataset):

    assert len(dataframe_dataset) == 6  # 10 - 3 - 2 + 1


def test_pandasdataframe_dataloader(dataframe_dataset):

    dl = DataLoader(
        dataset=dataframe_dataset, batch_size=2, collate_fn=collate_convert_tensor
    )

    assert len(dl) == 3  # len(dataframe_dataset) / 2 = 6 /2 = 3
