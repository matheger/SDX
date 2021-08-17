import os.path

from PyQt5 import QtCore, QtGui, QtWidgets

from data import data_handlers


class CloseFilesDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setup_ui()

        return

    def setup_ui(self):
        self.setObjectName("CloseFilesDialog")
        self.resize(360, 279)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())

        self.setSizePolicy(sizePolicy)
        self.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)

        self.CloseFilesDialogButtonBox = QtWidgets.QDialogButtonBox(self)
        self.CloseFilesDialogButtonBox.setGeometry(QtCore.QRect(10, 240, 341, 32))
        self.CloseFilesDialogButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.CloseFilesDialogButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.CloseFilesDialogButtonBox.setObjectName("CloseFilesDialogButtonBox")

        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 341, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.FilesList = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.FilesList.setObjectName("FilesList")
        self.FilesList.setSelectionMode(self.FilesList.SelectionMode.MultiSelection)
        self.verticalLayout.addWidget(self.FilesList)

        self.retranslateUi()
        self.CloseFilesDialogButtonBox.accepted.connect(self.accept)
        self.CloseFilesDialogButtonBox.rejected.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.populate_files_list()

        return

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("CloseFilesDialog", "Close File(s)"))
        self.label.setText(_translate("CloseFilesDialog", "Select file(s) to close:"))

        return

    def populate_files_list(self):
        open_files = data_handlers.data_store.keys()

        # items in list are displayed with their base name, but have full file names as an attribute
        for filename in open_files:
            item = QtWidgets.QListWidgetItem(os.path.basename(filename), self.FilesList)
            item.filename = filename
            self.FilesList.addItem(item)

        return

    def exec(self):
        """Reimplement `exec` method to return list of selected files, or `None` on dialog cancel"""

        ret_val = super().exec()

        # OK button was pressed
        if ret_val == 1:
            selected_items = self.FilesList.selectedItems()
            filenames = [item.filename for item in selected_items]
            return filenames

        # dialog canceled
        else:
            return None