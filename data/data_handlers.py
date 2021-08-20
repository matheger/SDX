from collections import defaultdict

from PyQt5 import QtWidgets

import pandas as pd

import seaborn as sns


data_store = {}
active_data = defaultdict(list)


class InconsistentLengthError(Exception):
    pass


def get_dataset(filename):
    """Return full dataset for given filename
    :param filename: str
    :return dataset: pandas.DataFrame
    """
    data = data_store[filename]

    return data


def get_dataset_len(filename):
    return len(data_store[filename])


def update_active_datasets(selection):
    global active_data
    active_data = selection

    _mw = QtWidgets.QApplication.instance().main_window

    # update hue selector in PlotSettings dock
    _mw.PlotSettingsDock.DynamicPlotSettingsWidget.refresh_hue_selector()

    # if auto updating is enabled, kick off the plotting call now (using the MainWindow method);
    # if update fails due to inconsistent dataset lengths, mimic the error in the MainWindow method
    if _mw.PlotSettingsDock.get_auto_update_setting():
        _mw.update_plot()

    return


def get_active_data():
    data = pd.DataFrame()
    first_col = True

    for filename, cols in active_data.items():
        # add columns one by one, adjusting their names with trailing "~" to make their names unique
        for col in cols:
            col_new = col
            while col in data.columns:
                col_new += "~"

            # check that new columns have the same length as previous ones (unless we're just adding the first one)
            if len(data) != len(data_store[filename]) and not first_col:
                raise InconsistentLengthError("Tried to merge datasets with different lengths")

            data[col_new] = data_store[filename][col]
            first_col = False

    return data


def read_csv_data(filename):
    data = pd.read_csv(filename)
    data_store[filename] = data

    return


def remove_dataset(filename):
    del data_store[filename]

    return


def create_seaborn_plot(data, hue):
    return sns.pairplot(data, hue=hue)
