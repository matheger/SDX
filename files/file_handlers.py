import pandas as pd
from PyQt5.QtWidgets import QFileDialog

from data import data_handlers


def open_file_dialog():
    filename, _ = QFileDialog().getOpenFileName(filter="*.csv")

    if filename in data_handlers.data_store:
        raise RuntimeError("File is already open")
        filename = None # signal to calling method that no further action is needed

    return filename


def close_file(filename, data_explorer):
    data_handlers.remove_dataset(filename)
    data_explorer.remove_file_item(filename)

    return