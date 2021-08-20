import sys
import traceback

from PyQt5 import QtCore, QtGui, QtWidgets

from sdx.ui.MainWindow import MainWindow


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
    main_window = MainWindow()

    # store globally accessible handle to main window
    app.main_window = main_window

    main_window.showMaximized()
    # MainWindow.show()
    sys.exit(app.exec_())
