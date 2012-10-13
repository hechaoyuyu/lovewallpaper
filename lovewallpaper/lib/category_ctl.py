# -*- coding: utf-8 -*-
from PySide import QtCore
from PySide import QtGui
from PySide.QtCore import Qt
from jsonman import Category, JsonMan
from wapper import CategoryWrapper



class CategoryController(QtCore.QObject):
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
    def thingSelected(self, tid, name, bgimage, url):
        my_choose_category = CategoryWrapper(Category(tid, name, bgimage, url))

        self.my_choose_clounm = self.window.My_JsonMan.getClounm(my_choose_category.url)

        self.window.ColunmView.setClounm(self.my_choose_clounm)


        self.window.ColunmView.NavLayout.setCurrentWidget(self.window.ColunmView.view)
        self.window.MasterContainerLayout.setCurrentWidget(self.window.ColunmView)


        




