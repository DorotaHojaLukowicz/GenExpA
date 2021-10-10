import pandas as pd
import numpy as np

from PySide2.QtCore import QObject, Signal
from PySide2.QtWidgets import QFileDialog, QMessageBox

from PySide2.QtGui import QStandardItemModel, QStandardItem

from genexpa.uis.ReadFromCombinedDialog import ReadFromCombinedDialog
from genexpa.core import explib, helpers

class GenesData(QObject):
    changed = Signal()

    def __init__(self, parent, actions):
        super().__init__(parent)
        self.actions = actions

        self.df = None

    def update(self, df):
        self.df = df
        self.changed.emit()

    def get_genes_count(self):
        if self.df is None:
            return 0
        return self.df.shape[0]

    def get_lines_cout(self):
        if self.df is None:
            return 0
        return len(self.df.columns.unique())

    def is_valid(self):
        return self.get_genes_count() > 0 and self.get_lines_cout() > 0

class LineModelsData(QObject):
    changed = Signal()

    def __init__(self, parent, actions):
        super().__init__(parent)
        self.actions = actions
        self.models = None

    def update(self, models):
        self.models = models
        self.changed.emit()

    def get_models_cout(self):
        if self.models is None:
            return 0
        return len(self.models)

    def as_df(self):
        if self.models is None:
            models = []
        else:
            models = [" ".join(m) for m in self.models]
            return pd.DataFrame(models, columns=["Cell lines"])

    def is_valid(self):
        return self.get_models_cout() > 0

class QuantitiveData(QObject):
    changed = Signal()

    def __init__(self, parent, actions):
        super().__init__(parent)
        self.actions = actions
        self.df = None

    def update(self, df):
        self.df = df
        self.changed.emit()

    def load_file(self, path, df_inputdata):
        df = explib.read_combined_input(path)

        if len(df.columns) != len(df_inputdata.columns):
            base_data = " ".join(df_inputdata.columns)
            quanta_data = " ".join(df.columns)
            error_str = "Not matching in cell lines names\n\n"
            error_str += "Input data (samples = {}):\n{}\n\n".format(len(df_inputdata.columns), base_data)
            error_str += "Quantified data (samples = {}):\n{}""".format(len(df.columns), quanta_data)

            helpers.popup("Bad input/quantified data", error_str)
            return None

        if not all(df.columns == df_inputdata.columns):
            missmatch = np.logical_not(df.columns == df_inputdata.columns)
            base_data = " ".join(df_inputdata.columns[missmatch])
            quanta_data = " ".join(df.columns[missmatch])
            error_str = """Miss match in cell lines names\nmiss matched normal data:\n{}\n\nmiss matched quantified data:\n{}""".format(base_data, quanta_data)

            helpers.popup("Bad input/quantified data", error_str)
            return None

        missing_genes = []

        for ref_gene in df_inputdata.index:
            if ref_gene not in df.index:
                missing_genes.append(ref_gene)

        if len(missing_genes) != 0:
            error_str = "Not all reference genes are present in quantified data\n\n"
            error_str += "Genes in input data\n{}\n\n".format(" ".join(df_inputdata.index))
            error_str += "Genes in quantified data:\n{}\n\n".format(" ".join(df.index))
            error_str += "Missing genes:\n{}""".format(" ".join(missing_genes))

            helpers.popup("Bad input data", error_str)
            return None

        self.df = df
        self.changed.emit()

    def clear(self):
        self.df = None
        self.changed.emit()

    def is_valid(self):
        if self.df is None:
            return False
        else:
            return True

class ResultsData(QObject):
    changed = Signal()
    def __init__(self, parent, actions):
        super().__init__(parent)
        self.actions = actions

        self.df_mean = None
        self.df_best_ref = None
        self.df_RQ = None
        self.df_stat = None
        self.df_comparison = None

        self.df_coherence = None

    def set_results(self, res, apply_remove_mask):
        self.df_mean, self.df_best_ref, self.df_RQ, self.df_stat, self.df_comparison = res

        if apply_remove_mask:
            mask = explib.get_best_series_remove(self.df_best_ref)
            mask_exp = explib.expand_mask(mask, self.df_RQ)
            self.df_mean = self.df_mean.loc[mask]
            self.df_best_ref = self.df_best_ref.loc[mask]
            self.df_RQ = self.df_RQ.loc[mask_exp]
            self.df_comparison = self.df_comparison[mask]

            _df_stat = self.df_stat.loc[mask]
            if hasattr(self.df_stat, "alpha"):
                _df_stat.alpha = self.df_stat.alpha
            if hasattr(self.df_stat, "stat_model"):
                _df_stat.stat_model = self.df_stat.stat_model

            self.df_stat = _df_stat

        self.df_coherence = explib.calc_coherence(self.df_comparison)

        self.changed.emit()

    def clear(self):
        self.df_mean = None
        self.df_best_ref = None
        self.df_RQ = None
        self.df_stat = None
        self.df_comparison = None

        self.df_coherence = None

        self.changed.emit()

    def get_summary_coherence(self):
        if self.df_coherence is not None:
            return self.df_coherence.mean(axis=1).values[0]
        else:
            return 0.0

    def is_valid(self):
        if self.df_mean is None:
            return False
        return True

    def get_all_df(self):
        return [self.df_mean, self.df_best_ref, self.df_RQ, self.df_stat, self.df_comparison, self.df_coherence]

class ParametersData(QObject):
    changed = Signal()
    def __init__(self, parent, actions):
        super().__init__(parent)
        self.actions = actions

        self.normalization_algorithms = ["Normfinder"] #["Normfinder", "GeNorm"]
        self.normalization_algorithms_model = QStandardItemModel (len(self.normalization_algorithms), 1)
        for i, norm_algo in enumerate(self.normalization_algorithms):
            item = QStandardItem(norm_algo)
            self.normalization_algorithms_model.setItem(i, 0, item)

        self.stat_algorithms = ["Pairwise t-test, Holm adjustment",
                                "Kolmogorov-Smirnov/Kruskal-Wallis, post: Dunn’s test",
                                "Mann-Whitney/Kruskal-Wallis, post: Dunn’s test",
                                "Kruskal-Wallis"]
        #self.stat_algorithms_modes = ["kw", "ks", "welch"]
        self.stat_algorithms_model = QStandardItemModel(len(self.stat_algorithms), 1)
        for i, stat_algo in enumerate(self.stat_algorithms):
            item = QStandardItem(stat_algo)
            self.stat_algorithms_model.setItem(i, 0, item)

        # internal data
        self.confidence = 0.05
        self.remove_rep = 0
        self.sample_rep = 1
        self.select_best = False

    def is_valid(self):
        if self.confidence < 0.0:
            return False

        if self.remove_rep < 0:
            return False

        """
        if self.sample_rep < 0:
            return False
        """

        return True

    def update(self, value, param_str):
        #self.sel_normalization_algorithm =
        if param_str == "confidence":
            try:
                self.confidence = float(value)
            except:
                self.confidence = -1.0

        elif param_str == "remove_rep":
            try:
                self.remove_rep = int(value)
            except:
                self.remove_rep = -1

            """
        elif param_str == "sample_rep":
            try:
                self.sample_rep = int(value)
            except:
                self.sample_rep = -1
            """

        elif param_str == "select_best":
            self.select_best = bool(value)

        self.changed.emit()


class System(QObject):
    def __init__(self, parent, app, actions):
        super().__init__(parent)
        self.mainWindowApp = self.parent()

        self.app = app

        self.actions = actions

        self.reference_genes_data = GenesData(self, self.actions)
        self.target_genes_data = GenesData(self, self.actions)
        self.line_models_data = LineModelsData(self, self.actions)
        self.quantitive_data = QuantitiveData(self, self.actions)
        self.results_data = ResultsData(self, self.actions)

        self.parameters_data = ParametersData(self, self.actions)

        self.read_from_combined_dialog = ReadFromCombinedDialog(self.mainWindowApp,
                                                                self.actions,
                                                                self)

        self.init_connections()

    def init_connections(self):
        self.actions.read_from_combined_input.connect(self.read_from_combined_input)
        self.actions.load_quantified.connect(self.load_quantified)

    def read_from_combined_input(self):
        accepted = self.read_from_combined_dialog.exec_()

        if accepted == 0:
            return None

        combined_data = self.read_from_combined_dialog.get_dataframes()

        if combined_data is None:
            return None

        df_ref, df_target, lines_models = combined_data

        self.reference_genes_data.update(df_ref)
        self.target_genes_data.update(df_target)
        self.line_models_data.update(lines_models)

    def load_quantified(self):
        if not self.input_valid():
            helpers.popup("Input data not loaded!",
                          "Before loading quantified data, first load proper input data!",
                          "warning")
            return None

        filename, filter = QFileDialog.getOpenFileName(
            parent=self.mainWindowApp,
            caption='Open quantified input file',
            dir='.',
            filter='*.xlsx *.xls')

        if filename == "":
            return None

        succes = self.quantitive_data.load_file(filename, self.reference_genes_data.df)
        if succes:
            self.mainWindowApp.update_gui()

    def input_valid(self):
        return (self.reference_genes_data.is_valid() and
        self.target_genes_data.is_valid() and
        self.line_models_data.is_valid())
