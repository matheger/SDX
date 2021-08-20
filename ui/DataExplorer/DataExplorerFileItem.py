import os.path

from PyQt5 import QtCore
from PyQt5.Qt import QTreeWidgetItem

from sdx.ui.DataExplorer.DataExplorerColumnItem import DataExplorerColumnItem

from sdx.data import data_handlers


class DataExplorerFileItem(QTreeWidgetItem):
    def __init__(self, parent, filename):
        super().__init__(parent)

        self.filename = filename

        self.setToolTip(0, filename)
        _name = f"{os.path.basename(filename)} ({str(data_handlers.get_dataset_len(filename))} rows)"
        self.setText(0, _name)

        # set only the "IsEnabled" flag for the item - disables selectability, drag&drop, editing, ...
        self.setFlags(QtCore.Qt.ItemFlags(32))

        font = self.font(0)
        font.setWeight(63)
        self.setFont(0, font)
        self.setFirstColumnSpanned(True)
        self.setExpanded(True)

        self.column_items = {}
        dataset = data_handlers.data_store[filename]

        for col in dataset:
            col_dtype = str(dataset.dtypes[col])
            col_item = DataExplorerColumnItem(self, col, col_dtype)

            self.column_items[col] = col_item
            self.addChild(col_item)

        return
