# -*- coding: utf-8 -*-
from PySide import QtCore
from PySide import QtGui
import os
from PySide.QtCore import Qt
from wapper import PictureWrapper,ImageTagWrapper,ImageTagListModel,PropertyWrapper,PropertyListModel
from lib.manager import Manager
from jsonman import Picture
try:
    import pynotify
except:
    print "No model"
    

class TagImageController(QtCore.QObject):
    showdetail = QtCore.Signal()
                                                                               

    def __init__(self,window,rc,form,layout,backto):
        try:
            pynotify.init("LoveWallpaperHD")
        except:
            print "No model"
        QtCore.QObject.__init__(self)
        self.window = window
        self.rc = rc
        self.form =  form

        self.father_layout = layout
        self.backto = backto
        self.manager = Manager()

    def setList(self, mylist):
        self.mylist = mylist
        self.limit_count = len(mylist) + 1


    def setIndex(self,myindex):
        self.myindex =  myindex
    
    @QtCore.Slot(str,str)
    def download(self, key,url):
        """docstring for download"""
        if self.manager.download(key,url):
            print "done"
            try:
                n = pynotify.Notification(" 爱壁纸HD", "下载完成！")
                n.show()
            except:
                print "done"
    @QtCore.Slot(str,str)
    def setWallpaper(self, key,url):

        if self.manager.setWallpaper(key,url):
            print "done"
            try:
                n = pynotify.Notification(" 爱壁纸HD", "设置完成啦")
                n.show()
            except:
                print "done"


    @QtCore.Slot(str)
    def showDetail(self, url):
        detail = self.window.My_JsonMan.getDetail(url)

        detailtag = [ImageTagWrapper(kv) for kv in detail.tags]
        detailtag_model = ImageTagListModel(detailtag)

        detaildata = [PropertyWrapper(kv) for kv in detail.data]
        detaildata_model = PropertyListModel(detaildata)
        self.rc.setContextProperty('kvmodel', detaildata_model)
        self.rc.setContextProperty('detailtitle', detail.name)
        self.rc.setContextProperty('tagsmodel', detailtag_model)
    
    @QtCore.Slot(str)
    def puresetWallpaper(self, url):
        if self.manager.puresetWallpaper(url):
            print "done"
            try:
                n = pynotify.Notification(" 爱壁纸HD", "设置完成啦")
                n.show()
            except:
                print "done"

    @QtCore.Slot(str)
    def deleteWallapper(self, url):
        os.system( "rm %s "%(url))
        self.go_back()
        self.window.userimage_clicked()

    @QtCore.Slot(str)
    def lookit(self, url):
        self.form.fullscreen()

    @QtCore.Slot(str,str)
    def toTag(self,name,url):
        
        my_choose_tag_clounm = self.window.My_JsonMan.getTag(url)
        
        self.window.tag_detailimagelistview.controller.setList(my_choose_tag_clounm.data, self.window.tag_detailimagelistview.rc)
        self.window.tag_detailimagelistview.setTitle(name)
        self.window.tag_detailimagelistview.controller.setLinks(my_choose_tag_clounm.link)
        
        self.window.Imagedetail_LayoutContainer.setBackToView(self.window.tag_detailimagelistview)
       
        self.window.MasterContainerLayout.setCurrentWidget(self.window.tag_detailimagelistview)

    @QtCore.Slot()
    def go_back(self):
        self.window.showNormal()
        self.father_layout.setCurrentWidget(self.backto)

    @QtCore.Slot()
    def prevPicture(self):
        try:
            if self.myindex - 1 > -1:
                self.rc.setContextProperty('myimage', self.mylist[self.myindex-1])
                self.myindex = self.myindex - 1
        except Exception, e:
            print "No More"
            try:
                n = pynotify.Notification("爱壁纸HD", "这是第一张啦!")
                n.show()
            except:
                print "done"



    @QtCore.Slot()
    def nextPicture(self):
        try:
            if self.myindex < self.limit_count:
                self.rc.setContextProperty('myimage', self.mylist[self.myindex+1])
                self.myindex = self.myindex + 1
        except Exception, e:
            print "No More"
            try:
                n = pynotify.Notification("爱壁纸HD", "这是最后一张啦!")
                n.show()
            except:
                print "done"


    @QtCore.Slot(str, str, str, str,str)
    def thingSelected(self, key, small, big, original, detail):
   
        picture_clicked = PictureWrapper(Picture(key,small,big,original,detail))
    