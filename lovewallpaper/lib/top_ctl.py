# -*- coding: utf-8 -*-
from PySide import QtCore
from PySide import QtGui
from PySide.QtCore import Qt
from jsonman import Picture
from wapper import PictureWrapper,PhotoListModel

class TopListController(QtCore.QObject):
    showdetail = QtCore.Signal()


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
            view = self.window.toplistview
        if rc == None:
            rc = self.window.toplistview_rc
        self.mylist = [PictureWrapper(thing) for thing in mylist ]
        self.clounm_list  = PhotoListModel(self.mylist)
        rc.setContextProperty('datamodel', self.clounm_list)
        rc.setContextProperty('place', "rate")

    def setLinks(self, links):
        self.links = links

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


    @QtCore.Slot(int,str, str, str, str,str,str)
    def thingSelected(self, myindex, key, small, big, original, detail,place = None):
        picture_clicked = PictureWrapper(Picture(key,small,big,original,detail))

        self.imageform.imagerc.setContextProperty('myimage', picture_clicked)
        self.imageform.image_controller.setIndex(myindex)
        self.imageform.image_controller.setList(self.mylist)

        self.window.MasterContainerLayout.setCurrentWidget(self.imageform)




