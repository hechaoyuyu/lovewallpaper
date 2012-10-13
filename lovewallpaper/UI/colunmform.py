# -*- coding: utf-8 -*-
from PySide.QtCore import QUrl,QSize
from PySide.QtGui import *
from PySide import QtDeclarative
from lib.imagelist_ctl import *
from lib.imagetag_ctl import *
from lib.wapper import ImageTagWrapper, ImageTagListModel

class Color:
        """docstring for Color"""
        def __init__(self, url, colorid ,name):
                self.url = url
                self.colorid =colorid
                self.name = name
                
                

class ColumnFrom(QWidget):
        """docstring for ImageFrom"""
        def __init__(self,window,layout = None , backto= None, imageform = None):
                super (ColumnFrom, self).__init__()
                self.window = window
                self.father_layout = layout
                self.backto = backto
                self.imageform = imageform
                self.createNewest = False
                self.createTags = False
                self.setStyleSheet("QToolBar {background-color:#b60400; border-bottom:2px solid #b60400;color:white}QToolButton{color:white; font-size:19px}")
                self.setContentsMargins(0,0,0,0)
                self.Layout = QVBoxLayout()
                self.Layout.setSpacing(0)
                self.Layout.setContentsMargins(0,0,0,0)

                self.Bar = QToolBar("ToolBar")
                self.Bar.setFloatable(False)
                self.Bar.setMovable(False)
                self.Bar.setIconSize(QSize(44,44))
                #Nav Container
                self.NavContainer = QWidget()
                self.NavLayout = QStackedLayout()
                self.NavContainer.setLayout(self.NavLayout)

                #CreateAction

                self.return_action = QAction(QIcon.fromTheme("new", QIcon(":/icons/return.png")), u"返回",self)


                self.Recent_Btn_Action = QAction(u"最新",self, triggered=self.newest_clicked)
                self.Hot_Btn_Action = QAction(u"热门",self,  triggered=self.hot_clicked)
                self.Relative_Tags_Btn_Action = QAction(u"相关标签",self,  triggered=self.tags_clicked)

                #CreateToolButton

                self.return_btn = QToolButton()
                self.return_btn.setDefaultAction(self.return_action)
                self.return_btn.setToolButtonStyle(Qt.ToolButtonIconOnly)
                self.return_btn.clicked.connect(self.back)

                self.Hot_Btn = QToolButton()
                self.Hot_Btn.setDefaultAction(self.Hot_Btn_Action)
                self.Hot_Btn.setToolButtonStyle(Qt.ToolButtonIconOnly) 

                self.Recent_Btn = QToolButton()
                self.Recent_Btn.setDefaultAction(self.Recent_Btn_Action)
                self.Recent_Btn.setToolButtonStyle(Qt.ToolButtonIconOnly)

                self.Relative_Tags_Btn = QToolButton()
                self.Relative_Tags_Btn.setDefaultAction(self.Relative_Tags_Btn_Action)
                self.Relative_Tags_Btn.setToolButtonStyle(Qt.ToolButtonIconOnly)
                
                self.Bar.addWidget(self.return_btn)
                self.Bar.addWidget(self.Recent_Btn)
                self.Bar.addWidget(self.Hot_Btn)
                self.Bar.setIconSize(QSize(44,44))
                self.Bar.addWidget(self.Relative_Tags_Btn)

                ####
               

                self.setLayout(self.Layout)

                #####

                #创建views

                self.view = QtDeclarative.QDeclarativeView()
                self.view.setResizeMode(QtDeclarative.QDeclarativeView.SizeRootObjectToView)

                self.rc = self.view.rootContext()
                self.controller = ImageListController(window, layout, imageform)
                self.rc.setContextProperty('controller', self.controller)
                self.rc.setContextProperty('bili', self.window.bili)
                self.rc.setContextProperty('imagenum', self.window.imagenum)
                self.view.setSource(QUrl('qrc:/UI/imagecolors.qml'))

                self.NavLayout.insertWidget(0, self.view)

                #######
                
                self.hot_view = QtDeclarative.QDeclarativeView()
                self.hot_view.setResizeMode(QtDeclarative.QDeclarativeView.SizeRootObjectToView)

                self.hot_rc = self.hot_view.rootContext()
                self.hot_controller = ImageListController(window,layout, imageform)
                self.hot_rc.setContextProperty('controller', self.hot_controller)
                self.hot_rc.setContextProperty('bili', self.window.bili)
                self.hot_rc.setContextProperty('imagenum', self.window.imagenum)
                self.hot_view.setSource(QUrl('qrc:/UI/imagecolors.qml'))

                self.NavLayout.insertWidget(1, self.hot_view)

                ########

                self.tags_view = QtDeclarative.QDeclarativeView()
                self.tags_view.setResizeMode(QtDeclarative.QDeclarativeView.SizeRootObjectToView)

                self.tags_rc = self.tags_view.rootContext()
                self.tags_controller = ImageTagController(window)
                self.tags_rc.setContextProperty('controller', self.tags_controller)

                self.tags_view.setSource(QUrl('qrc:/UI/imagetag.qml'))

                self.NavLayout.insertWidget(2, self.tags_view)

                #########


                self.Layout.addWidget(self.Bar)
                self.Layout.addWidget(self.NavContainer)
        def resizeEvent(self,QResizeEvent):
  

                if self.width()  > 1300:
              
                    self.imagenum = 5
                    try:
                        self.hot_rc.setContextProperty('imagenum', self.window.imagenum)
                        self.rc.setContextProperty('imagenum', self.window.imagenum)
                        

                    except Exception, e:
                        raise e



                if self.width()  < 1300 :
              
                    self.imagenum = 4
                    try:
                        self.hot_rc.setContextProperty('imagenum', self.window.imagenum)
                        self.rc.setContextProperty('imagenum', self.window.imagenum)
                        

                    except Exception, e:
                        raise e



        def setClounm(self, clounm):
                self.clounm = clounm

                self.setURL(self.clounm.url)
                colorlist = {}
                for color in self.clounm.colorlist:
                        colorlist[color["name"]] =  Color(color["url"],color["id"],color["name"])
                      
                        
                self.controller.setColors(colorlist)
                ######
                self.controller.setList(self.clounm.data, self.rc)
                self.controller.setLinks(self.clounm.link)
                #######

                self.hotClounm = self.window.My_JsonMan.getClounm(self.hotURL)

                self.hot_controller.setList(self.hotClounm.data, self.hot_rc)
                self.hot_controller.setLinks(self.hotClounm.link)

                hotcolorlist = {}
                for color in self.hotClounm.colorlist:
                        hotcolorlist[color["name"]] =  Color(color["url"],color["id"],color["name"])
                
                self.hot_controller.setColors(hotcolorlist)
                #####
                if self.clounm.tags == None:
                        self.Relative_Tags_Btn.hide()
                else:
                        self.Relative_Tags_Btn.show()
                        self.imagetags = [ImageTagWrapper(thing) for thing in self.clounm.tags]
                        self.imagetagsList = ImageTagListModel(self.imagetags)
                        self.tags_rc.setContextProperty('datamodel', self.imagetagsList)



        def setURL(self, url):

                self.url = url
          
                self.newestURL = self.url['newest']
                self.hotURL = self.url['hot']

        def setLink(self, link):
                pass

        def setTags(self, tags):
                self.tags = tags


        def newest_clicked(self):
                self.NavLayout.setCurrentWidget(self.view)

        def hot_clicked(self):

                self.NavLayout.setCurrentWidget(self.hot_view)

        def tags_clicked(self):
                self.NavLayout.setCurrentWidget(self.tags_view)
        
        @QtCore.Slot()
        def setBackToView(self, view):
                self.backto = view

        @QtCore.Slot()
        def setFatherLayout(self, layout):
                self.father_layout = layout

        @QtCore.Slot()
        def back(self):
                self.father_layout.setCurrentWidget(self.backto)

                
