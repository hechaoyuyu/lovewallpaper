# -*- coding: utf-8 -*-
from PySide.QtCore import *
from PySide.QtGui import *
from lib.newversion import Ui_NewVer
import os


class NewVer(QDialog,Ui_NewVer):
    """docstring for SettingUI"""
    def __init__(self, parent = None,version=None,detail=None):
        super(NewVer, self).__init__(parent)
        self.setupUi(self)
        self.versionLabel.setText(version)
        self.detailLabel.setText(detail)
        self.exec_()
    
    def accept(self):
        os.system("xdg-open http://www.lovebizhi.com/linux.html")
        self.close()
