# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newversion.ui'
#
# Created: Thu Aug 23 19:06:31 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_NewVer(object):
    def setupUi(self, NewVer):
        NewVer.setObjectName("NewVer")
        NewVer.resize(400, 300)
        self.gridLayout_2 = QtGui.QGridLayout(NewVer)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.versionLabel = QtGui.QLabel(NewVer)
        self.versionLabel.setText("")
        self.versionLabel.setObjectName("versionLabel")
        self.gridLayout.addWidget(self.versionLabel, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(NewVer)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.detailLabel = QtGui.QLabel(NewVer)
        self.detailLabel.setMinimumSize(QtCore.QSize(0, 150))
        self.detailLabel.setObjectName("detailLabel")
        self.gridLayout.addWidget(self.detailLabel, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(NewVer)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(NewVer)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), NewVer.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), NewVer.reject)
        QtCore.QMetaObject.connectSlotsByName(NewVer)

    def retranslateUi(self, NewVer):
        NewVer.setWindowTitle(QtGui.QApplication.translate("NewVer", "有新版本了", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("NewVer", "更新内容：", None, QtGui.QApplication.UnicodeUTF8))
        self.detailLabel.setText(QtGui.QApplication.translate("NewVer", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

