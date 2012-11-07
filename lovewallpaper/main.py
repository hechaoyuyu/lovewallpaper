#!/usr/bin/python2
# -*- coding: utf-8 -*-
from __future__ import division  
import sys

import os
from PySide.QtCore import *
from PySide.QtGui import *
from PySide import QtDeclarative
import thread
from jsonman import JsonMan 
from lib.wapper import *
from lib.tags_ctl import *
from lib.category_ctl import *
from lib.imagelist_ctl import *
from lib.image_ctl import *
from lib.maincontroller import *
from lib.everyday_ctl import *
from lib.special_ctl import *
from lib.top_ctl import *
from lib.userimage_ctl import *
from lib.tag_image_ctl import *
from lib.settingsUI import SettingUI
from UI.tagimagefrom import TagImageFrom
from UI.imagefrom import ImageFrom
from UI.ImageListView import ImageListView
from UI.colunmform import ColumnFrom

import resources_rc
import ConfigParser

class LoveWallpaper(QMainWindow):
   
    def __init__(self, parent=None,app=None):
        super(LoveWallpaper, self).__init__(parent)
        #设置标题
        self.app = app
        self.setWindowTitle(u"爱壁纸HD")
        self.setWindowIcon(QIcon(":/source/notify.png"))
        self.setStyleSheet("QMainWindow {background-color:white; } QToolBar {border-bottom:2px solid #b60400} QLineEdit{ border:2px solid #b60400 }")
        CONFIG = os.path.expanduser('~') + "/.config/lovewallpaper/config"
        TIME = os.path.expanduser('~') + "/.config/lovewallpaper/splash/timeset"
        cf = ConfigParser.ConfigParser()
        
        cf.read(CONFIG)

        self.ToOffine = False
    

        #获取UUID

        homefolder = os.path.expanduser('~')
       	if cf.get("Path", "download") == "":
	  
            cf.set("Path", "download", homefolder+'/Wallpaper/')
            cf.write(open(CONFIG, "w"))

        #设置默认窗口
       

        width = int(self.app.desktop().screenGeometry().width() * 0.75)
        height = int(self.app.desktop().screenGeometry().height() * 0.75)
        self.bili = height/width
        self.imagenum = 4
        self.titlenum = 2

        self.init_width = width

        self.setMinimumSize(QSize(width, height))
        self.setIconSize(QSize(48,48))
        self.createToolBars()
        self.createActions()
        self.createToolBottons()
        #self.setUnifiedTitleAndToolBarOnMac(True)
        self.tryluck_created = False
        self.tags_created  = False
        self.everyday_created = False
        self.top_created = False
        self.special_created = False
        self.history_list = []
        self.nowview = ""
        self.setContentsMargins(0,0,0,0)


    def reseticon(self, target):
        if self.Home_actiton == target:
            self.Home_actiton.setIcon(QIcon(":/icons/home_act.png"))
        else:
            self.Home_actiton.setIcon(QIcon(":/icons/home.png"))

        if self.Categroy_action == target:
            self.Categroy_action.setIcon(QIcon(":/icons/list_act.png"))
        else:
            self.Categroy_action.setIcon(QIcon(":/icons/list.png"))

        if self.Tryluck_actiton == target:
            self.Tryluck_actiton.setIcon(QIcon(":/icons/try_act.png"))
        else:
            self.Tryluck_actiton.setIcon(QIcon(":/icons/try.png"))

        if self.My_wallpapers_actiton == target:
            self.My_wallpapers_actiton.setIcon(QIcon(":/icons/inbox_act.png"))
        else:
            self.My_wallpapers_actiton.setIcon(QIcon(":/icons/inbox.png"))

        if self.Tags_actiton == target:
            self.Tags_actiton.setIcon(QIcon(":/icons/tags_act.png"))
        else:
            self.Tags_actiton.setIcon(QIcon(":/icons/tags.png"))

        if self.Settings_actiton == target:
            self.Settings_actiton.setIcon(QIcon(":/icons/more_act.png"))
        else:
            self.Settings_actiton.setIcon(QIcon(":/icons/more.png"))


    def createActions(self):
        #添加按钮动作
        self.Home_actiton = QAction(QIcon.fromTheme("new", QIcon(":/icons/home_act.png")), u"推荐",
                self)


        self.Home_actiton.triggered.connect(self.home_clicked)

        self.Categroy_action = QAction(QIcon.fromTheme("new", QIcon(":/icons/list.png")), u"浏览",
                self, triggered=self.category_clicked)


        self.Tryluck_actiton = QAction(QIcon.fromTheme("new", QIcon(":/icons/try.png")), u"手气",
                self, triggered=self.tryluck_clicked)

        #self.Tryluck_actiton.setCheckable(True)

        self.My_wallpapers_actiton = QAction(QIcon.fromTheme("new", QIcon(":/icons/inbox.png")), u"本地",
                self, triggered=self.userimage_clicked)
        self.Tags_actiton = QAction(QIcon.fromTheme("new", QIcon(":/icons/tags.png")), u"标签",
                self, triggered=self.tags_clicked)
        self.Settings_actiton = QAction(QIcon.fromTheme("new", QIcon(":/icons/more.png")), u"更多",
                self, triggered=self.settings_clicked)
        self.Return_actiton = QAction(QIcon.fromTheme("new", QIcon(":/icons/return.png")), u"后退",
                self, triggered=self.to_home)
        self.Return_to_Master_actiton = QAction(QIcon.fromTheme("new", QIcon(":/icons/return.png")), u"后退",
                self, triggered=self.return_to_Master_clicked)
        self.set_back_action = QAction(QIcon.fromTheme("new", QIcon(":/icons/return.png")), u"后退",
                self, triggered=self.to_home)
        self.search_action = QAction(QIcon.fromTheme("new", QIcon(":/icons/search.png")), u"搜索",
                self, triggered=self.do_search)
        

        # Category的Action
        # self.Column_btn_actiton = QAction( u"分类",
        #         self, triggered=self.category_clicked)
        # self.Top_btn_actiton = QAction(u"排行",
        #         self, triggered=self.Top_btn_clicked)
        # self.Special_btn_actiton = QAction( u"专题",
        #         self, triggered=self.Special_btn_clicked)
        # self.Everyday_btn_actiton = QAction( u"每日",
        #         self, triggered=self.everyday_clicked)
    def resizeEvent(self,QResizeEvent):
  

        if self.width()  > 1300:
            print self.app.desktop().screenGeometry().width()
            self.imagenum = 5
            self.titlenum = 3
            try:
                self.imagelistview_rc.setContextProperty('imagenum', self.imagenum)
                self.trylucklistview_rc.setContextProperty('imagenum', self.imagenum)
                self.toplistview_rc.setContextProperty('imagenum', self.imagenum)
                self.mainimagelistview_rc.setContextProperty('imagenum', self.imagenum)
                self.everydayrc.setContextProperty('imagenum', self.imagenum)
                self.userlistview_rc.setContextProperty('imagenum', self.imagenum)
                self.rc.setContextProperty('imagenum', self.imagenum)
                
                self.categoryrc.setContextProperty('titlenum', self.titlenum)
                self.specialrc.setContextProperty('titlenum', self.titlenum)
            except Exception, e:
                raise e


            
        if self.width() < 1300:
            print self.app.desktop().screenGeometry().width()
            self.imagenum = 4
            self.titlenum = 2
            try:
                self.imagelistview_rc.setContextProperty('imagenum', self.imagenum)
                self.trylucklistview_rc.setContextProperty('imagenum', self.imagenum)
                self.toplistview_rc.setContextProperty('imagenum', self.imagenum)
                self.mainimagelistview_rc.setContextProperty('imagenum', self.imagenum)
                self.everydayrc.setContextProperty('imagenum', self.imagenum)
                self.userlistview_rc.setContextProperty('imagenum', self.imagenum)
                self.rc.setContextProperty('imagenum', self.imagenum)
                
                self.categoryrc.setContextProperty('titlenum', self.titlenum)
                self.specialrc.setContextProperty('titlenum', self.titlenum)

            except Exception, e:
                raise e

    def userimage_clicked(self):
        self.reseticon(self.My_wallpapers_actiton)
        self.userlistviewcontroller.setList(self.userlistviewcontroller.Prepare(),self.userlistview_rc)
        self.Layout.setCurrentWidget(self.userlistview)

    def settings_clicked(self):
        self.reseticon(self.Settings_actiton)
        self.Layout.setCurrentWidget(self.settingUI)
        

    def to_home(self):
        self.MasterContainerLayout.setCurrentWidget(self.MasterBox)


    def return_to_Master_clicked(self):
   
       
        self.Layout.setCurrentWidget(self.view)    



    def Special_btn_clicked(self):
        
        if self.special_created:
            self.CategoryContainerLayout.setCurrentWidget(self.specialview)
        else:
            self.speciallist  = self.My_JsonMan.Special()
            self.specials  =  [SpecialWrapper(special) for special in self.speciallist]
            self.special_model_list = SpecialListModel(self.specials)
            self.specialrc.setContextProperty("specials_model", self.special_model_list)
            self.special_created = True
            self.CategoryContainerLayout.setCurrentWidget(self.specialview)
            
            
    def Top_btn_clicked(self):
        if self.top_created:
            self.toplistviewcontroller.setList(self.toplist.data)
            self.toplistviewcontroller.setLinks(self.toplist.link)
            self.CategoryContainerLayout.setCurrentWidget(self.toplistview)
        else:
            self.toplist  = self.My_JsonMan.getTop()
            self.toplistviewcontroller.setList(self.toplist.data)
            self.toplistviewcontroller.setLinks(self.toplist.link)
            self.top_created = True
            self.CategoryContainerLayout.setCurrentWidget(self.toplistview)
            
        
        
    def everyday_clicked(self):


        if self.everyday_created:
            self.CategoryContainerLayout.setCurrentWidget(self.everydayview)
        else:

            self.everyday_list = self.My_JsonMan.Everyday()
            self.everydays = [EverydayWrapper(every) for every in self.everyday_list]
            self.everydays_model_list = EverydayListModel(self.everydays)
            self.everydayrc.setContextProperty('everymodel', self.everydays_model_list)

            self.everyday_created = True
            self.CategoryContainerLayout.setCurrentWidget(self.everydayview)

        

    def category_clicked(self):
        self.reseticon(self.Categroy_action)
        self.Layout.setCurrentWidget(self.CategoryBox)
        self.CategoryContainerLayout.setCurrentWidget(self.categoryview)
        

    def tags_clicked(self):
        self.reseticon(self.Tags_actiton)

        if self.tags_created:
            self.Layout.setCurrentWidget(self.tagsview)
        else:

            self.tags_list = self.My_JsonMan.create_tags()
            self.tags_texts = [TagWrapper(text) for text in self.tags_list]
            self.tags_texts_list = TagListModel(self.tags_texts)
            self.tagsrc.setContextProperty('tagsmodel', self.tags_texts_list)

            self.tags_created = True
            self.Layout.setCurrentWidget(self.tagsview)

        

    @QtCore.Slot()
    def home_clicked(self):

        self.reseticon(self.Home_actiton)
        self.Layout.setCurrentWidget(self.view)


    def tryluck_clicked(self):
        self.reseticon(self.Tryluck_actiton)

        if self.tryluck_created:

            self.Layout.setCurrentWidget(self.trylucklistview)

        else:
            self.tryluck_list = self.My_JsonMan.create_tryluck()
            self.tryluck_images = [PictureWrapper(tryluck_thing) for tryluck_thing in self.tryluck_list]

            self.trylcuklistviewcontroller.setList(self.tryluck_images)

            self.tryluck_imageList = PhotoListModel(self.tryluck_images)
            self.trylucklistview_rc.setContextProperty('datamodel', self.tryluck_imageList)
            self.tryluck_created = True
            self.Layout.setCurrentWidget(self.trylucklistview)
            



    def create_view(self):

        try:
            #初始化桌面参数
            self.My_JsonMan = JsonMan(self.app.desktop().screenGeometry().width(), 
	    self.app.desktop().screenGeometry().height(),self)
            
            #获取返回信息
            self.My_JsonMan.get_json()
            self.mylist = self.My_JsonMan.rate_list
            self.category_list = self.My_JsonMan.category_list

            #通过返回数据创建数据模型
            self.images = [PictureWrapper(thing) for thing in self.mylist]
            self.imageList = PhotoListModel(self.images)

            self.categoryes = [CategoryWrapper(text) for text in self.category_list]
            self.categoryes_list = CategoryListModel(self.categoryes)
        except Exception, e:
            print "No Network"
            self.ToOffine = True
            self.images = []
            self.imageList = []
            self.categoryes = []
            self.categoryes_list = []
            self.category_list = []
            self.mylist = []

        
        #布局UI


        self.MasterContainer = QWidget()
        self.MasterContainer.setContentsMargins(0,0,0,0)
        
        self.MasterContainerLayout = QStackedLayout()
        self.MasterContainerLayout.setSpacing(0)
        self.MasterContainer.setLayout(self.MasterContainerLayout)
        self.MasterContainerLayout.setContentsMargins(0,0,0,0)


        #顶级目录
        self.MasterBox = QWidget()
        self.MasterBox.setContentsMargins(0,0,0,0)
        self.MasterBoxLayout = QVBoxLayout()
        self.MasterBoxLayout.setSpacing(0)
        self.MasterBoxLayout.setContentsMargins(0,0,0,0)
        self.MasterBox.setLayout(self.MasterBoxLayout)
        self.MasterBoxLayout.addWidget(self.ToolBar)

        self.LayoutContainer = QWidget()
        self.Layout = QStackedLayout()
        self.Layout.setSpacing(0)
        self.LayoutContainer.setLayout(self.Layout)
        self.LayoutContainer.setContentsMargins(0,0,0,0)
        
        #Category级目录
        self.BrowserContainer = QWidget()
        self.BrowserLayout = QVBoxLayout()
        self.BrowserLayout.setSpacing(0)
        self.BrowserLayout.setContentsMargins(0,0,0,0)
        self.BrowserContainer.setLayout(self.BrowserLayout)
        self.BrowserContainer.setContentsMargins(0,0,0,0)

        self.CategoryContainer = QWidget()
        self.CategoryContainer.setContentsMargins(0,0,0,0)
        self.CategoryContainerLayout = QStackedLayout()
        self.CategoryContainer.setLayout(self.CategoryContainerLayout)
        self.CategoryContainerLayout.setContentsMargins(0,0,0,0)  


        self.CategoryBox = QWidget()
        self.CategoryBoxLayout = QStackedLayout()
        self.CategoryBox.setLayout(self.CategoryBoxLayout)

        



        self.view = QtDeclarative.QDeclarativeView()
        self.view.setResizeMode(QtDeclarative.QDeclarativeView.SizeRootObjectToView)

        
        self.rc = self.view.rootContext()
        self.controller = Controller(self, self.images)
        self.rc.setContextProperty('controller', self.controller)

        self.rc.setContextProperty('datamodel', self.imageList)
        self.rc.setContextProperty('bili', self.bili)
        self.rc.setContextProperty('imagenum', self.imagenum)
        self.view.setSource(QUrl('qrc:/UI/imagelist.qml'))

        self.createImageWindowUI_For_Category()
        self.createTopWindowUI()
        self.createImageWindowUI()
        self.createUserImageWindowUI()
        self.createdetail_ImageWindowUI()
        self.createTagImageWindowUI()
        self.createCategoryUI()
        self.createTagsUI()
        self.createTagsImageListView()

        self.createImageListViewUI()
        self.createEverydayViewUI()
        self.createSpecialViewUI()
        self.createTopListViewUI()
        self.createSearchResultViewUI()
        self.createMaserPageViewUI()
        self.createUserImageView()

        self.createTryLuckViewUI()
        self.createDetailImageListView()
        self.MasterBoxLayout.addWidget(self.LayoutContainer)
        
        # self.BrowserLayout.addWidget(self.CategoryBar)
        self.BrowserLayout.addWidget(self.CategoryContainer)

        self.CategoryBoxLayout.insertWidget(0, self.BrowserContainer)

        self.createImageWindowUI_For_Clounm()
        self.createImageWindowUI_For_Clounm_2nd()
        self.createColunmView()
        self.createColunmView_2nd()
        self.createSettingsUI()
        self.createETWindowUI()
        self.createCategoryImageListView()

        


        self.Layout.insertWidget(0,self.view)
        self.Layout.setContentsMargins(0,0,0,0)
        self.Layout.setCurrentWidget(self.view)

        self.MasterContainerLayout.insertWidget(0,self.MasterBox)
        self.Layout.insertWidget(1,self.CategoryBox)

        self.Layout.setCurrentWidget(self.view)
        self.CategoryBoxLayout.setCurrentWidget(self.BrowserContainer)
        self.MasterContainerLayout.setCurrentWidget(self.MasterBox)
        return self.MasterContainer

    def createUserImageView(self):
        self.userlistview = QtDeclarative.QDeclarativeView()
        self.userlistview.setResizeMode(QtDeclarative.QDeclarativeView.SizeRootObjectToView)

        self.userlistview_rc = self.userlistview.rootContext()
        self.userlistviewcontroller = UserImageController(self,self.MasterContainerLayout, self.UserImageLayoutContainer)
        self.userlistview_rc.setContextProperty('controller', self.userlistviewcontroller)
        self.userlistview_rc.setContextProperty('bili', self.bili)
        self.userlistview_rc.setContextProperty('imagenum', self.imagenum)
        self.userlistview.setSource(QUrl('qrc:/UI/userimagelist.qml'))
        self.Layout.insertWidget(9,self.userlistview)

    def createSettingsUI(self):
        self.settingUI = SettingUI()
        
        self.Layout.insertWidget(7,self.settingUI)



    def createColunmView(self):
        
        self.ColunmView  = ColumnFrom(self, self.MasterContainerLayout, self.MasterBox, self.clounm_ImageContainer)
        self.MasterContainerLayout.insertWidget(4,self.ColunmView)
        self.clounm_ImageContainer.setBackToView(self.ColunmView)
    
    def createColunmView_2nd(self):
        
        self.ColunmView_2nd  = ColumnFrom(self, self.MasterContainerLayout, self.ColunmView, self.clounm_2nd_ImageContainer)
        self.MasterContainerLayout.insertWidget(5,self.ColunmView_2nd)
        self.clounm_2nd_ImageContainer.setBackToView(self.ColunmView_2nd)
    
    def createTagsImageListView(self):
         self.tag_imagelistview = ImageListView(self, self.MasterContainerLayout, self.TagImageLayoutContainer, self.MasterBox )
         self.MasterContainerLayout.insertWidget(5, self.tag_imagelistview)

    def createDetailImageListView(self):
         self.tag_detailimagelistview = ImageListView(self, self.MasterContainerLayout, self.Imagedetail_LayoutContainer, self.MasterBox )
         self.MasterContainerLayout.insertWidget(5, self.tag_detailimagelistview)

    def createCategoryImageListView(self):
         self.category_imagelistview = ImageListView(self, self.MasterContainerLayout, self.ETImageContainer, self.MasterBox )
         self.ETImageContainer.setBackToView(self.category_imagelistview)
         self.MasterContainerLayout.insertWidget(5, self.category_imagelistview)

    def createSearchResultViewUI(self):
        self.searchview = QtDeclarative.QDeclarativeView()
        self.searchview.setResizeMode(QtDeclarative.QDeclarativeView.SizeRootObjectToView)

        self.searchrc = self.searchview.rootContext()
        self.searchcontroller = TagsController(self)
        self.searchrc.setContextProperty('controller', self.searchcontroller)
 

        self.searchview.setSource(QUrl('qrc:/UI/search_result.qml'))
        self.Layout.insertWidget(6,self.searchview)
        

    def createSpecialViewUI(self):
        self.specialview = QtDeclarative.QDeclarativeView()
        self.specialview.setResizeMode(QtDeclarative.QDeclarativeView.SizeRootObjectToView)

        self.specialrc = self.specialview.rootContext()
        self.special_ctl = SpecialController(self)
        self.specialrc.setContextProperty('controller', self.special_ctl)
        self.specialrc.setContextProperty('titlenum', self.titlenum)

        self.specialview.setSource(QUrl('qrc:/UI/special.qml'))
        self.CategoryContainerLayout.insertWidget(5,self.specialview)

    def createEverydayViewUI(self):
        self.everydayview = QtDeclarative.QDeclarativeView()
        self.everydayview.setResizeMode(QtDeclarative.QDeclarativeView.SizeRootObjectToView)

        self.everydayrc = self.everydayview.rootContext()
        self.everyday_ctl = EverydayController(self)
        self.everydayrc.setContextProperty('controller', self.everyday_ctl)
        self.everydayrc.setContextProperty('imagenum', self.imagenum)

        self.everydayview.setSource(QUrl('qrc:/UI/everyday.qml'))
        self.CategoryContainerLayout.insertWidget(5,self.everydayview)

    def createMaserPageViewUI(self):
        self.mainimagelistview = QtDeclarative.QDeclarativeView()
        self.mainimagelistview.setResizeMode(QtDeclarative.QDeclarativeView.SizeRootObjectToView)

        self.mainimagelistview_rc = self.mainimagelistview.rootContext()
        self.mainimagelistviewcontroller = ImageListController(self,self.MasterContainerLayout,self.ImageLayoutContainer)
        self.mainimagelistview_rc.setContextProperty('controller', self.mainimagelistviewcontroller)
        self.mainimagelistview_rc.setContextProperty('bili', self.bili)
        self.mainimagelistview_rc.setContextProperty('imagenum', self.imagenum)

        self.mainimagelistview.setSource(QUrl('qrc:/UI/imagelist.qml'))
        self.Layout.insertWidget(4,self.mainimagelistview)    
    
    def createTopListViewUI(self):

        self.toplistview = QtDeclarative.QDeclarativeView()
        self.toplistview.setResizeMode(QtDeclarative.QDeclarativeView.SizeRootObjectToView)

        self.toplistview_rc = self.toplistview.rootContext()
        self.toplistviewcontroller = TopListController(self,self.MasterContainerLayout, self.TopLayoutContainer)
        self.toplistview_rc.setContextProperty('controller', self.toplistviewcontroller)
        self.toplistview_rc.setContextProperty('bili', self.bili)
        self.toplistview_rc.setContextProperty('imagenum', self.imagenum)
        self.toplistview.setSource(QUrl('qrc:/UI/top.qml'))
        self.CategoryContainerLayout.insertWidget(4,self.toplistview)

    def createTryLuckViewUI(self):

        self.trylucklistview = QtDeclarative.QDeclarativeView()
        self.trylucklistview.setResizeMode(QtDeclarative.QDeclarativeView.SizeRootObjectToView)

        self.trylucklistview_rc = self.trylucklistview.rootContext()
        self.trylcuklistviewcontroller = TryLuckController(self)
        self.trylucklistview_rc.setContextProperty('controller', self.trylcuklistviewcontroller)
        self.trylucklistview_rc.setContextProperty('bili', self.bili)
        self.trylucklistview_rc.setContextProperty('imagenum', self.imagenum)

        self.trylucklistview.setSource(QUrl('qrc:/UI/tryluck.qml'))
        self.Layout.insertWidget(4,self.trylucklistview)

    def createImageListViewUI(self):

        self.imagelistview = QtDeclarative.QDeclarativeView()
        self.imagelistview.setResizeMode(QtDeclarative.QDeclarativeView.SizeRootObjectToView)

        self.imagelistview_rc = self.imagelistview.rootContext()
        self.imagelistviewcontroller = ImageListController(self,self.MasterContainerLayout,self.category_ImageContainer)
        self.imagelistview_rc.setContextProperty('controller', self.imagelistviewcontroller)
        self.imagelistview_rc.setContextProperty('bili', self.bili)
        self.imagelistview_rc.setContextProperty('imagenum', self.imagenum)

        self.imagelistview.setSource(QUrl('qrc:/UI/imagelist.qml'))
        self.CategoryContainerLayout.insertWidget(4,self.imagelistview)

    def createETWindowUI(self):
        self.ETImageContainer = ImageFrom(self,self.MasterContainerLayout)
        self.MasterContainerLayout.insertWidget(4,self.ETImageContainer)

    def createImageWindowUI_For_Clounm_2nd(self):
        self.clounm_2nd_ImageContainer = ImageFrom(self,self.MasterContainerLayout)
        self.MasterContainerLayout.insertWidget(4,self.clounm_2nd_ImageContainer)

    def createImageWindowUI_For_Clounm(self):
        self.clounm_ImageContainer = ImageFrom(self,self.MasterContainerLayout)
        self.MasterContainerLayout.insertWidget(3,self.clounm_ImageContainer)

    def createImageWindowUI_For_Category(self):
        self.category_ImageContainer = ImageFrom(self,self.Layout,self.MasterContainer)
        self.MasterContainerLayout.insertWidget(3,self.category_ImageContainer)

    def createImageWindowUI(self):
        self.ImageLayoutContainer = ImageFrom(self,self.MasterContainerLayout,self.MasterBox)
        self.MasterContainerLayout.insertWidget(3,self.ImageLayoutContainer)

    def createTagImageWindowUI(self):
        self.TagImageLayoutContainer = ImageFrom(self,self.MasterContainerLayout,self.MasterBox)
        self.MasterContainerLayout.insertWidget(3,self.TagImageLayoutContainer)

    def createdetail_ImageWindowUI(self):
        self.Imagedetail_LayoutContainer = TagImageFrom(self,self.MasterContainerLayout,self.MasterBox)
        self.MasterContainerLayout.insertWidget(3,self.Imagedetail_LayoutContainer)


    def createTopWindowUI(self):
        self.TopLayoutContainer = ImageFrom(self,self.MasterContainerLayout,self.MasterBox)
        self.MasterContainerLayout.insertWidget(3,self.TopLayoutContainer)

    def createUserImageWindowUI(self):
        self.UserImageLayoutContainer = ImageFrom(self,self.MasterContainerLayout,self.MasterBox)
        self.UserImageLayoutContainer.imageview.setSource(QUrl('qrc:/UI/userImage.qml'))
        self.MasterContainerLayout.insertWidget(3,self.UserImageLayoutContainer)



    def createTagsUI(self):

        self.tagsview = QtDeclarative.QDeclarativeView()
        self.tagsview.setResizeMode(QtDeclarative.QDeclarativeView.SizeRootObjectToView)

        self.tagsrc = self.tagsview.rootContext()
        self.tagscontroller = TagsController(self)
        self.tagsrc.setContextProperty('controller', self.tagscontroller)
 

        self.tagsview.setSource(QUrl('qrc:/UI/tags.qml'))
        self.Layout.insertWidget(1,self.tagsview)

    def createCategoryUI(self):
        self.categoryview = QtDeclarative.QDeclarativeView()
        self.categoryview.setResizeMode(QtDeclarative.QDeclarativeView.SizeRootObjectToView)

        self.categoryrc = self.categoryview.rootContext()
        self.categorycontroller = CategoryController(self)
        self.categoryrc.setContextProperty('controller', self.categorycontroller)
        self.categoryrc.setContextProperty('category_model', self.categoryes_list)

        
        self.categoryview.setSource(QUrl('qrc:/UI/category.qml'))
        self.CategoryContainerLayout.insertWidget(2,self.categoryview)  

    def createToolBottons(self):
        self.Home_btn = QToolButton()
        self.Home_btn.setDefaultAction(self.Home_actiton)
        self.Home_btn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.ToolBar.addWidget(self.Home_btn)


        self.Categroy_btn = QToolButton()
        self.Categroy_btn.setDefaultAction(self.Categroy_action)
        self.Categroy_btn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.ToolBar.addWidget(self.Categroy_btn)

        self.Tryluck_btn = QToolButton()
        self.Tryluck_btn.setDefaultAction(self.Tryluck_actiton)
        self.Tryluck_btn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.ToolBar.addWidget(self.Tryluck_btn)


        self.Tags_btn = QToolButton()
        self.Tags_btn.setDefaultAction(self.Tags_actiton)
        self.Tags_btn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.ToolBar.addWidget(self.Tags_btn)

        self.My_wallpapers_btn = QToolButton()
        self.My_wallpapers_btn.setDefaultAction(self.My_wallpapers_actiton)
        self.My_wallpapers_btn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.ToolBar.addWidget(self.My_wallpapers_btn)


        self.Settings_btn = QToolButton()
        self.Settings_btn.setDefaultAction(self.Settings_actiton)
        self.Settings_btn.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        
        self.ToolBar.addWidget(self.Settings_btn)



        self.clear_bar = QToolBar("Fix")
        self.clear_bar.setSizePolicy(QSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding))
        self.clear_bar.setStyleSheet("QToolBar {border-bottom:0px solid white}")
        self.ToolBar.addWidget(self.clear_bar)
        
        self.searchLine = QLineEdit()
        self.searchLine.setMaximumWidth(200)
        self.searchLine.setMaximumHeight(30)
        self.searchLine.setPlaceholderText(u"搜索")
        self.searchLine.returnPressed.connect(self.do_search)
        self.ToolBar.addWidget(self.searchLine)

        self.search_btn = QToolButton()
        self.search_btn.setDefaultAction(self.search_action)
        self.search_btn.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.search_btn.setStyleSheet("QToolButton {background-color:#b60400;height:25px;width:60px;margin-right:10px;} ")
        self.ToolBar.addWidget(self.search_btn)


    def createToolBars(self):
        self.ToolBar = QToolBar("MainToolBar")
        self.ToolBar.setFloatable(False)
        self.ToolBar.setMovable(False)
        self.ToolBar.setIconSize(QSize(48,48))


    def do_search(self):
        self.search_word = self.searchLine.text()
        url = self.My_JsonMan.getSearch_Url().replace("%s",self.search_word)

        search_tag_list = self.My_JsonMan.getSearch_Result(url)
        tags_texts = [TagWrapper(text) for text in search_tag_list]
        tags_texts_list = TagListModel(tags_texts)

        self.searchrc.setContextProperty('tagsmodel', tags_texts_list)

        self.MasterContainerLayout.setCurrentWidget(self.LayoutContainer)
        self.Layout.setCurrentWidget(self.searchview)

  
