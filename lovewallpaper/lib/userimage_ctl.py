# -*- coding: utf-8 -*-
from PySide import QtCore
from PySide import QtGui
from PySide.QtCore import Qt
from jsonman import Picture
from wapper import UserImageWapper,UserImageListModel
from lib.manager import Manager
import os

class Image:
    """docstring for Image"""
    def __init__(self, index,url):
        self.index = index
        self.url = url
        

class UserImageController(QtCore.QObject):


    def __init__(self,window,layout = None, imageform = None):
        QtCore.QObject.__init__(self)
        self.window = window
        self.links = ""
        self.manager = Manager()
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
        self.mylist = [UserImageWapper(thing) for thing in mylist ]
        self.clounm_list  = UserImageListModel(self.mylist)
        rc.setContextProperty('datamodel', self.clounm_list)



    def setImageForm(self, imageform):
        self.imageform = imageform
        
    def setFatherLayout(self, layout):
        self.layout = layout

    def Prepare(self):
        files = Manager().prepareFiles()
        fileslist = []
        num = 0
        for myfile in files:
          
            fileslist.append(Image(num, myfile.decode("utf-8")))
            num = num + 1
        return fileslist

    @QtCore.Slot(str)
    def setWallpaper(self, url):

        if self.manager.puresetWallpaper(url):
            print "done"
            try:
                n = pynotify.Notification(" 爱壁纸HD", "设置完成啦",  "./source/notify.png")
                n.set_urgency(pynotify.URGENCY_CRITICAL)
                n.set_timeout(10000) # 10 seconds
                n.set_category("device")
                n.show()
            except:
                print "done"

    @QtCore.Slot(str)
    def deleteWallapper(self, url):
        os.system( "rm %s "%(url))
        self.window.userimage_clicked()

    @QtCore.Slot(str)
    def lookit(self, url):
        pass

    @QtCore.Slot(int,str)
    def thingSelected(self, myindex, url):
     
        picture_clicked = UserImageWapper(Image(myindex,url))

        self.imageform.imagerc.setContextProperty('myimage', picture_clicked)
        self.imageform.image_controller.setIndex(myindex)
        self.imageform.image_controller.setList(self.mylist)

        self.window.MasterContainerLayout.setCurrentWidget(self.imageform)




