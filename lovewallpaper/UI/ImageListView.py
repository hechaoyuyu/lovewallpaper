# -*- coding: utf-8 -*-
from PySide.QtCore import QUrl,QSize
from PySide.QtGui import *
from PySide import QtDeclarative
from lib.imagelist_ctl import *

class ImageListView(QWidget):
        """docstring for ImageFrom"""
        def __init__(self,window, layout = None, imageform = None, backto = None, title = None):
                super (ImageListView, self).__init__()
                
                #导入这个页面的视图
                self.father_layout = layout
                self.setStyleSheet("QToolBar {background-color:#b60400; border-bottom:2px solid #b60400} QLabel{color:white; font-size:19px}")
                self.window = window

                self.backto = backto

                self.setContentsMargins(0,0,0,0)
                self.Layout = QVBoxLayout()
                self.Layout.setSpacing(0)
                self.Layout.setContentsMargins(0,0,0,0)

                self.Bar = QToolBar("ToolBar")
                self.Bar.setFloatable(False)
                self.Bar.setMovable(False)
                self.Bar.setIconSize(QSize(44,44))

                self.return_action = QAction(QIcon.fromTheme("new", QIcon(":/icons/return.png")), u"返回",
                self)

                self.return_btn = QToolButton()
                self.return_btn.setDefaultAction(self.return_action)
                self.return_btn.setToolButtonStyle(Qt.ToolButtonIconOnly)
                self.return_btn.triggered.connect(self.back)

                
                
                self.clear_bar_left = QToolBar("Fix")
                
                self.Bar.addWidget(self.clear_bar_left)
                self.clear_bar_left.addWidget(self.return_btn)

                self.label = QLabel(title)
                self.Bar.addWidget(self.label)
                
                self.clear_bar_right = QToolBar("Fix")
                self.clear_bar_right.setSizePolicy(QSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding))
                self.Bar.addWidget(self.clear_bar_right)
                self.Bar.setIconSize(QSize(44,44))




                self.setLayout(self.Layout)


                self.view = QtDeclarative.QDeclarativeView()
                self.view.setResizeMode(QtDeclarative.QDeclarativeView.SizeRootObjectToView)

                self.rc = self.view.rootContext()
                self.controller = ImageListController(window,layout,imageform)
                self.rc.setContextProperty('controller', self.controller)
                self.rc.setContextProperty('bili', self.window.bili)
                self.rc.setContextProperty('imagenum', self.window.imagenum)
                
                self.view.setSource(QUrl('qrc:/UI/imagelist.qml'))

                self.Layout.addWidget(self.Bar)
                self.Layout.addWidget(self.view)
        
        @QtCore.Slot()
        def setTitle(self, title):
                self.label.setText(title)          


        @QtCore.Slot()
        def setBackToView(self, view):
                self.backto = view

        @QtCore.Slot()
        def setFatherLayout(self, layout):
                self.father_layout = layout

        @QtCore.Slot()
        def back(self):
                self.father_layout.setCurrentWidget(self.backto)

                
