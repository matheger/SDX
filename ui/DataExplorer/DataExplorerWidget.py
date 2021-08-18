from collections import defaultdict

import os.path

from PyQt5 import QtWidgets, QtCore
from PyQt5.Qt import QTreeWidget

from ui.DataExplorer.DataExplorerColumnItem import DataExplorerColumnItem
from ui.DataExplorer.DataExplorerFileItem import DataExplorerFileItem
from ui import dialogs

from data import data_handlers
from files import file_handlers


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
        self.allowed_dataset_len = None

        return

    def add_file_item(self, filename):
        file_item = DataExplorerFileItem(self, filename)
        self.file_items[filename] = file_item
        self.addTopLevelItem(file_item)

        # deactivate new item if dataset length is inconsistent with any existing selection
        if self.allowed_dataset_len is not None:
            self._disallow_inconsistent_files()

        return

    def remove_file_item(self, filename):
        item = self.file_items.pop(filename)
        index = self.indexFromItem(item, 0)
        self.takeTopLevelItem(index.row())

        return

    def _disallow_inconsistent_files(self):
        if self.allowed_dataset_len is None:
            return

        for filename, item in self.file_items.items():
            if data_handlers.get_dataset_len(filename) != self.allowed_dataset_len:
                item.setDisabled(True)

        return

    def _allow_all_files(self):
        for item in self.file_items.values():
            item.setDisabled(False)

        self.allowed_dataset_len = None

        return

    def clear_selection(self):
        self.clearSelection()
        self._allow_all_files()

        return

    @QtCore.pyqtSlot()
    def update_active_datasets(self):
        data_handlers.active_data.clear()

        # if all data has been unselected, re-allow all datasets and do nothing else
        if not self.selectedItems():
            self._allow_all_files()
            return

        for item in self.selectedItems():
            # operate only on column items, not file items (which shouldn't be selectable anyway)
            if not isinstance(item, DataExplorerColumnItem):
                continue

            filename = item.parent().filename
            data_handlers.active_data[filename].append(item.column_name)

            # if no allowed dataset length is currently set, set it now
            if self.allowed_dataset_len is None:
                self.allowed_dataset_len = data_handlers.get_dataset_len(filename)
                self._disallow_inconsistent_files()

        # if auto updating is enabled, kick off the plotting call now (using the MainWindow method);
        # if update fails due to inconsistent dataset lengths, mimic the error in the MainWindow method
        _mw = QtWidgets.QApplication.instance().MainWindow
        if _mw.PlotSettingsDock.get_auto_update_setting():
            try:
                _mw.update_plot()
            except data_handlers.InconsistentLengthError:
                dialogs.show_error("Selected datasets have inconsistent lengths")

        return
