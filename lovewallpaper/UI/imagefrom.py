# -*- coding: utf-8 -*-
from PySide.QtCore import QUrl
from PySide.QtGui import *
from PySide import QtDeclarative
from lib.image_ctl import *


class ImageFrom(QWidget):
        """docstring for ImageFrom"""
        def __init__(self,window,layout = None,backto = None):
                super (ImageFrom, self).__init__()
                
                #导入这个页面的视图
                
                self.showNormal= True
                
                self.window = window
                self.backto = backto
                self.father_layout = layout

                self.setContentsMargins(0,0,0,0)
                self.ImageLayout = QVBoxLayout()
                self.ImageLayout.setContentsMargins(0,0,0,0)

                # self.ImageBar = QToolBar("ImageToolBar")
                # self.ImageBar.setFloatable(False)
                # self.ImageBar.setMovable(False)


                # self.return_action = QAction(QIcon.fromTheme("new", QIcon(":/icons/return.png")), u"返回",
                # self)

                # self.return_btn = QToolButton()
                # self.return_btn.setDefaultAction(self.return_action)
                # self.return_btn.setToolButtonStyle(Qt.ToolButtonIconOnly)
                # self.return_btn.triggered.connect(self.back)

                # self.ImageBar.addWidget(self.return_btn)

                # self.image_btn_container = QWidget()

                # self.image_btn_container.setFixedHeight(40)
                # self.image_btn_layout = QHBoxLayout()

                # self.image_btn_layout.setContentsMargins(100,5,100,5)
                # self.image_btn_container.setLayout(self.image_btn_layout)
               

                self.setLayout(self.ImageLayout)

                # self.download_btn = QPushButton(u"下载图片")
                # self.set_bg_btn = QPushButton(u"设置为壁纸")
                # self.detail_btn = QPushButton(u"显示详情")


                # self.image_btn_layout.addWidget(self.download_btn)
                # self.image_btn_layout.addWidget(self.set_bg_btn)
                # self.image_btn_layout.addWidget(self.detail_btn)

                self.imageview = QtDeclarative.QDeclarativeView()
                self.imageview.setResizeMode(QtDeclarative.QDeclarativeView.SizeRootObjectToView)

                self.imagerc = self.imageview.rootContext()
                self.image_controller = ImageController(window,self.imagerc,self,self.father_layout,self.backto)
                self.imagerc.setContextProperty('controller', self.image_controller)

                self.imageview.setSource(QUrl('qrc:/UI/image.qml'))

                # self.ImageLayout.addWidget(self.ImageBar)
                self.ImageLayout.addWidget(self.imageview)
                # self.ImageLayout.addWidget(self.image_btn_container)
                
        
        def fullscreen(self):
                if self.showNormal:
                        self.window.showFullScreen()
                        self.showNormal = False
                else:
                        self.window.showNormal()
                        self.showNormal = True



        @QtCore.Slot()
        def setBackToView(self, view):
               
                self.image_controller.backto = view

        @QtCore.Slot()
        def setFatherLayout(self, layout):
                self.image_controller.father_layout = layout

                
