# -*- coding: utf-8 -*-
from PySide import QtCore
from PySide import QtGui
from PySide.QtCore import Qt
from jsonman import JsonMan
from jsonman import Tag
from wapper import TagWrapper,TagListModel
from UI.ImageListView import ImageListView

class TagsController(QtCore.QObject):
    # ratepage_maker = QtCore.Signal()
    # tryluckpage_maker = QtCore.Signal()
    # clean_model = QtCore.Signal()

    def __init__(self,window):
        QtCore.QObject.__init__(self)
        self.window = window

    @QtCore.Slot()
    def randomTag(self):
        tags_list = self.window.My_JsonMan.create_tags()
        tags_texts = [TagWrapper(text) for text in tags_list]
        tags_texts_list = TagListModel(tags_texts)
        self.window.tagsrc.setContextProperty('tagsmodel', tags_texts_list)

    @QtCore.Slot(str, str, str, str)
    def thingSelected(self, tid, name, total, url):
        my_choose_tag = TagWrapper(Tag(tid, name, total, url))
        self.my_choose_tag_clounm = self.window.My_JsonMan.getTag(my_choose_tag.url)
        
        self.window.tag_imagelistview.controller.setList(self.my_choose_tag_clounm.data, self.window.tag_imagelistview.rc)
        self.window.tag_imagelistview.setTitle(name)
        self.window.tag_imagelistview.controller.setLinks(self.my_choose_tag_clounm.link)

        
        self.window.TagImageLayoutContainer.setBackToView(self.window.tag_imagelistview)
       
        self.window.MasterContainerLayout.setCurrentWidget(self.window.tag_imagelistview)