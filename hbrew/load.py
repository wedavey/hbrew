# encoding: utf-8
"""
load
~~~~~~~~~~~~~~~

<Description goes here...>

"""
__author__ = "Will Davey"
__email__ = "wedavey@gmail.com"
__created__ = "2020-10-14"
__copyright__ = "Copyright 2020 Will Davey"
__license__ = "MIT https://opensource.org/licenses/MIT"

import pandas as pd
import os
from collections import namedtuple
from hbrew import DATADIR

# globals
BATCH_METADATA_PATH = os.path.join(DATADIR,"batch_metadata.csv")


class BatchProbeData(object):
    """ Load and process batch probe data

    :param data_path: path of the batch probe csv data
    :param tmax: maximum allowed batch time in hours (clipped above this)
    """
    def __init__(self, data_path=None, tmax=None):
        self.data_path = data_path
        self.tmax = tmax

    def raw_df(self):
        """ Return the raw data as pandas DataFrame"""
        return pd.read_csv(self.data_path, parse_dates=["time"])

    def clean_df(self):
        """Return the cleansed data as pandas DataFrame

        TODO: fill out the description.
        """
        # load raw data and standardise column names
        df = self.raw_df()
        df = df.rename(columns = {
            "tilt.Temperature": "temp",
            "tilt.Specific-Gravity": "grav",
        })

        # calculate time in hours
        start_time = df['time'][0]
        current_time = df['time'].iloc[-1]
        time_delta = df['time'] - start_time
        time_hours = time_delta.dt.total_seconds() / 60 / 60
        df["time"] = time_hours

        # filter on tmax
        if self.tmax is not None:
            df = df[df["time"] < self.tmax]

        return df[["time", "temp", "grav"]]


class BatchMgr(object):
    """Access to batch probe and metadata"""
    def __init__(self,
                 metadata_path = BATCH_METADATA_PATH,
                 probe_data_dir = DATADIR,
                 ):
        self.metadata_path = metadata_path
        self.probe_data_dir = probe_data_dir

        # load all batch metadata
        self.metadata = load_batch_metadata(metadata_path)
        # named tuple for holding individual batch metadata
        self.BatchMetadata = namedtuple('BatchMetadata', self.metadata.dtypes.index.tolist())

    def get_batch_metadata(self, batch_code):
        """Return metadata for batch with code *batch_code*"""
        # get batch row from meatadata
        data = self.metadata.loc[batch_code]
        # replace NaN with None
        data = data.where(pd.notnull(data), None)
        # convert into named tuple
        return self.BatchMetadata(*data)

    def get_batch_probe_data(self, batch_code):
        """Return probe data for batch with code *batch_code*"""
        batch_metadata = self.get_batch_metadata(batch_code)
        tmax = batch_metadata.tmax
        path = os.path.join(self.probe_data_dir, "{}.csv".format(batch_code))
        return BatchProbeData(path, tmax)


def load_batch_metadata(data_path = BATCH_METADATA_PATH):
    """Return batch metadata as pandas DataFrame"""
    return pd.read_csv(data_path).set_index("code")


# EOF