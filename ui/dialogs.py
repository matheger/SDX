from PyQt5 import QtWidgets


def show_error(message):
    dialog = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Icon.Critical,
                                  "Error", message,
                                   QtWidgets.QMessageBox.StandardButton.Ok)
    dialog.exec()

    return


def show_warning(message):
    dialog = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Icon.Warning,
                                   "Warning", message,
                                   QtWidgets.QMessageBox.StandardButton.Ok)
    dialog.exec()

    return


def show_information(message):
    dialog = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Icon.Information,
                                   "Information", message,
                                   QtWidgets.QMessageBox.StandardButton.Ok)
    dialog.exec()

    return