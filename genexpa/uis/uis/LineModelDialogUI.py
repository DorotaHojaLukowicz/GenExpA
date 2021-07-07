# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LineModelDialog.ui',
# licensing of 'LineModelDialog.ui' applies.
#
# Created: Sat Jan  4 23:05:16 2020
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(375, 311)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listLines = QtWidgets.QListView(Dialog)
        self.listLines.setObjectName("listLines")
        self.horizontalLayout.addWidget(self.listLines)
        self.buttonAddLine = QtWidgets.QPushButton(Dialog)
        self.buttonAddLine.setObjectName("buttonAddLine")
        self.horizontalLayout.addWidget(self.buttonAddLine)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.labelModelText = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.labelModelText.setFont(font)
        self.labelModelText.setObjectName("labelModelText")
        self.horizontalLayout_2.addWidget(self.labelModelText)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.buttonDiscard = QtWidgets.QPushButton(Dialog)
        self.buttonDiscard.setObjectName("buttonDiscard")
        self.horizontalLayout_3.addWidget(self.buttonDiscard)
        self.buttonAccept = QtWidgets.QPushButton(Dialog)
        self.buttonAccept.setObjectName("buttonAccept")
        self.horizontalLayout_3.addWidget(self.buttonAccept)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Dialog", None, -1))
        self.buttonAddLine.setText(QtWidgets.QApplication.translate("Dialog", "Add line to model", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Dialog", "Selected model:", None, -1))
        self.labelModelText.setText(QtWidgets.QApplication.translate("Dialog", "-", None, -1))
        self.buttonDiscard.setText(QtWidgets.QApplication.translate("Dialog", "Discard", None, -1))
        self.buttonAccept.setText(QtWidgets.QApplication.translate("Dialog", "Accept", None, -1))

