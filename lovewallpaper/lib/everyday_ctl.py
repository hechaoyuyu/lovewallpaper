# -*- coding: utf-8 -*-
from PySide import QtCore
from PySide import QtGui
from PySide.QtCore import Qt
from wapper import EverydayWrapper
from jsonman import Everyday 



class EverydayController(QtCore.QObject):
    # ratepage_maker = QtCore.Signal()
    # tryluckpage_maker = QtCore.Signal()
    # clean_model = QtCore.Signal()

    def __init__(self,window):
        QtCore.QObject.__init__(self)
        self.window = window

    @QtCore.Slot(str)
    def NavClicked(self, click):
        print click
        if click == "Special":
            self.window.Special_btn_clicked()
        elif click == "Top":
            self.window.Top_btn_clicked()
        elif click == "Everyday":
            self.window.everyday_clicked()
        elif click == "Category":
            self.window.category_clicked()

    @QtCore.Slot(str, str, str, str)
    def thingSelected(self, image, name, total, url):
        my_choose_day = EverydayWrapper(Everyday(image, name, url, total))
        self.my_choose_day = self.window.My_JsonMan.getEveryday(my_choose_day.url)
        self.window.category_imagelistview.controller.setList(self.my_choose_day.data,self.window.category_imagelistview.rc)
        self.window.category_imagelistview.controller.setLinks(self.my_choose_day.link)
        self.window.category_imagelistview.setTitle(name)
        self.window.MasterContainerLayout.setCurrentWidget(self.window.category_imagelistview)