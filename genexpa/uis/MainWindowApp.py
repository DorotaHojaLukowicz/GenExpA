import os
import time

from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PySide2.QtGui import QDoubleValidator, QIntValidator
from PySide2 import QtCore

from genexpa.uis.uis.MainWindowUI import Ui_MainWindow
from genexpa.uis.WaitPopup import WaitPopup
from genexpa.uis.TableDisplayDialog import TableDisplayDialog

from genexpa.core.actions import Actions
from genexpa.core.system import System
from genexpa.core import helpers, explib


class CoherenceScoreModel(QtCore.QAbstractListModel):
    def __init__(self):
        super().__init__()
        self.coherence_list = [] # gene, value
        self.coherence_df = None

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            gene, value = self.coherence_list[index.row()]

            gene_str = "{:<14}  {:.2f}".format(gene, value)
            return gene_str

    def rowCount(self, index):
        return len(self.coherence_list)


    def clearModel(self):
        if len(self.coherence_list) == 0:
            return None

        self.beginRemoveRows(QtCore.QModelIndex(), 0, len(self.coherence_list)-1)
        self.coherence_list.clear()
        self.coherence_df = None
        self.endRemoveRows()

    def setCoherence(self, df):
        if self.coherence_df is df:
            return

        self.clearModel()

        self.coherence_df = df
        genes = self.coherence_df.columns.get_level_values(0).unique()
        self.beginInsertRows(QtCore.QModelIndex(), 0, len(genes))

        values_sum = 0.0
        for gene in genes:
            value = df[gene].values.mean()
            self.coherence_list.append([
                gene,
                value
            ])
            values_sum += value

        mean = values_sum/len(genes)
        self.coherence_list.append(["Average", mean])

        self.endInsertRows()

class MainWindowApp(QMainWindow):
    def __init__(self, app):
        super().__init__()


        self.actions = Actions()
        self.system = System(self, app, self.actions)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.coherence_score_model = CoherenceScoreModel()
        self.ui.listCoherence.setModel(self.coherence_score_model)
        self.ui.listCoherence.setSelectionRectVisible(False)

        self.remove_validator = QIntValidator(0,100)
        self.ui.lineEditRemoveRep.setValidator(self.remove_validator)
        #self.ui.lineEditSampleRepetition.setValidator(self.remove_validator)

        self.ui.lineEditConfidence.setText(str(self.system.parameters_data.confidence))
        self.ui.lineEditRemoveRep.setText(str(self.system.parameters_data.remove_rep))
        #self.ui.lineEditSampleRepetition.setText(str(self.system.parameters_data.sample_rep))

        self.ui.checkSelectBest.setChecked(self.system.parameters_data.select_best)

        self.ui.comboBoxNormalizationAlgorithm.setModel(self.system.parameters_data.normalization_algorithms_model)
        self.ui.comboBoxStatModel.setModel(self.system.parameters_data.stat_algorithms_model)

        self.input_data = None

        self.init_connections()

        self.update_gui()

    def init_connections(self):
        self.ui.actionRead_from_combined_input.triggered.connect(self.actions.read_from_combined_input)
        self.ui.actionLoad_Quantified.triggered.connect(self.actions.load_quantified)
        self.ui.actionActivate_license.triggered.connect(self.actions.open_licence_popup)

        self.system.reference_genes_data.changed.connect(self.reference_genes_data_changed)
        self.system.target_genes_data.changed.connect(self.target_genes_data_changed)
        self.system.line_models_data.changed.connect(self.line_models_data_changed)
        self.system.quantitive_data.changed.connect(self.update_gui)
        self.system.results_data.changed.connect(self.update_gui)

        self.ui.buttonShowRef.clicked.connect(self.show_ref_table)
        self.ui.buttonShowTarget.clicked.connect(self.show_target_table)
        self.ui.buttonShowModels.clicked.connect(self.show_model_list)
        self.ui.buttonShowQuantitive.clicked.connect(self.show_quantitivie)

        self.ui.buttonRemoveQuantitive.clicked.connect(self.system.quantitive_data.clear)

        self.ui.buttonRunCalculations.clicked.connect(self.run_calculations)

        self.ui.lineEditConfidence.textChanged.connect(
            lambda x: self.parameters_changed(x, "confidence"))

        self.ui.lineEditRemoveRep.textChanged.connect(
            lambda x:self.parameters_changed(x, "remove_rep"))

        """
        self.ui.lineEditSampleRepetition.textChanged.connect(
            lambda x: self.parameters_changed(x, "sample_rep"))
        """

        self.ui.checkSelectBest.stateChanged.connect(
            lambda x: self.parameters_changed(x, "select_best"))

        self.ui.buttonShowBestRef.clicked.connect(self.show_best_ref)
        self.ui.buttonShowRQ.clicked.connect(self.show_RQ)
        self.ui.buttonShowStatistic.clicked.connect(self.show_statistic)
        #self.ui.buttonShowCoherence.clicked.connect(self.show_coherence_score)

        self.ui.buttonExportResults.clicked.connect(self.export_results)
        self.ui.buttonExportGraphs.clicked.connect(self.export_graphs)

    def parameters_changed(self, value, parameter_str):
        self.system.parameters_data.update(value, parameter_str)
        self.update_gui()

    def reference_genes_data_changed(self):
        self.ui.labelRefCnt.setText(str(self.system.reference_genes_data.get_genes_count()))
        self.update_gui()

    def target_genes_data_changed(self):
        self.ui.labelTargetCnt.setText(str(self.system.target_genes_data.get_genes_count()))
        self.update_gui()

    def line_models_data_changed(self):
        self.ui.labelModelsCnt.setText(str(self.system.line_models_data.get_models_cout()))
        self.update_gui()


    def show_ref_table(self):
        self.ref_table = TableDisplayDialog(self.system.mainWindowApp,
                                            self.system.reference_genes_data.df,
                                            "Reference genes data")
        self.ref_table.show()

    def show_target_table(self):
        self.target_table = TableDisplayDialog(self.system.mainWindowApp,
                                               self.system.target_genes_data.df,
                                               "Target genes data")
        self.target_table.show()

    def show_model_list(self):
        self.models_table =TableDisplayDialog(self.system.mainWindowApp,
                                              self.system.line_models_data.as_df(),
                                              "Lines models data",
                                              [0])
        self.models_table.show()

    def show_quantitivie(self):
        self.quantitive_table = TableDisplayDialog(self.system.mainWindowApp,
                                                   self.system.quantitive_data.df,
                                                   "Quantitive gene data")
        self.quantitive_table.show()

    def show_best_ref(self):
        self.best_table = TableDisplayDialog(self.system.mainWindowApp,
            self.system.results_data.df_best_ref,
            "Best reference gene/pair results data",
            [0]
        )
        self.best_table.show()

    def show_RQ(self):
        self.RQ_table = TableDisplayDialog(self.system.mainWindowApp,
            self.system.results_data.df_RQ,
            "RQ results data"
        )
        self.RQ_table.show()

    def show_statistic(self):
        self.stat_table = TableDisplayDialog(self.system.mainWindowApp,
            self.system.results_data.df_stat,
            "Statistic results data"
        )
        self.stat_table.show()

    def show_coherence_score(self):
        self.coherence_table = TableDisplayDialog(self.system.mainWindowApp,
            self.system.results_data.df_coherence.T,
            "Coherence score results data",
            str_col = list(range(len(self.system.results_data.df_coherence.columns)))
        )
        self.coherence_table.show()

    def run_calculations(self):
        if not (self.system.input_valid() and self.system.parameters_data.is_valid()):
            return None

        df_ref = explib.append_group_index(self.system.reference_genes_data.df)

        df_target = self.system.target_genes_data.df
        df_ref_norm = self.system.quantitive_data.df

        models = self.system.line_models_data.models

        remove_rep = self.system.parameters_data.remove_rep
        sample_rep = self.system.parameters_data.sample_rep

        confidence = self.system.parameters_data.confidence

        stat_mode = self.ui.comboBoxStatModel.currentIndex()

        ind = self.ui.comboBoxNormalizationAlgorithm.currentIndex()
        norm_alog = self.system.parameters_data.normalization_algorithms[ind]

        apply_remove_mask = self.ui.checkSelectBest.isChecked()
        wp = WaitPopup(self.system)

        try:
            wp.start()
            res = explib.full_analyze(df_ref, df_target, models, remove_rep, sample_rep, stat_mode, confidence, df_ref_norm, norm_alog)

        except:
            import traceback
            print(traceback.format_exc())
            res = None
            helpers.popup("Run ERROR", "Error occured during analyze step,\npleas double check you input data", "critical")

        wp.calculation_finished()

        if res is not None:
            self.system.results_data.set_results(res, apply_remove_mask)

        else:
            self.system.results_data.clear()

    def export_results(self):
        export_dfs = self.system.results_data.get_all_df()
        if export_dfs is None:
            return None

        filename, filter = QFileDialog.getSaveFileName(
            parent=self, caption='Select result file', dir='.',
            filter='Microsoft Excel 2007-2013 XML (*.xlsx)')

        if filename == "":
            return None

        if filename.split(".")[-1] != "xlsx":
            filename = filename + ".xlsx"
        explib.full_excel_export(filename, export_dfs)

    def export_graphs(self):
        export_dfs = self.system.results_data.get_all_df()
        if export_dfs is None:
            return

        dir_name = QFileDialog.getExistingDirectory(
            parent=self.system.mainWindowApp,
            caption='Select directory to save generated graphs',
            dir='.')

        if dir_name == "":
            return None

        RQ_df = export_dfs[2]
        stat_df = export_dfs[3]

        wp = WaitPopup(self.system)
        wp.start()
        explib.create_boxplots(RQ_df, stat_df, dir_name)
        try:
            pass
        except Exception as e:
            helpers.popup("Graph export ERROR", "Error occured during graph export", 'critical')
            print(e)

        wp.calculation_finished()


    def update_gui(self):
        input_valid = self.system.input_valid()
        if input_valid:
            self.ui.buttonShowRef.setEnabled(True)
            self.ui.buttonShowTarget.setEnabled(True)
            self.ui.buttonShowModels.setEnabled(True)
        else:
            self.ui.buttonShowRef.setEnabled(False)
            self.ui.buttonShowTarget.setEnabled(False)
            self.ui.buttonShowModels.setEnabled(False)
            self.ui.buttonShowQuantitive.setEnabled(False)
            self.ui.labelQantitive.setText("Not loaded")

        quanta_valid = self.system.quantitive_data.is_valid()
        if quanta_valid:
            self.ui.buttonShowQuantitive.setEnabled(True)
            self.ui.buttonRemoveQuantitive.setEnabled(True)
            self.ui.labelQantitive.setText("Loaded!")
        else:
            self.ui.buttonRemoveQuantitive.setEnabled(False)

        parameters_valid = self.system.parameters_data.is_valid()

        if (input_valid and parameters_valid):
            self.ui.buttonRunCalculations.setEnabled(True)
        else:
            self.ui.buttonRunCalculations.setEnabled(False)

        results_valid = self.system.results_data.is_valid()

        if results_valid:
            self.ui.groupBoxResultsSummary.setEnabled(True)
            #self.ui.labelCoherenceScore.setText("{0:.3f}".format(self.system.results_data.get_summary_coherence()))
            self.coherence_score_model.setCoherence(self.system.results_data.df_coherence)

        else:
            self.ui.groupBoxResultsSummary.setEnabled(False)
