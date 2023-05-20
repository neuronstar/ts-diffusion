from torch.utils.data import DataLoader, Dataset
from typing import Optional

import pandas as pd
import torch
from loguru import logger


class DataFrameDataset(Dataset):
    """A dataset from a pandas dataframe

    :param dataframe: input dataframe with a DatetimeIndex.
    :param input_length: length of input in time dimension
    :param horizon: future length to be forecasted
    """

    def __init__(self, dataframe: pd.DataFrame, input_length: int, horizon: int):
        super().__init__()
        self.dataframe = dataframe
        self.input_length = input_length
        self.horizon = horizon
        self.dataframe_rows = len(self.dataframe)
        self.length = self.dataframe_rows - self.input_length - self.horizon + 1

    def moving_slicing(self, idx):

        x, y = (
            self.dataframe[idx : self.input_length + idx].values,
            self.dataframe[
                self.input_length + idx : self.input_length + self.horizon + idx
            ].values,
        )
        return x, y

    def _validate_dataframe(self):
        """Validate the input dataframe.
        - We require the dataframe index to be DatetimeIndex.
        - This dataset is null aversion.
        - Dataframe index should be sorted.
        """

        if not isinstance(
            self.dataframe.index, pd.core.indexes.datetimes.DatetimeIndex
        ):
            raise TypeError(
                f"Type of the dataframe index is not DatetimeIndex: {type(self.dataframe.index)}"
            )

        has_na = self.dataframe.isnull().values.any()

        if has_na:
            logger.warning(f"Dataframe has null")

        has_index_sorted = self.dataframe.index.equals(
            self.dataframe.index.sort_values()
        )

        if not has_index_sorted:
            logger.warning(f"Dataframe index is not sorted")

    def __getitem__(self, idx):
        if idx >= self.length:
            raise IndexError("End of dataset")
        return self.moving_slicing(idx)

    def __len__(self):
        return self.length


def collate_convert_tensor(batch):
    """batch first convention"""

    x = torch.tensor([b[0] for b in batch])
    y = torch.tensor([b[-1] for b in batch])

    return x, y
