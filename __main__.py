import sys
import traceback

from PyQt5 import QtCore, QtGui, QtWidgets

import sdx.ui.MainWindow


# custom exception handler
def exception_handler(exc_type, exc_value, exc_trace):
    """Custom exception handling"""

    message = "".join(traceback.format_exception_only(exc_type, exc_value))

    # print full traceback
    message += "\nFull traceback:\n" + \
               "".join(traceback.format_tb(exc_trace))

    msg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, "SYNC",
                                f"An exception has occurred:\n\n{message}",
                                flags=QtCore.Qt.WindowStaysOnTopHint)
    msg.exec()

    return


def run():
    import sys
    app = QtWidgets.QApplication(sys.argv)

    sys.excepthook = exception_handler
    MainWindow = ui.MainWindow.MainWindow()

    # store globally accessible handle to main window
    app.MainWindow = MainWindow

    MainWindow.showMaximized()
    # MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run()