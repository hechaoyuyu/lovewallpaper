# -*- coding: utf-8 -*-
from PySide.QtCore import *
from PySide.QtGui import *
from lib.settings import Ui_Settings
import ConfigParser
import os
from lib.manager import Manager
from jsonman import JsonMan
from lib.VERSION import __VERSION__
try:
    import pynotify
except:
    print "No model"

#Define the ListModel
class DataModel (QAbstractListModel):
    """docstring for ClassName"""
    def __init__(self, plugins):
        QAbstractListModel.__init__(self)
        self.plugins = plugins
        self.setRoleNames({0: 'plugin'})

    def rowCount(self, parent=QModelIndex()):
        return len(self.plugins)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            if not index.isValid():
                return None
            elif index.row() > len(self.plugins):
                return None
            else:
                return self.plugins[index.row()].decode('utf-8')

#Define the Settings UI from the QtDesigner gen. SettingsUI
class SettingUI(QWidget, Ui_Settings):
    """docstring for SettingUI"""
    def __init__( self , parent = None ):
        super( SettingUI , self ).__init__(parent)
        try:
            pynotify.init("LoveWallpaperHD")
        except:
            print "done"
        self.setupUi(self)

        self.setStyleSheet("QToolBar {background-color:#b60400; border-bottom:2px solid #b60400}")

        self.usr_home = os.path.expanduser('~') + "/.config/lovewallpaper"

        self.label_16.setText(QApplication.translate("Settings", "<html><head/><body><p>版本:<span style=\" font-weight:600;\">" + __VERSION__ + "</span></p></body></html>", None, QApplication.UnicodeUTF8))

        self.cf = ConfigParser.ConfigParser()

        self.cf.read("%s/config" % (self.usr_home))

        self.chooseButton.clicked.connect(self.setPath)

        self.postUpButton.clicked.connect(self.postfeedback)

        self.feedbackTextEdit.textChanged.connect(self.limittext)

        self.manager = Manager()

        if self.cf.get("Slide", "slide") == 0:
            self.autoslide_checkbox.setCheckState(Qt.Unchecked)
        else:
            self.autoslide_checkbox.setCheckState(Qt.Checked)

        self.autoslide_checkbox.stateChanged.connect(self.beginslide)

        self.time_spinbox.valueChanged.connect(self.setTime)

        self.time_spinbox.setValue(int(self.cf.get("Slide", "freeze")))

        text = self.cf.get("Path", "download")

        self.path_line.setText(text.decode('utf-8'))

        self.platform_list = ["GnomeShell", "KDE", "XFCE", "Mac", "Gnome", "MATE", "LXDE"]

        self.platform_model = DataModel(self.platform_list)

        self.paltformlistView.setModel(self.platform_model)

        self.paltformlistView.clicked.connect(self.selectPaltForm)

    def selectPaltForm(self, indexes):
        platform = self.platform_list[indexes.row()]
        self.cf.set("Config", "platform", platform)
        self.cf.write(open("%s/config" % (self.usr_home), "w"))
        try:
            n = pynotify.Notification("爱壁纸HD", "好啦，我已经记住了的桌面环境")
            n.show()
        except:
            print "False"

    def limittext(self):
        if len(self.feedbackTextEdit.toPlainText()) < 500:

            self.limitLabel.setText(str(500 - len(self.feedbackTextEdit.toPlainText())))
        else:
            self.feedbackTextEdit.undo()

    def postfeedback(self):
        self.jsonman = JsonMan()
        if len(self.feedbackTextEdit.toPlainText()) < 500:

            text = self.feedbackTextEdit.toPlainText()
            userinfo = self.userinfolineEdit.text()
            self.jsonman.sendFeedBack(text,userinfo)
        else:

            print "post",text,userinfo,"toomuch"

    def setTime(self, value):
        self.cf.set("Slide", "freeze", value)
        self.cf.write(open("%s/config"%(self.usr_home), "w"))

    def beginslide(self,par):
        self.cf.read("%s/config"%(self.usr_home))

        if par == 0:
            self.cf.set("Slide", "slide", 0)
            self.cf.write(open("%s/config" % (self.usr_home), "w"))
            self.manager.AutoSlider.RandomSet(self.manager.prepareFiles())
        else:
            self.cf.set("Slide", "slide", 1)
            self.cf.write(open("%s/config" % (self.usr_home), "w"))
            self.manager.AutoSlider.BeginSlide(self.manager.prepareFiles(), int(self.cf.get( "Slide", "freeze" ) ) )

    def setPath(self):
        fileName = QFileDialog.getExistingDirectory(self)
        self.path_line.setText(fileName)
        self.cf.set("Path", "download", fileName + '/')
        print "set" + fileName
        self.cf.write(open("%s/config" % (self.usr_home), "w"))
