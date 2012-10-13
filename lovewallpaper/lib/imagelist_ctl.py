# -*- coding: utf-8 -*-
from PySide import QtCore
from PySide import QtGui
from PySide.QtCore import Qt
from jsonman import Picture
from wapper import PictureWrapper,PhotoListModel

class ImageListController(QtCore.QObject):

    def __init__(self,window,layout = None, imageform = None):
        QtCore.QObject.__init__(self)
        self.window = window
        self.links = ""
        
        if layout == None:
            self.layout = self.window.CategoryContainerLayout
        else:
            self.layout = layout
        if imageform == None:
            self.imageform =  self.window.category_ImageContainer
        else:
            self.imageform = imageform

    def setList(self, mylist,rc = None, view = None):
        if view == None:
            view = self.window.imagelistview
        if rc == None:
            rc = self.window.imagelistview_rc
        self.rc = rc

        self.mylist = [PictureWrapper(thing) for thing in mylist ]
        self.clounm_list  = PhotoListModel(self.mylist)
        rc.setContextProperty('datamodel', self.clounm_list)


    def setLinks(self, links):
        self.links = links

    def setColors(self, colors):
        self.colors = colors

    def setImageForm(self, imageform):
        self.imageform = imageform
        
    def setFatherLayout(self, layout):
        self.layout = layout

    @QtCore.Slot()
    def nextPage(self):
        try:
            if self.links["next"] != "":
                nextPage_list  = self.window.My_JsonMan.getTag(self.links["next"])
                self.links = nextPage_list.link
                ob_list = [PictureWrapper(thing) for thing in nextPage_list.data ]

                count = len(self.mylist)
                for image in ob_list:
                    self.mylist.append(image)
        except Exception, e:
            print "No Next Page"
            try:
                n = pynotify.Notification("爱壁纸HD", "这个没有更多的壁纸啦!")
                n.show()
            except:
                print "done"


    @QtCore.Slot(int,str, str, str, str,str)
    def thingSelected(self, myindex, key, small, big, original, detail):
        picture_clicked = PictureWrapper(Picture(key,small,big,original,detail))

        self.imageform.imagerc.setContextProperty('myimage', picture_clicked)
        self.imageform.image_controller.setIndex(myindex)
        self.imageform.image_controller.setList(self.mylist)

        self.window.MasterContainerLayout.setCurrentWidget(self.imageform)

    @QtCore.Slot(str)
    def colorSelected(self, color):
  
        my_choose_clounm = self.window.My_JsonMan.getClounm(self.colors[color].url)
        self.setList(my_choose_clounm.data, self.rc)
        self.setLinks(my_choose_clounm.link)



