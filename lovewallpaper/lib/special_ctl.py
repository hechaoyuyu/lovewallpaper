# -*- coding: utf-8 -*-
from PySide import QtCore
from PySide import QtGui
from PySide.QtCore import Qt
from jsonman import Special, JsonMan
from wapper import SpecialWrapper



class SpecialController(QtCore.QObject):
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

    @QtCore.Slot(str,str,str,str)
    def thingSelected(self, name, description, image, detail):
        my_choose_special = SpecialWrapper(Special(name, description, image, detail))
        self.my_choose_special_back = self.window.My_JsonMan.getSpecial(my_choose_special.detail)
        self.window.category_imagelistview.controller.setList(self.my_choose_special_back.data, self.window.category_imagelistview.rc)
        self.window.category_imagelistview.controller.setLinks("")
        self.window.category_imagelistview.setTitle(name)
        self.window.MasterContainerLayout.setCurrentWidget(self.window.category_imagelistview)

        




