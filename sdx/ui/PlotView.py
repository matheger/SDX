from PyQt5 import QtCore, QtWidgets, QtGui

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

import pandas as pd
import seaborn as sns

class PlotView(FigureCanvasQTAgg):
    def __init__(self):
        super().__init__()
        self.setObjectName("PlotView")
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.context_menu)

        return

    def plot(self, figure):
        assert isinstance(figure, Figure)

        # resize image to fit window on first display (assuming 80 dpi because why not)
        _sh = self.sizeHint()
        _w, _h = _sh.width(), _sh.height()
        figure.set_dpi(80)
        figure.set_size_inches(_w / 80, _h / 80)
        self.figure = figure

        self.draw()

        return

    def context_menu(self):
        menu = QtWidgets.QMenu()
        menu.addAction("Save", self.save_figure)
        menu.exec(QtGui.QCursor.pos())

        return

    def save_figure(self):
        filename, _ = QtWidgets.QFileDialog().getSaveFileName(self, filter="*.png")
        self.figure.savefig(filename)

        return