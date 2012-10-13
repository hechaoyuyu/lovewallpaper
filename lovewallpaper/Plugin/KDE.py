# -*- coding: utf-8 -*-
import os
import random
import fileinput
import sys 
try:
    import pynotify
except:
    print "No model"

class WallpaperSetter:
    """docstring for WallpaperSetter"""

        #如果桌面环境支持设置壁纸，返回True


    def setWallpaper(self, path, key):
        os.system("dbus-send --session --dest=org.new_wallpaper.Plasmoid --type=method_call /org/new_wallpaper/Plasmoid/0 org.new_wallpaper.Plasmoid.SetWallpaper string:%s.jpg" %(path+key))
       
    
    def puresetWallpaper(self, url):
        os.system("dbus-send --session --dest=org.new_wallpaper.Plasmoid --type=method_call /org/new_wallpaper/Plasmoid/0 org.new_wallpaper.Plasmoid.SetWallpaper string:%s" %(url))

class AutoSlide:
    """docstring for AutoSlide"""
    def BeginSlide(self, files,time):
        try:
            pynotify.init("LoveWallpaperHD")
            n = pynotify.Notification(" 爱壁纸HD", "很抱歉，现在爱壁纸HD不支持设置KDE自动切换壁纸，您可以使用KDE原生的图片文件夹轮放功能来实现")
            n.show()
            return False
        except:
                print "done"

    def RandomSet(self,files):      
                                    
        mymax = len(files) - 1
        num = random.randint(0,mymax)
        wallpeper = files[num] 
        os.system("dbus-send --session --dest=org.new_wallpaper.Plasmoid --type=method_call /org/new_wallpaper/Plasmoid/0 org.new_wallpaper.Plasmoid.SetWallpaper string:%s" %(wallpaper))

            

