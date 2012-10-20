# -*- coding: utf-8 -*-
from appscript import app, mactypes
import os
import random

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
        f = path + key+".jpg"
        print "defaults write com.apple.desktop Background '{default = {ImageFilePath =\"" + f + "\"; }; }'; killAll Dock; "
        os.system("defaults write com.apple.desktop Background '{default = {ImageFilePath =\"" + f + "\"; }; }'; killAll Dock; ")

    def puresetWallpaper(self, url):
        f = url
        print "defaults write com.apple.desktop Background '{default = {ImageFilePath =\"" + f + "\"; }; }'; killAll Dock; "
        os.system("defaults write com.apple.desktop Background '{default = {ImageFilePath =\"" + f + "\"; }; }'; killAll Dock; ")


class AutoSlide:
    """docstring for AutoSlide"""
    def BeginSlide(self, files,time):
        try:
            pynotify.init("LoveWallpaperHD")
            n = pynotify.Notification(" 爱壁纸HD", "很抱歉，现在爱壁纸HD不支持设置Mac自动切换壁纸，您可以使用Mac原生的图片文件夹轮放功能来实现")
            n.show()
            return False
        except:
                print "done"

    def RandomSet(self,files):      
                                    
        mymax = len(files) - 1
        num = random.randint(0,mymax)
        wallpeper = files[num] 
        f = wallpeper
        print "defaults write com.apple.desktop Background '{default = {ImageFilePath =\"" + f + "\"; }; }'; killAll Dock; "
        os.system("defaults write com.apple.desktop Background '{default = {ImageFilePath =\"" + f + "\"; }; }'; killAll Dock; ")
