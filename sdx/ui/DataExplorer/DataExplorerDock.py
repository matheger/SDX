from PyQt5 import QtCore, QtWidgets

from sdx.ui.DataExplorer.DataExplorerWidget import DataExplorerWidget
from sdx.ui.CloseFilesDialog import CloseFilesDialog
from sdx.ui import dialogs

from sdx.data import data_handlers
from sdx.files import file_handlers


class DataExplorerDock(QtWidgets.QDockWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.setupUi()

        return

    def setupUi(self):
        self.setObjectName("DataExplorerDock")

        self.DockContents = QtWidgets.QWidget(self)
        self.DockContents.setObjectName("DockContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.DockContents)
        self.verticalLayout.setObjectName("verticalLayout")

        self.ButtonsLayout = QtWidgets.QHBoxLayout(self.DockContents)
        self.ButtonsLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.ButtonsLayout.setContentsMargins(0, 0, 0, 0)
        self.ButtonsLayout.setObjectName("DataExplorerButtonsLayout")
        self.verticalLayout.addLayout(self.ButtonsLayout)

        self.DataExplorer = DataExplorerWidget(self.DockContents)
        self.verticalLayout.addWidget(self.DataExplorer)

        self.OpenFileButton = QtWidgets.QPushButton(self.DockContents)
        self.OpenFileButton.setObjectName("OpenFileButton")
        self.ButtonsLayout.addWidget(self.OpenFileButton)

        self.CloseFileButton = QtWidgets.QPushButton(self.DockContents)
        self.CloseFileButton.setObjectName("CloseFileButton")
        self.ButtonsLayout.addWidget(self.CloseFileButton)

        self.CloseAllButton = QtWidgets.QPushButton(self.DockContents)
        self.CloseAllButton.setObjectName("CloseAllButton")
        self.ButtonsLayout.addWidget(self.CloseAllButton)

        self.ClearSelectionButton = QtWidgets.QPushButton(self.DockContents)
        self.ClearSelectionButton.setObjectName("ClearSelectionButton")
        self.ButtonsLayout.addWidget(self.ClearSelectionButton)

        self.setMinimumSize(QtCore.QSize(200, 0))
        self.setWidget(self.DockContents)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        return

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Data Explorer"))
        self.OpenFileButton.setText(_translate("self", "Open File"))
        self.CloseFileButton.setText(_translate("self", "Close File(s)"))
        self.CloseAllButton.setText(_translate("self", "Close All"))
        self.ClearSelectionButton.setText(_translate("self", "Clear Selection"))

        return

    @QtCore.pyqtSlot()
    def on_OpenFileButton_clicked(self):
        try:
            filename = file_handlers.open_file_dialog()
        except file_handlers.FileOpenError:
            dialogs.show_warning("File is already open")
            return

        if not filename: # empty filename: user closed dialog
            return

        data_handlers.read_csv_data(filename)
        self.DataExplorer.add_file_item(filename)

        return

    @QtCore.pyqtSlot()
    def on_CloseFileButton_clicked(self):
        dialog = CloseFilesDialog()
        retval = dialog.exec()

        if not retval: # user canceled dialog or selected no files to be closed
            return

        else:
            for filename in retval:
                file_handlers.close_file(filename, self.DataExplorer)

        return

    @QtCore.pyqtSlot()
    def on_CloseAllButton_clicked(self):
        open_files = list(self.DataExplorer.file_items)
        for filename in open_files:
            file_handlers.close_file(filename, self.DataExplorer)

    @QtCore.pyqtSlot()
    def on_ClearSelectionButton_clicked(self):
        self.DataExplorer.clear_selection()