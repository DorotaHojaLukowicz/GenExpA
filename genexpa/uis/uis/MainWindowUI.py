# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui',
# licensing of 'MainWindow.ui' applies.
#
# Created: Fri Dec  4 11:26:59 2020
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(794, 879)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 774, 810))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonShowQuantitive = QtWidgets.QPushButton(self.groupBox)
        self.buttonShowQuantitive.setObjectName("buttonShowQuantitive")
        self.gridLayout.addWidget(self.buttonShowQuantitive, 5, 3, 1, 1)
        self.buttonShowRef = QtWidgets.QPushButton(self.groupBox)
        self.buttonShowRef.setToolTip("")
        self.buttonShowRef.setObjectName("buttonShowRef")
        self.gridLayout.addWidget(self.buttonShowRef, 0, 3, 1, 1)
        self.labelModelsCnt = QtWidgets.QLabel(self.groupBox)
        self.labelModelsCnt.setObjectName("labelModelsCnt")
        self.gridLayout.addWidget(self.labelModelsCnt, 3, 1, 1, 1)
        self.labelTargetCnt = QtWidgets.QLabel(self.groupBox)
        self.labelTargetCnt.setObjectName("labelTargetCnt")
        self.gridLayout.addWidget(self.labelTargetCnt, 1, 1, 1, 1)
        self.buttonShowTarget = QtWidgets.QPushButton(self.groupBox)
        self.buttonShowTarget.setObjectName("buttonShowTarget")
        self.gridLayout.addWidget(self.buttonShowTarget, 1, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.labelRefCnt = QtWidgets.QLabel(self.groupBox)
        self.labelRefCnt.setObjectName("labelRefCnt")
        self.gridLayout.addWidget(self.labelRefCnt, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.buttonShowModels = QtWidgets.QPushButton(self.groupBox)
        self.buttonShowModels.setObjectName("buttonShowModels")
        self.gridLayout.addWidget(self.buttonShowModels, 3, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setMouseTracking(False)
        self.label.setWhatsThis("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.labelQantitive = QtWidgets.QLabel(self.groupBox)
        self.labelQantitive.setObjectName("labelQantitive")
        self.horizontalLayout_6.addWidget(self.labelQantitive)
        self.buttonRemoveQuantitive = QtWidgets.QPushButton(self.groupBox)
        self.buttonRemoveQuantitive.setObjectName("buttonRemoveQuantitive")
        self.horizontalLayout_6.addWidget(self.buttonRemoveQuantitive)
        spacerItem = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_6, 5, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.comboBoxNormalizationAlgorithm = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBoxNormalizationAlgorithm.setMinimumSize(QtCore.QSize(150, 0))
        self.comboBoxNormalizationAlgorithm.setObjectName("comboBoxNormalizationAlgorithm")
        self.comboBoxNormalizationAlgorithm.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBoxNormalizationAlgorithm)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.comboBoxStatModel = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBoxStatModel.setMinimumSize(QtCore.QSize(150, 0))
        self.comboBoxStatModel.setObjectName("comboBoxStatModel")
        self.comboBoxStatModel.addItem("")
        self.horizontalLayout.addWidget(self.comboBoxStatModel)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.lineEditConfidence = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEditConfidence.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEditConfidence.setObjectName("lineEditConfidence")
        self.horizontalLayout.addWidget(self.lineEditConfidence)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.lineEditRemoveRep = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEditRemoveRep.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lineEditRemoveRep.setObjectName("lineEditRemoveRep")
        self.horizontalLayout_2.addWidget(self.lineEditRemoveRep)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9)
        self.lineEditSampleRepetition = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEditSampleRepetition.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lineEditSampleRepetition.setObjectName("lineEditSampleRepetition")
        self.horizontalLayout_7.addWidget(self.lineEditSampleRepetition)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkSelectBest = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkSelectBest.setEnabled(True)
        self.checkSelectBest.setObjectName("checkSelectBest")
        self.horizontalLayout_3.addWidget(self.checkSelectBest)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 60))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(133, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 1, 2, 1, 1)
        self.buttonRunCalculations = QtWidgets.QPushButton(self.widget)
        self.buttonRunCalculations.setMinimumSize(QtCore.QSize(200, 40))
        self.buttonRunCalculations.setObjectName("buttonRunCalculations")
        self.gridLayout_2.addWidget(self.buttonRunCalculations, 1, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(134, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 1, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 110, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem6, 0, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 12, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem7, 2, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.widget)
        self.groupBoxResultsSummary = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBoxResultsSummary.setEnabled(True)
        self.groupBoxResultsSummary.setObjectName("groupBoxResultsSummary")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBoxResultsSummary)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_17 = QtWidgets.QLabel(self.groupBoxResultsSummary)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 0, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.buttonExportResults = QtWidgets.QPushButton(self.groupBoxResultsSummary)
        self.buttonExportResults.setMinimumSize(QtCore.QSize(200, 40))
        self.buttonExportResults.setObjectName("buttonExportResults")
        self.horizontalLayout_5.addWidget(self.buttonExportResults)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.buttonExportGraphs = QtWidgets.QPushButton(self.groupBoxResultsSummary)
        self.buttonExportGraphs.setEnabled(True)
        self.buttonExportGraphs.setMinimumSize(QtCore.QSize(200, 40))
        self.buttonExportGraphs.setObjectName("buttonExportGraphs")
        self.horizontalLayout_5.addWidget(self.buttonExportGraphs)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 9, 1, 1, 2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem11)
        self.buttonShowBestRef = QtWidgets.QPushButton(self.groupBoxResultsSummary)
        self.buttonShowBestRef.setObjectName("buttonShowBestRef")
        self.verticalLayout_4.addWidget(self.buttonShowBestRef)
        self.buttonShowRQ = QtWidgets.QPushButton(self.groupBoxResultsSummary)
        self.buttonShowRQ.setObjectName("buttonShowRQ")
        self.verticalLayout_4.addWidget(self.buttonShowRQ)
        self.buttonShowStatistic = QtWidgets.QPushButton(self.groupBoxResultsSummary)
        self.buttonShowStatistic.setObjectName("buttonShowStatistic")
        self.verticalLayout_4.addWidget(self.buttonShowStatistic)
        self.gridLayout_3.addLayout(self.verticalLayout_4, 4, 2, 5, 1)
        self.listCoherence = QtWidgets.QListView(self.groupBoxResultsSummary)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.listCoherence.setFont(font)
        self.listCoherence.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listCoherence.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.listCoherence.setObjectName("listCoherence")
        self.gridLayout_3.addWidget(self.listCoherence, 4, 1, 5, 1)
        self.verticalLayout_3.addWidget(self.groupBoxResultsSummary)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 27))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionRead_from_combined_input = QtWidgets.QAction(MainWindow)
        self.actionRead_from_combined_input.setObjectName("actionRead_from_combined_input")
        self.actionLoad_Quantified = QtWidgets.QAction(MainWindow)
        self.actionLoad_Quantified.setObjectName("actionLoad_Quantified")
        self.actionActivate_license = QtWidgets.QAction(MainWindow)
        self.actionActivate_license.setObjectName("actionActivate_license")
        self.menuFile.addAction(self.actionRead_from_combined_input)
        self.menuFile.addAction(self.actionLoad_Quantified)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionActivate_license)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("MainWindow", "Input data", None, -1))
        self.buttonShowQuantitive.setText(QtWidgets.QApplication.translate("MainWindow", "Show Table", None, -1))
        self.buttonShowRef.setText(QtWidgets.QApplication.translate("MainWindow", "Show Table", None, -1))
        self.labelModelsCnt.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Cell models count", None, -1))
        self.labelModelsCnt.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Cell models count", None, -1))
        self.labelModelsCnt.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.labelTargetCnt.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Loaded target genes count", None, -1))
        self.labelTargetCnt.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Loaded target genes count", None, -1))
        self.labelTargetCnt.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.buttonShowTarget.setText(QtWidgets.QApplication.translate("MainWindow", "Show Table", None, -1))
        self.label_2.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Table of target genes loaded into the program", None, -1))
        self.label_2.setStatusTip(QtWidgets.QApplication.translate("MainWindow", " Table of target genes loaded into the program", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Target genes:", None, -1))
        self.labelRefCnt.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Loaded reference genes cout", None, -1))
        self.labelRefCnt.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Loaded reference genes cout", None, -1))
        self.labelRefCnt.setText(QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.label_3.setToolTip(QtWidgets.QApplication.translate("MainWindow", "A current list of cell line models", None, -1))
        self.label_3.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "A current list of cell line models", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "Line models:", None, -1))
        self.buttonShowModels.setText(QtWidgets.QApplication.translate("MainWindow", "Show List", None, -1))
        self.label.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Table of reference genes loaded into the program", None, -1))
        self.label.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Table of reference genes loaded into the program", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Reference gens:", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "Quantitive data:", None, -1))
        self.labelQantitive.setText(QtWidgets.QApplication.translate("MainWindow", "Not loaded", None, -1))
        self.buttonRemoveQuantitive.setText(QtWidgets.QApplication.translate("MainWindow", "Remove", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("MainWindow", "Parameters", None, -1))
        self.label_8.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Select normalization algorithm to use during analysis ", None, -1))
        self.label_8.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Select normalization algorithm to use during analysis ", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("MainWindow", "Normalization algorithm", None, -1))
        self.comboBoxNormalizationAlgorithm.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "Normfinder", None, -1))
        self.label_5.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Select statistical model to use during analysis ", None, -1))
        self.label_5.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Select statistical model to use during analysis ", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("MainWindow", "Statistical model:", None, -1))
        self.comboBoxStatModel.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "Student", None, -1))
        self.label_6.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Select p-value", None, -1))
        self.label_6.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Select p-value", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("MainWindow", "confidence:", None, -1))
        self.lineEditConfidence.setText(QtWidgets.QApplication.translate("MainWindow", "0.05", None, -1))
        self.label_7.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Select number of remove worst reference gene cycles", None, -1))
        self.label_7.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Select number of remove worst reference gene cycles", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("MainWindow", "Remove repetitions:", None, -1))
        self.lineEditRemoveRep.setText(QtWidgets.QApplication.translate("MainWindow", "2", None, -1))
        self.label_9.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Select check repetition for a single sample", None, -1))
        self.label_9.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Select check repetition for a single sample", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("MainWindow", "Single sample repetition", None, -1))
        self.lineEditSampleRepetition.setText(QtWidgets.QApplication.translate("MainWindow", "3", None, -1))
        self.checkSelectBest.setText(QtWidgets.QApplication.translate("MainWindow", "Select best remove for model", None, -1))
        self.buttonRunCalculations.setText(QtWidgets.QApplication.translate("MainWindow", "Run calculations", None, -1))
        self.groupBoxResultsSummary.setTitle(QtWidgets.QApplication.translate("MainWindow", "Results summary", None, -1))
        self.label_17.setText(QtWidgets.QApplication.translate("MainWindow", "Coherence score list", None, -1))
        self.buttonExportResults.setText(QtWidgets.QApplication.translate("MainWindow", "Export results", None, -1))
        self.buttonExportGraphs.setText(QtWidgets.QApplication.translate("MainWindow", "Export graphs", None, -1))
        self.buttonShowBestRef.setText(QtWidgets.QApplication.translate("MainWindow", "Show best references", None, -1))
        self.buttonShowRQ.setText(QtWidgets.QApplication.translate("MainWindow", "Show RQ values", None, -1))
        self.buttonShowStatistic.setText(QtWidgets.QApplication.translate("MainWindow", "Show p-values", None, -1))
        self.menuFile.setTitle(QtWidgets.QApplication.translate("MainWindow", "File", None, -1))
        self.actionRead_from_combined_input.setText(QtWidgets.QApplication.translate("MainWindow", "Read from combined input", None, -1))
        self.actionLoad_Quantified.setText(QtWidgets.QApplication.translate("MainWindow", "Load Quantified", None, -1))
        self.actionActivate_license.setText(QtWidgets.QApplication.translate("MainWindow", "Activate license", None, -1))

