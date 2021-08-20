import pandas as pd
from PyQt5.QtWidgets import QFileDialog

from sdx.data import data_handlers


class FileOpenError(Exception):
    pass


def open_file_dialog():
    filename, _ = QFileDialog().getOpenFileName(filter="*.csv")

    if filename in data_handlers.data_store:
        raise FileOpenError("File is already open")

    return filename


def close_file(filename, data_explorer):
    data_handlers.remove_dataset(filename)
    data_explorer.remove_file_item(filename)

    return