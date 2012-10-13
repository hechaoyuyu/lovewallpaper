# -*- coding: utf-8 -*-
from PySide import QtCore
from PySide import QtGui
from PySide.QtCore import Qt
from jsonman import Category, JsonMan

class CategoryWrapper(QtCore.QObject):
    def __init__(self, category):
        QtCore.QObject.__init__(self)
        self._category = category
 
    def _tid(self):
        return str(self._category.tid)
    def _name(self):
        return self._category.name
    def _bgimage(self):
        return self._category.bgimage
    def _url(self):
        return self._category.url

 
    changed = QtCore.Signal()
 
    tid = QtCore.Property(unicode, _tid, notify=changed)
    name = QtCore.Property(unicode, _name, notify=changed)
    bgimage = QtCore.Property(unicode, _bgimage, notify=changed)
    url = QtCore.Property(unicode, _url, notify=changed)

class CategoryListModel(QtCore.QAbstractListModel):
    TID_ROLE = Qt.UserRole + 1
    NAME_ROLE = Qt.UserRole + 2
    bgimage_ROLE = Qt.UserRole + 3
    URL_ROLE = Qt.UserRole + 4

    def __init__(self, categorys, parent=None):
        super(CategoryListModel, self).__init__(parent)
        self._categorys = categorys
        keys = {}
        keys[CategoryListModel.TID_ROLE] = "tid"
        keys[CategoryListModel.NAME_ROLE] = "name"
        keys[CategoryListModel.bgimage_ROLE] = "bgimage"
        keys[CategoryListModel.URL_ROLE] = "url"
        self.setRoleNames(keys)

    def rowCount(self, index):
        return len(self._categorys)


    def data(self, index, role):
        if not index.isValid():
            return None

        if index.row() > len(self._categorys):
            return None

        img = self._categorys[index.row()]
        if role == CategoryListModel.TID_ROLE:
            return img.tid
        elif role == CategoryListModel.NAME_ROLE:
            return img.name
        elif role == CategoryListModel.bgimage_ROLE:
            return img.bgimage
        elif role == CategoryListModel.URL_ROLE:
            return img.url
        else:
            return None

class CategoryController(QtCore.QObject):
    # ratepage_maker = QtCore.Signal()
    # tryluckpage_maker = QtCore.Signal()
    # clean_model = QtCore.Signal()

    def __init__(self,window):
        QtCore.QObject.__init__(self)
        self.window = window

    @QtCore.Slot(str,str,str,str)
    def thingSelected(self, tid, name, bgimage, url):
        my_choose_category = CategoryWrapper(Category(tid, name, bgimage, url))
        self.my_choose_clounm = self.window.My_JsonMan.getClounm(my_choose_category.url)
        self.window.imagelistviewcontroller.setList(self.my_choose_clounm.data)
        
        self.window.Layout.setCurrentWidget(self.window.imagelistview)


        




