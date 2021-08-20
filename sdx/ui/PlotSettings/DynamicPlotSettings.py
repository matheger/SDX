from PyQt5 import QtCore, QtWidgets

from sdx.data import data_handlers


class DynamicPlotSettings(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi()

        return

    def setupUi(self):
        self.setObjectName("DynamicPlotSettings")

        self.formLayout = QtWidgets.QFormLayout(self)
        self.formLayout.setObjectName("formLayout")

        self.HueSelect = QtWidgets.QComboBox(self)
        self.HueSelect.setObjectName("HueSelect")
        self.formLayout.addRow("Hue", self.HueSelect)

        self.HueSelect.currentTextChanged.connect(self._update_plot)

        return

    def _update_plot(self):
        _mw = QtWidgets.QApplication.instance().main_window
        if _mw.PlotSettingsDock.get_auto_update_setting():
            _mw.update_plot()

        return

    def refresh_hue_selector(self):
        self.HueSelect.clear()
        self.HueSelect.addItem("")

        for col_list in data_handlers.active_data.values():
            self.HueSelect.addItems(col_list)

        return

    def get_hue_selection(self):
        return self.HueSelect.currentText()
