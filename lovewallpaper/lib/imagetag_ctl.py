# -*- coding: utf-8 -*-
from PySide import QtCore
from PySide import QtGui
from PySide.QtCore import Qt
from jsonman import ImageTag, JsonMan
from wapper import ImageTagWrapper



class ImageTagController(QtCore.QObject):
    # ratepage_maker = QtCore.Signal()
    # tryluckpage_maker = QtCore.Signal()
    # clean_model = QtCore.Signal()

    def __init__(self,window):
        QtCore.QObject.__init__(self)
        self.window = window

    @QtCore.Slot(str,str,str)
    def thingSelected(self, image, name, url):
        my_choose_category = ImageTagWrapper(ImageTag( image, name, url))

        self.my_choose_clounm = self.window.My_JsonMan.getClounm(my_choose_category.url)

        self.window.ColunmView_2nd.setClounm(self.my_choose_clounm)


        self.window.ColunmView_2nd.NavLayout.setCurrentWidget(self.window.ColunmView_2nd.view)
        self.window.MasterContainerLayout.setCurrentWidget(self.window.ColunmView_2nd)


        




