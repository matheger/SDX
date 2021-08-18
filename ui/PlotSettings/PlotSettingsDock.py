from PyQt5 import QtCore, QtWidgets

from ui.PlotSettings.StaticPlotSettings import StaticPlotSettings

from data import data_handlers


class PlotSettingsDock(QtWidgets.QDockWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        self.setObjectName("PlotSettingsDock")

        self.DockContents = QtWidgets.QWidget(self)
        self.DockContents.setObjectName("Contents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.DockContents)
        self.verticalLayout.setObjectName("verticalLayout")

        # create static portion of properties section
        self.StaticPlotSettingsWidget = StaticPlotSettings(self)
        self.verticalLayout.addWidget(self.StaticPlotSettingsWidget)

        self.setMinimumSize(QtCore.QSize(200, 0))
        self.setWidget(self.DockContents)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        return

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Plot Settings"))

    def get_num_samples_setting(self):
        if self.StaticPlotSettingsWidget.NumSamplesCheckBox.isChecked():
            num_samples = self.StaticPlotSettingsWidget.NumSamplesSpinBox.value()
        else:
            num_samples = None

        return num_samples

    def get_auto_update_setting(self):
        return self.StaticPlotSettingsWidget.AutoUpdateCheckBox.isChecked()