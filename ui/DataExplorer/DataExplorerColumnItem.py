from PyQt5.Qt import QTreeWidgetItem

class DataExplorerColumnItem(QTreeWidgetItem):
    def __init__(self, parent, column_name, column_dtype):
        super().__init__(parent)

        self.column_name = column_name

        self.setText(0, column_name)
        self.setText(1, column_dtype)

        return