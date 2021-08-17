from PyQt5 import QtCore, QtGui, QtWidgets

from data import data_handlers


class StaticPlotSettings(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi()
        return

    def setupUi(self):
        self.setObjectName("self")

        self.formLayout = QtWidgets.QFormLayout(self)
        self.formLayout.setObjectName("formLayout")

        self.PlotTypeLabel = QtWidgets.QLabel(self)
        self.PlotTypeLabel.setObjectName("PlotTypeLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.PlotTypeLabel)

        # self.PlotTypeSelector = QtWidgets.QComboBox(self)
        # self.PlotTypeSelector.setObjectName("PlotTypeSelector")
        # self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.PlotTypeSelector)

        self.NumSamplesCheckBox = QtWidgets.QCheckBox(self)
        self.NumSamplesCheckBox.setObjectName("NumSamplesCheckBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.NumSamplesCheckBox)

        self.NumSamplesSpinBox = QtWidgets.QSpinBox(self)
        self.NumSamplesSpinBox.setObjectName("NumSamplesSpinBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.NumSamplesSpinBox)
        self.NumSamplesSpinBox.setWrapping(False)
        self.NumSamplesSpinBox.setRange(1,999999999) # no one should ever plot that many points... I hope...
        self.NumSamplesSpinBox.setSingleStep(100)
        self.NumSamplesSpinBox.setValue(1000)

        # start with sampling disabled
        self.NumSamplesCheckBox.setChecked(False)
        self.NumSamplesSpinBox.setEnabled(False)
        self.NumSamplesCheckBox.stateChanged.connect(self.toggle_sampling)

        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.LabelRole, spacerItem)

        self.UpdateButton = QtWidgets.QPushButton(self)
        self.UpdateButton.setObjectName("UpdateButton")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.UpdateButton)

        self.AutoUpdateCheckBox = QtWidgets.QCheckBox(self)
        self.AutoUpdateCheckBox.setIconSize(QtCore.QSize(14, 14))
        self.AutoUpdateCheckBox.setObjectName("AutoUpdateCheckBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.AutoUpdateCheckBox)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        return

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.PlotTypeLabel.setText(_translate("self", "Plot type"))
        self.NumSamplesCheckBox.setText(_translate("self", "Samples"))
        self.UpdateButton.setText(_translate("self", "Update"))
        self.AutoUpdateCheckBox.setText(_translate("self", "Auto-update"))

        return

    @QtCore.pyqtSlot()
    def on_UpdateButton_clicked(self):
        # MainWindow will delegate all necessary plotting calls
        _mw = QtWidgets.QApplication.instance().MainWindow
        _mw.update_plot()

        return

    @QtCore.pyqtSlot()
    def toggle_sampling(self):
        self.NumSamplesSpinBox.setEnabled(self.NumSamplesCheckBox.isChecked())

        return
