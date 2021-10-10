# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(794, 778)
        self.actionRead_from_combined_input = QAction(MainWindow)
        self.actionRead_from_combined_input.setObjectName(u"actionRead_from_combined_input")
        self.actionLoad_Quantified = QAction(MainWindow)
        self.actionLoad_Quantified.setObjectName(u"actionLoad_Quantified")
        self.actionActivate_license = QAction(MainWindow)
        self.actionActivate_license.setObjectName(u"actionActivate_license")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 774, 715))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonShowQuantitive = QPushButton(self.groupBox)
        self.buttonShowQuantitive.setObjectName(u"buttonShowQuantitive")

        self.gridLayout.addWidget(self.buttonShowQuantitive, 5, 3, 1, 1)

        self.buttonShowRef = QPushButton(self.groupBox)
        self.buttonShowRef.setObjectName(u"buttonShowRef")

        self.gridLayout.addWidget(self.buttonShowRef, 0, 3, 1, 1)

        self.labelModelsCnt = QLabel(self.groupBox)
        self.labelModelsCnt.setObjectName(u"labelModelsCnt")

        self.gridLayout.addWidget(self.labelModelsCnt, 3, 1, 1, 1)

        self.labelTargetCnt = QLabel(self.groupBox)
        self.labelTargetCnt.setObjectName(u"labelTargetCnt")

        self.gridLayout.addWidget(self.labelTargetCnt, 1, 1, 1, 1)

        self.buttonShowTarget = QPushButton(self.groupBox)
        self.buttonShowTarget.setObjectName(u"buttonShowTarget")

        self.gridLayout.addWidget(self.buttonShowTarget, 1, 3, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.labelRefCnt = QLabel(self.groupBox)
        self.labelRefCnt.setObjectName(u"labelRefCnt")

        self.gridLayout.addWidget(self.labelRefCnt, 0, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.buttonShowModels = QPushButton(self.groupBox)
        self.buttonShowModels.setObjectName(u"buttonShowModels")

        self.gridLayout.addWidget(self.buttonShowModels, 3, 3, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setMouseTracking(False)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.labelQantitive = QLabel(self.groupBox)
        self.labelQantitive.setObjectName(u"labelQantitive")

        self.horizontalLayout_6.addWidget(self.labelQantitive)

        self.buttonRemoveQuantitive = QPushButton(self.groupBox)
        self.buttonRemoveQuantitive.setObjectName(u"buttonRemoveQuantitive")

        self.horizontalLayout_6.addWidget(self.buttonRemoveQuantitive)

        self.horizontalSpacer_9 = QSpacerItem(30, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_9)


        self.gridLayout.addLayout(self.horizontalLayout_6, 5, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_4.addWidget(self.label_8)

        self.comboBoxNormalizationAlgorithm = QComboBox(self.groupBox_2)
        self.comboBoxNormalizationAlgorithm.addItem("")
        self.comboBoxNormalizationAlgorithm.setObjectName(u"comboBoxNormalizationAlgorithm")
        self.comboBoxNormalizationAlgorithm.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_4.addWidget(self.comboBoxNormalizationAlgorithm)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.comboBoxStatModel = QComboBox(self.groupBox_2)
        self.comboBoxStatModel.addItem("")
        self.comboBoxStatModel.setObjectName(u"comboBoxStatModel")
        self.comboBoxStatModel.setMinimumSize(QSize(150, 0))

        self.horizontalLayout.addWidget(self.comboBoxStatModel)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout.addWidget(self.label_6)

        self.lineEditConfidence = QLineEdit(self.groupBox_2)
        self.lineEditConfidence.setObjectName(u"lineEditConfidence")
        self.lineEditConfidence.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout.addWidget(self.lineEditConfidence)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_2.addWidget(self.label_7)

        self.lineEditRemoveRep = QLineEdit(self.groupBox_2)
        self.lineEditRemoveRep.setObjectName(u"lineEditRemoveRep")
        self.lineEditRemoveRep.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_2.addWidget(self.lineEditRemoveRep)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.checkSelectBest = QCheckBox(self.groupBox_2)
        self.checkSelectBest.setObjectName(u"checkSelectBest")
        self.checkSelectBest.setEnabled(True)

        self.horizontalLayout_3.addWidget(self.checkSelectBest)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.widget = QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 60))
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(133, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.buttonRunCalculations = QPushButton(self.widget)
        self.buttonRunCalculations.setObjectName(u"buttonRunCalculations")
        self.buttonRunCalculations.setMinimumSize(QSize(200, 40))

        self.gridLayout_2.addWidget(self.buttonRunCalculations, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(134, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 110, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 12, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 2, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.widget)

        self.groupBoxResultsSummary = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBoxResultsSummary.setObjectName(u"groupBoxResultsSummary")
        self.groupBoxResultsSummary.setEnabled(True)
        self.gridLayout_3 = QGridLayout(self.groupBoxResultsSummary)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_17 = QLabel(self.groupBoxResultsSummary)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_3.addWidget(self.label_17, 0, 1, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)

        self.buttonExportResults = QPushButton(self.groupBoxResultsSummary)
        self.buttonExportResults.setObjectName(u"buttonExportResults")
        self.buttonExportResults.setMinimumSize(QSize(200, 40))

        self.horizontalLayout_5.addWidget(self.buttonExportResults)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.buttonExportGraphs = QPushButton(self.groupBoxResultsSummary)
        self.buttonExportGraphs.setObjectName(u"buttonExportGraphs")
        self.buttonExportGraphs.setEnabled(True)
        self.buttonExportGraphs.setMinimumSize(QSize(200, 40))

        self.horizontalLayout_5.addWidget(self.buttonExportGraphs)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)


        self.gridLayout_3.addLayout(self.horizontalLayout_5, 9, 1, 1, 2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.buttonShowBestRef = QPushButton(self.groupBoxResultsSummary)
        self.buttonShowBestRef.setObjectName(u"buttonShowBestRef")

        self.verticalLayout_4.addWidget(self.buttonShowBestRef)

        self.buttonShowRQ = QPushButton(self.groupBoxResultsSummary)
        self.buttonShowRQ.setObjectName(u"buttonShowRQ")

        self.verticalLayout_4.addWidget(self.buttonShowRQ)

        self.buttonShowStatistic = QPushButton(self.groupBoxResultsSummary)
        self.buttonShowStatistic.setObjectName(u"buttonShowStatistic")

        self.verticalLayout_4.addWidget(self.buttonShowStatistic)


        self.gridLayout_3.addLayout(self.verticalLayout_4, 4, 2, 5, 1)

        self.listCoherence = QListView(self.groupBoxResultsSummary)
        self.listCoherence.setObjectName(u"listCoherence")
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.listCoherence.setFont(font)
        self.listCoherence.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listCoherence.setSelectionMode(QAbstractItemView.NoSelection)

        self.gridLayout_3.addWidget(self.listCoherence, 4, 1, 5, 1)


        self.verticalLayout_3.addWidget(self.groupBoxResultsSummary)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 794, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionRead_from_combined_input)
        self.menuFile.addAction(self.actionLoad_Quantified)
        self.menuFile.addSeparator()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionRead_from_combined_input.setText(QCoreApplication.translate("MainWindow", u"Read from combined input", None))
        self.actionLoad_Quantified.setText(QCoreApplication.translate("MainWindow", u"Load Quantified", None))
        self.actionActivate_license.setText(QCoreApplication.translate("MainWindow", u"Activate license", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Input data", None))
        self.buttonShowQuantitive.setText(QCoreApplication.translate("MainWindow", u"Show Table", None))
#if QT_CONFIG(tooltip)
        self.buttonShowRef.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.buttonShowRef.setText(QCoreApplication.translate("MainWindow", u"Show Table", None))
#if QT_CONFIG(tooltip)
        self.labelModelsCnt.setToolTip(QCoreApplication.translate("MainWindow", u"Cell models count", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.labelModelsCnt.setStatusTip(QCoreApplication.translate("MainWindow", u"Cell models count", None))
#endif // QT_CONFIG(statustip)
        self.labelModelsCnt.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(tooltip)
        self.labelTargetCnt.setToolTip(QCoreApplication.translate("MainWindow", u"Loaded target genes count", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.labelTargetCnt.setStatusTip(QCoreApplication.translate("MainWindow", u"Loaded target genes count", None))
#endif // QT_CONFIG(statustip)
        self.labelTargetCnt.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.buttonShowTarget.setText(QCoreApplication.translate("MainWindow", u"Show Table", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("MainWindow", u"Table of target genes loaded into the program", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_2.setStatusTip(QCoreApplication.translate("MainWindow", u" Table of target genes loaded into the program", None))
#endif // QT_CONFIG(statustip)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Target genes:", None))
#if QT_CONFIG(tooltip)
        self.labelRefCnt.setToolTip(QCoreApplication.translate("MainWindow", u"Loaded reference genes cout", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.labelRefCnt.setStatusTip(QCoreApplication.translate("MainWindow", u"Loaded reference genes cout", None))
#endif // QT_CONFIG(statustip)
        self.labelRefCnt.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("MainWindow", u"A current list of cell line models", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_3.setStatusTip(QCoreApplication.translate("MainWindow", u"A current list of cell line models", None))
#endif // QT_CONFIG(statustip)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Line models:", None))
        self.buttonShowModels.setText(QCoreApplication.translate("MainWindow", u"Show List", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("MainWindow", u"Table of reference genes loaded into the program", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label.setStatusTip(QCoreApplication.translate("MainWindow", u"Table of reference genes loaded into the program", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.label.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.label.setText(QCoreApplication.translate("MainWindow", u"Reference gens:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Quantitive data:", None))
        self.labelQantitive.setText(QCoreApplication.translate("MainWindow", u"Not loaded", None))
        self.buttonRemoveQuantitive.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Parameters", None))
#if QT_CONFIG(tooltip)
        self.label_8.setToolTip(QCoreApplication.translate("MainWindow", u"Select normalization algorithm to use during analysis ", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_8.setStatusTip(QCoreApplication.translate("MainWindow", u"Select normalization algorithm to use during analysis ", None))
#endif // QT_CONFIG(statustip)
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Normalization algorithm", None))
        self.comboBoxNormalizationAlgorithm.setItemText(0, QCoreApplication.translate("MainWindow", u"Normfinder", None))

#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("MainWindow", u"Select statistical model to use during analysis ", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_5.setStatusTip(QCoreApplication.translate("MainWindow", u"Select statistical model to use during analysis ", None))
#endif // QT_CONFIG(statustip)
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Statistical model:", None))
        self.comboBoxStatModel.setItemText(0, QCoreApplication.translate("MainWindow", u"Student", None))

#if QT_CONFIG(tooltip)
        self.label_6.setToolTip(QCoreApplication.translate("MainWindow", u"Select p-value", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_6.setStatusTip(QCoreApplication.translate("MainWindow", u"Select p-value", None))
#endif // QT_CONFIG(statustip)
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"confidence:", None))
        self.lineEditConfidence.setText(QCoreApplication.translate("MainWindow", u"0.05", None))
#if QT_CONFIG(tooltip)
        self.label_7.setToolTip(QCoreApplication.translate("MainWindow", u"Select number of remove worst reference gene cycles", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_7.setStatusTip(QCoreApplication.translate("MainWindow", u"Select number of remove worst reference gene cycles", None))
#endif // QT_CONFIG(statustip)
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Remove repetitions:", None))
        self.lineEditRemoveRep.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.checkSelectBest.setText(QCoreApplication.translate("MainWindow", u"Select best remove for model", None))
        self.buttonRunCalculations.setText(QCoreApplication.translate("MainWindow", u"Run calculations", None))
        self.groupBoxResultsSummary.setTitle(QCoreApplication.translate("MainWindow", u"Results summary", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Coherence score list", None))
        self.buttonExportResults.setText(QCoreApplication.translate("MainWindow", u"Export results", None))
        self.buttonExportGraphs.setText(QCoreApplication.translate("MainWindow", u"Export graphs", None))
        self.buttonShowBestRef.setText(QCoreApplication.translate("MainWindow", u"Show best references", None))
        self.buttonShowRQ.setText(QCoreApplication.translate("MainWindow", u"Show RQ values", None))
        self.buttonShowStatistic.setText(QCoreApplication.translate("MainWindow", u"Show p-values", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

