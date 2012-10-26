# -*- coding: utf-8 -*-

from xml.dom.minidom import Document
import os
import random
try:
    import pynotify
except:
    print "No model"
#咳咳，类的名字不要改变，函数名称也不要改变，下面三个参数会自动传入
#path是传过来的图片所在的文件夹
#key是用户操作的图片的名字
#files是path目录下的所有文件

class WallpaperSetter:
    """docstring for WallpaperSetter"""
    def __init__(self):
        #如果桌面环境支持设置壁纸，返回True
        pass

    def setWallpaper(self, path, key):
        os.system(  "gconftool-2 --type=string --set /desktop/gnome/background/picture_filename %s/%s.jpg"  %(path, key))


    def puresetWallpaper(self, url):
        os.system(  "gconftool-2 --type=string --set /desktop/gnome/background/picture_filename %s"  %(url))


class AutoSlide:
    """docstring for AutoSlide"""
    def BeginSlide(self, files,time):
        try:
            pynotify.init("LoveWallpaperHD")
            n = pynotify.Notification(" 爱壁纸HD", "很抱歉，现在爱壁纸HD不支持设置StartOS自动切换壁纸")
            n.show()
            return False
        except:
                print "done"

    def RandomSet(self,files):      
                                    
        mymax = len(files) - 1
        num = random.randint(0,mymax)
        wallpeper = files[num] 

        os.system(  "gconftool-2 --type=string --set /desktop/gnome/background/picture_filename %s"  %(wallpeper))