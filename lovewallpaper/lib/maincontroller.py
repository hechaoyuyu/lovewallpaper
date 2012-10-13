from jsonman import Picture
from PySide import QtCore
from wapper import PictureWrapper,PhotoListModel

class Controller(QtCore.QObject):

    def __init__(self,window,ratelist):
        QtCore.QObject.__init__(self)
        self.window = window
        self.ratelist = ratelist


    @QtCore.Slot(int,str, str, str, str,str)
    def thingSelected(self, myindex, key, small, big, original, detail):

        picture_clicked = PictureWrapper(Picture(key,small,big,original,detail))

        self.window.ImageLayoutContainer.imagerc.setContextProperty('myimage', picture_clicked)

        self.window.ImageLayoutContainer.image_controller.setList(self.ratelist)


        self.window.ImageLayoutContainer.image_controller.setIndex(myindex)
       
        self.window.MasterContainerLayout.setCurrentWidget(self.window.ImageLayoutContainer)

    @QtCore.Slot()
    def nextPage(self):
        pass


class TryLuckController(QtCore.QObject):

    def __init__(self,window):
        QtCore.QObject.__init__(self)
        self.window = window
        self.trylucklist = ""

    def setList(self, trylucklist):
        self.trylucklist = trylucklist

    @QtCore.Slot()
    def tryAgain(self):
        tryluck_list = self.window.My_JsonMan.create_tryluck()
        tryluck_images = [PictureWrapper(tryluck_thing) for tryluck_thing in tryluck_list]

        self.setList(tryluck_images)

        tryluck_imageList = PhotoListModel(tryluck_images)
        self.window.trylucklistview_rc.setContextProperty('datamodel', tryluck_imageList)

    @QtCore.Slot(int,str, str, str, str,str)
    def thingSelected(self, myindex, key, small, big, original, detail):

        picture_clicked = PictureWrapper(Picture(key,small,big,original,detail))

        self.window.ImageLayoutContainer.imagerc.setContextProperty('myimage', picture_clicked)

        self.window.ImageLayoutContainer.image_controller.setList(self.trylucklist)

        self.window.ImageLayoutContainer.image_controller.setIndex(myindex)
       
        self.window.MasterContainerLayout.setCurrentWidget(self.window.ImageLayoutContainer)


    @QtCore.Slot()
    def nextPage(self):
        pass
