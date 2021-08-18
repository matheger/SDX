from PyQt5 import QtCore, QtWidgets
from PyQt5.Qt import QMainWindow

from ui.DataExplorer.DataExplorerDock import DataExplorerDock
from ui.PlotSettings.PlotSettingsDock import PlotSettingsDock
from ui.PlotView import PlotView
from ui import dialogs

from data import data_handlers


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.PlotView = PlotView()
        self.horizontalLayout.addWidget(self.PlotView)

        # self.menubar = QtWidgets.QMenuBar(self)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 1064, 800))
        # self.menubar.setObjectName("menubar")
        # self.setMenuBar(self.menubar)

        # self.statusbar = QtWidgets.QStatusBar(self)
        # self.statusbar.setObjectName("statusbar")
        # self.setStatusBar(self.statusbar)

        self.DataExplorerDock = DataExplorerDock(self)
        self.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.DataExplorerDock)

        self.PlotSettingsDock = PlotSettingsDock(self)
        self.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.PlotSettingsDock)

        self.retranslateUi()

        QtCore.QMetaObject.connectSlotsByName(self)
        return

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Seaborn Data Explorer"))
        self.DataExplorerDock.setWindowTitle(_translate("MainWindow", "Data Explorer"))

    @QtCore.pyqtSlot()
    def update_plot(self):
        try:
            data = data_handlers.get_active_data()
        except data_handlers.InconsistentLengthError:
            dialogs.show_error("Selected datasets have inconsistent lengths")
            return

        if (num_samples := self.PlotSettingsDock.get_num_samples_setting()):
            num_samples = min([len(data), num_samples]) # avoid ValueError when requesting too many samples
            data = data.sample(num_samples)

        try:
            fig = data_handlers.create_seaborn_plot(data).fig
        except ValueError:
            dialogs.show_warning("No data to display")
            return

        self.PlotView.plot(fig)

        return
