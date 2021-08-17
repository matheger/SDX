from collections import defaultdict

import os.path

from PyQt5 import QtWidgets, QtCore
from PyQt5.Qt import QTreeWidget

import ui.DataExplorer.DataExplorerColumnItem
from ui.DataExplorer.DataExplorerFileItem import DataExplorerFileItem
from ui import dialogs

from data import data_handlers


class DataExplorerWidget(QTreeWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.setObjectName("parent")
        self.setColumnCount(2)
        self.setHeaderLabels(["Column", "dtype"])
        self.setColumnWidth(0, 80)
        self.setColumnWidth(1, 10)

        self.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.MultiSelection)
        self.itemSelectionChanged.connect(self.update_active_datasets)

        self.file_items = {}

        return

    def add_file_item(self, filename):
        file_item = DataExplorerFileItem(self, filename)
        self.file_items[filename] = file_item
        self.addTopLevelItem(file_item)

        return

    def remove_file_item(self, filename):
        item = self.file_items.pop(filename)
        index = self.indexFromItem(item, 0)
        self.takeTopLevelItem(index.row())

        return

    @QtCore.pyqtSlot()
    def update_active_datasets(self):
        data_handlers.active_data.clear()

        for item in self.selectedItems():
            if isinstance(item, ui.DataExplorer.DataExplorerColumnItem.DataExplorerColumnItem):
                filename = item.parent().filename
                data_handlers.active_data[filename].append(item.column_name)

        # if auto updating is enabled, kick off the plotting call now (using the MainWindow method);
        # if update fails due to inconsistent dataset lengths, mimic the error in the MainWindow method
        _mw = QtWidgets.QApplication.instance().MainWindow
        if _mw.PlotSettingsDock.get_auto_update_setting():
            try:
                _mw.update_plot()
            except data_handlers.InconsistentLengthError:
                dialogs.show_error("Selected datasets have inconsistent lengths")

        return
