# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'ui\_QtDesigner\_CloseFilesDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CloseFilesDialog(object):
    def setupUi(self, CloseFilesDialog):
        CloseFilesDialog.setObjectName("CloseFilesDialog")
        CloseFilesDialog.resize(360, 279)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CloseFilesDialog.sizePolicy().hasHeightForWidth())
        CloseFilesDialog.setSizePolicy(sizePolicy)
        CloseFilesDialog.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.CloseFilesDialogButtonBox = QtWidgets.QDialogButtonBox(CloseFilesDialog)
        self.CloseFilesDialogButtonBox.setGeometry(QtCore.QRect(10, 240, 341, 32))
        self.CloseFilesDialogButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.CloseFilesDialogButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.CloseFilesDialogButtonBox.setObjectName("CloseFilesDialogButtonBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(CloseFilesDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 341, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.FilesListView = QtWidgets.QListView(self.verticalLayoutWidget)
        self.FilesListView.setObjectName("FilesListView")
        self.verticalLayout.addWidget(self.FilesListView)

        self.retranslateUi(CloseFilesDialog)
        self.CloseFilesDialogButtonBox.accepted.connect(CloseFilesDialog.accept)
        self.CloseFilesDialogButtonBox.rejected.connect(CloseFilesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(CloseFilesDialog)

    def retranslateUi(self, CloseFilesDialog):
        _translate = QtCore.QCoreApplication.translate
        CloseFilesDialog.setWindowTitle(_translate("CloseFilesDialog", "Close File(s)"))
        self.label.setText(_translate("CloseFilesDialog", "Select file(s) to close:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CloseFilesDialog = QtWidgets.QDialog()
    ui = Ui_CloseFilesDialog()
    ui.setupUi(CloseFilesDialog)
    CloseFilesDialog.show()
    sys.exit(app.exec_())

