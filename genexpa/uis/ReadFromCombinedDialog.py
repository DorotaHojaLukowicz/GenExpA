from itertools import combinations

from genexpa.uis.uis.ReadFromCombinedDialogUI import Ui_Dialog
from PySide2.QtWidgets import QDialog, QFileDialog
from PySide2 import QtCore

from genexpa.uis.LineModelDialog import LineModelDialog
from genexpa.core import explib


class PandasModel(QtCore.QAbstractTableModel):
    def __init__(self, df, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent=parent)
        self._df = df.copy()

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

        val = self._df.iloc[index.row(), index.column()]
        return str(val)

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

class GenesModel(QtCore.QAbstractListModel):
    def __init__(self, genes, sel_inds=None):
        super().__init__()
        self.genes = genes
        if sel_inds is None:
            self.active_inds = list(range(len(self.genes)))
        else:
            self.active_inds = sel_inds

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            return self.genes[self.active_inds[index.row()]]

    def rowCount(self, index):
        return len(self.active_inds)

    def addGene(self, ind):
        if ind > len(self.genes):
            return None

        if ind in self.active_inds:
            return None

        insert_ind = None
        for i, active_ind in enumerate(self.active_inds):
            if active_ind > ind:
                insert_ind = i
                break

        if insert_ind is None:
            insert_ind = len(self.active_inds)

        self.beginInsertRows(QtCore.QModelIndex(), insert_ind, insert_ind)
        self.active_inds.insert(insert_ind, ind)
        self.endInsertRows()

    def removeGene(self, ind):
        if ind not in self.active_inds:
            return  None

        remove_ind = self.active_inds.index(ind)
        self.beginRemoveRows(QtCore.QModelIndex(),remove_ind, remove_ind)
        self.active_inds.pop(remove_ind)
        self.endRemoveRows()

    def removeInd(self, remove_ind):
        if remove_ind > len(self.active_inds):
            return None

        self.beginRemoveRows(QtCore.QModelIndex(),remove_ind, remove_ind)
        self.active_inds.pop(remove_ind)
        self.endRemoveRows()

    def getActiveGenes(self):
        return [self.genes[i] for i in self.active_inds]

class LinesModel(QtCore.QAbstractListModel):
    def __init__(self):
        super().__init__()
        self.lines_models = []

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            lines = self.lines_models[index.row()]
            lines_str = " ".join(lines)
            return lines_str

    def rowCount(self, index):
        return len(self.lines_models)

    def addLineModel(self, new_line_model):
        if new_line_model is None or new_line_model == []:
            return  None
        new_line_model_set = set(new_line_model)

        for line_model in self.lines_models:
            if set(line_model) == new_line_model_set:
                return None

        if len(new_line_model) < 2:
            return None

        end_ind = len(self.lines_models)
        self.beginInsertRows(QtCore.QModelIndex(), end_ind, end_ind)
        self.lines_models.append(tuple(new_line_model))
        self.endInsertRows()

    def removeLineModel(self, ind):
        if ind > len(self.lines_models):
            return None

        self.beginRemoveRows(QtCore.QModelIndex(), ind, ind)
        self.lines_models.pop(ind)
        self.endRemoveRows()

    def clearModel(self):
        if len(self.lines_models) == 0:
            return None

        self.beginRemoveRows(QtCore.QModelIndex(), 0, len(self.lines_models)-1)
        self.lines_models.clear()
        self.endRemoveRows()

    def getCurrentLines(self):
        return self.lines_models[:]

class ReadFromCombinedDialog(QDialog):
    def __init__(self, parent, actions, system):
        super().__init__(parent)
        self.actions = actions
        self.system = system

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.loaded_df = None
        self.loaded_df_model = None

        self.cell_lines = []

        self.init_connections()

    def init_connections(self):
        self.ui.buttonSelectFile.clicked.connect(self.read_file)

        self.ui.buttonSelectRef.clicked.connect(self.add_ref_gene)
        self.ui.buttonUnSelectRef.clicked.connect(self.remove_ref_gene)
        self.ui.buttonAddSingle.clicked.connect(self.add_line_model)

        self.ui.buttonDeleteModel.clicked.connect(self.remove_line_model)
        self.ui.buttonRemoveAll.clicked.connect(self.clear_line_model)
        self.ui.buttonGenerateComb.clicked.connect(self.generate_comb_line_model)

        self.ui.buttonAccept.clicked.connect(self.accept)
        self.ui.buttonCancel.clicked.connect(self.close)

    def read_file(self):
        filename, filter = QFileDialog.getOpenFileName(
            parent=self.system.mainWindowApp,
            caption='Open combined input file',
            dir='.',
            filter='*.xlsx *.xls')

        if filename == "":
            return None

        df = explib.read_combined_input(filename)

        self.ui.loadedFileText.setText(filename)
        self.set_loaded_df(df)

    def set_loaded_df(self, df):
        self.loaded_df = df
        self.loaded_df_model = PandasModel(self.loaded_df)
        self.ui.tableLoadedDF.setModel(self.loaded_df_model)

        # update other models
        self.avail_genes = self.loaded_df.index.unique().tolist()

        self.avail_genes_model = GenesModel(self.avail_genes)
        self.ui.listAvailRef.setModel(self.avail_genes_model)

        self.selected_genes_model = GenesModel(self.avail_genes, [])
        self.ui.listSelRef.setModel(self.selected_genes_model)

        self.cell_lines_model = LinesModel()
        self.ui.listCurrentModels.setModel(self.cell_lines_model)

        self.cell_lines = self.loaded_df.columns.unique().tolist()

    def add_ref_gene(self):
        for qmodel in self.ui.listAvailRef.selectedIndexes():
            self.selected_genes_model.addGene(qmodel.row())

    def remove_ref_gene(self):
        for qmodel in self.ui.listSelRef.selectedIndexes():
            self.selected_genes_model.removeInd(qmodel.row())

    def add_line_model(self):
        lines_selector_dialog = LineModelDialog(self.system.mainWindowApp,
             self.cell_lines)

        accepted = lines_selector_dialog.exec_()
        if not accepted:
            return None

        self.cell_lines_model.addLineModel(lines_selector_dialog.selected_lines)

    def remove_line_model(self):
        for qmodel in self.ui.listCurrentModels.selectedIndexes():
            self.cell_lines_model.removeLineModel(qmodel.row())

    def clear_line_model(self):
        self.cell_lines_model.clearModel()

    def generate_comb_line_model(self):
        for r in range(2, len(self.cell_lines)+1):
            for comb in combinations(self.cell_lines, r):
                self.cell_lines_model.addLineModel(comb)


    def get_dataframes(self):
        # return df_ref, df_target, line_models
        try:
            ref_genes =  self.selected_genes_model.getActiveGenes()
            target_genes = [gene for gene in self.selected_genes_model.genes if gene not in ref_genes]

            df_ref = self.loaded_df.loc[ref_genes,:].copy()
            df_target = self.loaded_df.loc[target_genes,:].copy()

            lines_models = self.cell_lines_model.getCurrentLines()

            return df_ref, df_target, lines_models
        except:
            return None
