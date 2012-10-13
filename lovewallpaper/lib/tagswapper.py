# -*- coding: utf-8 -*-
from PySide import QtCore
from PySide import QtGui
from PySide.QtCore import Qt

class TagWrapper(QtCore.QObject):
    def __init__(self, tag):
        QtCore.QObject.__init__(self)
        self._tag = tag
 
    def _tid(self):
        return self._tag.tid
    def _name(self):
        return self._tag.name
    def _total(self):
        return self._tag.total
    def _url(self):
        return self._tag.url

 
    changed = QtCore.Signal()
 
    tid = QtCore.Property(unicode, _tid, notify=changed)
    name = QtCore.Property(unicode, _name, notify=changed)
    total = QtCore.Property(unicode, _total, notify=changed)
    url = QtCore.Property(unicode, _url, notify=changed)

class TagListModel(QtCore.QAbstractListModel):
    TID_ROLE = Qt.UserRole + 1
    NAME_ROLE = Qt.UserRole + 2
    TOTAL_ROLE = Qt.UserRole + 3
    URL_ROLE = Qt.UserRole + 4

    def __init__(self, tags, parent=None):
        super(TagListModel, self).__init__(parent)
        self._tags = tags
        keys = {}
        keys[TagListModel.TID_ROLE] = "tid"
        keys[TagListModel.NAME_ROLE] = "name"
        keys[TagListModel.TOTAL_ROLE] = "total"
        keys[TagListModel.URL_ROLE] = "url"
        self.setRoleNames(keys)

    def rowCount(self, index):
        return len(self._tags)


    def data(self, index, role):
        if not index.isValid():
            return None

        if index.row() > len(self._tags):
            return None

        img = self._tags[index.row()]
        if role == TagListModel.TID_ROLE:
            return img.tid
        elif role == TagListModel.NAME_ROLE:
            return img.name
        elif role == TagListModel.TOTAL_ROLE:
            return img.total
        elif role == TagListModel.URL_ROLE:
            return img.url
        else:
            return None

class TagsController(QtCore.QObject):
    # ratepage_maker = QtCore.Signal()
    # tryluckpage_maker = QtCore.Signal()
    # clean_model = QtCore.Signal()

    def __init__(self,window):
        QtCore.QObject.__init__(self)
        self.window = window

    @QtCore.Slot(str)
    def thingSelected(self, wrapper):
        print 'User clicked on:', wrapper