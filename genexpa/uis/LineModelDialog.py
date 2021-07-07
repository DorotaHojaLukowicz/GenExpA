from genexpa.uis.uis.LineModelDialogUI import Ui_Dialog
from PySide2.QtWidgets import QDialog
from PySide2 import QtCore


class LineListModel(QtCore.QAbstractListModel):
    def __init__(self, lines):
        super().__init__()
        self.lines = lines

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            return self.lines[index.row()]

    def rowCount(self, index):
        return len(self.lines)

class LineModelDialog(QDialog):
    def __init__(self, parent, lines):
        super().__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.selected_lines = []
        self.selected_lines_str = ""

        self.lines = lines
        self.list_model = LineListModel(self.lines)
        self.ui.listLines.setModel(self.list_model)

        self.init_connections()

    def init_connections(self):
        self.ui.buttonAddLine.clicked.connect(self.add_to_line)
        self.ui.buttonDiscard.clicked.connect(self.close)
        self.ui.buttonAccept.clicked.connect(self.accept)

    def add_to_line(self):
        for qmodel in self.ui.listLines.selectedIndexes():
            ind = qmodel.row()
            sel_line = self.lines[ind]
            if sel_line not in self.selected_lines:
                self.add_to_current_model(sel_line)


    def add_to_current_model(self, line):
        self.selected_lines.append(line)
        self.selected_lines_str += " {}".format(line)
        self.ui.labelModelText.setText(self.selected_lines_str)
