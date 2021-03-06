# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ReadFromCombinedDialog.ui',
# licensing of 'ReadFromCombinedDialog.ui' applies.
#
# Created: Sat Jan  4 12:25:52 2020
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(860, 666)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBoxLoadFile = QtWidgets.QGroupBox(Dialog)
        self.groupBoxLoadFile.setMinimumSize(QtCore.QSize(0, 100))
        self.groupBoxLoadFile.setObjectName("groupBoxLoadFile")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBoxLoadFile)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBoxLoadFile)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.loadedFileText = QtWidgets.QLabel(self.groupBoxLoadFile)
        self.loadedFileText.setObjectName("loadedFileText")
        self.horizontalLayout.addWidget(self.loadedFileText)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableLoadedDF = QtWidgets.QTableView(self.groupBoxLoadFile)
        self.tableLoadedDF.setObjectName("tableLoadedDF")
        self.horizontalLayout_2.addWidget(self.tableLoadedDF)
        self.widget = QtWidgets.QWidget(self.groupBoxLoadFile)
        self.widget.setMinimumSize(QtCore.QSize(180, 0))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.buttonSelectFile = QtWidgets.QPushButton(self.widget)
        self.buttonSelectFile.setObjectName("buttonSelectFile")
        self.verticalLayout_2.addWidget(self.buttonSelectFile)
        self.horizontalLayout_2.addWidget(self.widget)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.groupBoxLoadFile)
        self.groupBoxSelectRef = QtWidgets.QGroupBox(Dialog)
        self.groupBoxSelectRef.setMinimumSize(QtCore.QSize(0, 100))
        self.groupBoxSelectRef.setObjectName("groupBoxSelectRef")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBoxSelectRef)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.groupBoxSelectRef)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.listAvailRef = QtWidgets.QListView(self.groupBoxSelectRef)
        self.listAvailRef.setObjectName("listAvailRef")
        self.verticalLayout_5.addWidget(self.listAvailRef)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.buttonSelectRef = QtWidgets.QPushButton(self.groupBoxSelectRef)
        self.buttonSelectRef.setObjectName("buttonSelectRef")
        self.verticalLayout_4.addWidget(self.buttonSelectRef)
        self.buttonUnSelectRef = QtWidgets.QPushButton(self.groupBoxSelectRef)
        self.buttonUnSelectRef.setObjectName("buttonUnSelectRef")
        self.verticalLayout_4.addWidget(self.buttonUnSelectRef)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.groupBoxSelectRef)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.listSelRef = QtWidgets.QListView(self.groupBoxSelectRef)
        self.listSelRef.setObjectName("listSelRef")
        self.verticalLayout_6.addWidget(self.listSelRef)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.verticalLayout.addWidget(self.groupBoxSelectRef)
        self.groupBoxSelectModels = QtWidgets.QGroupBox(Dialog)
        self.groupBoxSelectModels.setMinimumSize(QtCore.QSize(0, 100))
        self.groupBoxSelectModels.setObjectName("groupBoxSelectModels")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBoxSelectModels)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.groupBoxSelectModels)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.listCurrentModels = QtWidgets.QListView(self.groupBoxSelectModels)
        self.listCurrentModels.setObjectName("listCurrentModels")
        self.verticalLayout_7.addWidget(self.listCurrentModels)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)
        self.widget_2 = QtWidgets.QWidget(self.groupBoxSelectModels)
        self.widget_2.setMinimumSize(QtCore.QSize(180, 0))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.buttonAddSingle = QtWidgets.QPushButton(self.widget_2)
        self.buttonAddSingle.setObjectName("buttonAddSingle")
        self.verticalLayout_8.addWidget(self.buttonAddSingle)
        self.buttonGenerateComb = QtWidgets.QPushButton(self.widget_2)
        self.buttonGenerateComb.setObjectName("buttonGenerateComb")
        self.verticalLayout_8.addWidget(self.buttonGenerateComb)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem1)
        self.buttonDeleteModel = QtWidgets.QPushButton(self.widget_2)
        self.buttonDeleteModel.setObjectName("buttonDeleteModel")
        self.verticalLayout_8.addWidget(self.buttonDeleteModel)
        self.buttonRemoveAll = QtWidgets.QPushButton(self.widget_2)
        self.buttonRemoveAll.setObjectName("buttonRemoveAll")
        self.verticalLayout_8.addWidget(self.buttonRemoveAll)
        self.horizontalLayout_4.addWidget(self.widget_2)
        self.verticalLayout.addWidget(self.groupBoxSelectModels)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.buttonCancel = QtWidgets.QPushButton(Dialog)
        self.buttonCancel.setObjectName("buttonCancel")
        self.horizontalLayout_5.addWidget(self.buttonCancel)
        self.buttonAccept = QtWidgets.QPushButton(Dialog)
        self.buttonAccept.setObjectName("buttonAccept")
        self.horizontalLayout_5.addWidget(self.buttonAccept)
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Read from combined input", None, -1))
        self.groupBoxLoadFile.setTitle(QtWidgets.QApplication.translate("Dialog", "Load file", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Dialog", "Loaded file: ", None, -1))
        self.loadedFileText.setText(QtWidgets.QApplication.translate("Dialog", "None", None, -1))
        self.buttonSelectFile.setText(QtWidgets.QApplication.translate("Dialog", "Select file", None, -1))
        self.groupBoxSelectRef.setTitle(QtWidgets.QApplication.translate("Dialog", "Select reference genes", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Dialog", "Available reference genes", None, -1))
        self.buttonSelectRef.setText(QtWidgets.QApplication.translate("Dialog", "Select as ref->", None, -1))
        self.buttonUnSelectRef.setText(QtWidgets.QApplication.translate("Dialog", "<- Unselect", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Dialog", "Selected genes as reference", None, -1))
        self.groupBoxSelectModels.setTitle(QtWidgets.QApplication.translate("Dialog", "Select Models", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("Dialog", "Current models", None, -1))
        self.buttonAddSingle.setText(QtWidgets.QApplication.translate("Dialog", "Add single", None, -1))
        self.buttonGenerateComb.setText(QtWidgets.QApplication.translate("Dialog", "Generate combinations", None, -1))
        self.buttonDeleteModel.setText(QtWidgets.QApplication.translate("Dialog", "Delete model", None, -1))
        self.buttonRemoveAll.setText(QtWidgets.QApplication.translate("Dialog", "Remove all", None, -1))
        self.buttonCancel.setText(QtWidgets.QApplication.translate("Dialog", "Cancel", None, -1))
        self.buttonAccept.setText(QtWidgets.QApplication.translate("Dialog", "Accept", None, -1))

