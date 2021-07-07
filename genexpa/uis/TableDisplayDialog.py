from genexpa.uis.uis.TableDisplayDialogUI import Ui_Dialog
from PySide2.QtWidgets import QDialog
from PySide2 import QtCore

from genexpa.core import explib


class PandasModel(QtCore.QAbstractTableModel):
    def __init__(self, df, parent=None, str_col=[]):
        QtCore.QAbstractTableModel.__init__(self, parent=parent)
        self.str_col = str_col
        self._df = df

    def toDataFrame(self):
        return self._df.copy()

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if role != QtCore.Qt.DisplayRole:
            return None

        if orientation == QtCore.Qt.Horizontal:
            return self._df.columns.tolist()[section]

        elif orientation == QtCore.Qt.Vertical:
            return self._df.index.tolist()[section]

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role != QtCore.Qt.DisplayRole:
            return None

        if not index.isValid():
            return None

        if index.column() in self.str_col:
            return str(self._df.iloc[index.row(), index.column()])
        return '{:0.3e}'.format(self._df.iloc[index.row(), index.column()])

    def setData(self, index, value, role):
        row = self._df.index[index.row()]
        col = self._df.columns[index.column()]
        if hasattr(value, 'toPyObject'):
            # PyQt4 gets a QVariant
            value = value.toPyObject()
        else:
            # PySide gets an unicode
            dtype = self._df[col].dtype
            if dtype != object:
                value = None if value == '' else dtype.type(value)
        self._df.set_value(row, col, value)

        return True

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self._df.index)

    def columnCount(self, parent=QtCore.QModelIndex()):
        return len(self._df.columns)

class TableDisplayDialog(QDialog):
    def __init__(self, parent, df, name="Table", str_col=[]):
        super().__init__(parent)
        self._df = explib.flatten_mlvl_index(df)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle(name)

        self.model = PandasModel(self._df, None, str_col)
        self.ui.tableView.setModel(self.model)
