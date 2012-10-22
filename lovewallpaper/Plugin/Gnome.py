# -*- coding: utf-8 -*-

from xml.dom.minidom import Document
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
        os.system( "gsettings set org.gnome.desktop.background picture-uri \"file://%s/%s.jpg\""%(path, key))

    
    def puresetWallpaper(self, url):
        os.system( "gsettings set org.gnome.desktop.background picture-uri \"file://%s\""%(url))


class AutoSlide:
    """docstring for AutoSlide"""
    def BeginSlide(self, files,time):

        doc = Document()

        background = doc.createElement("background")
        doc.appendChild(background)

        starttime = doc.createElement("starttime")
       
        year = doc.createElement("year")
        year_text = doc.createTextNode("2009")
        year.appendChild(year_text)

        month = doc.createElement("month")
        month_text = doc.createTextNode("08")
        month.appendChild(month_text)

        day = doc.createElement("day")
        day_text = doc.createTextNode("04")
        day.appendChild(day_text)

        hour = doc.createElement("hour")
        hour_text = doc.createTextNode("00")
        hour.appendChild(hour_text)

        minute = doc.createElement("minute")
        minute_text = doc.createTextNode("00")
        minute.appendChild(minute_text)

        second = doc.createElement("second")
        second_text = doc.createTextNode("00")
        second.appendChild(second_text)

        starttime.appendChild(year)
        starttime.appendChild(month)
        starttime.appendChild(day)
        starttime.appendChild(hour)
        starttime.appendChild(minute)
        starttime.appendChild(second)

        background.appendChild(starttime)

        
        timestr = str(60*time)
        changetimestr = "5" 


        odd = True

        for file in files:
            if(odd):
                static = doc.createElement("static")
                
                file_e = doc.createElement("file")
                file_text = doc.createTextNode(file)
                file_e.appendChild(file_text)

                duration = doc.createElement("duration")
                duration_text = doc.createTextNode(timestr)
                duration.appendChild(duration_text)

                static.appendChild(duration)
                static.appendChild(file_e)

                background.appendChild(static)
                odd = False
            else:
                transition = doc.createElement("transition")

                duration = doc.createElement("duration")
                duration_text = doc.createTextNode("5")
                duration.appendChild(duration_text)


                file_e = doc.createElement("file")
                file_text = doc.createTextNode(file)
                file_e.appendChild(file_text)

                transition.appendChild(duration)
                transition.appendChild(file_e)

                background.appendChild(transition)
                odd = True

        if (odd):
            static = doc.createElement("static")
                    
            file_e = doc.createElement("file")
            file_text = doc.createTextNode(files[0])
            file_e.appendChild(file_text)

            duration = doc.createElement("duration")
            duration_text = doc.createTextNode(timestr)
            duration.appendChild(duration_text)

            static.appendChild(duration)
            static.appendChild(file_e)
            
            background.appendChild(static)
            

        self.createfile(background)
            

            
    def createfile(self,result):
                path =  os.path.expanduser('~')
                background = open(path+'/.background.xml','w')
                background.write(result.toprettyxml(indent="  "))
                background.close()
                os.system("gsettings set org.gnome.desktop.background picture-uri 'file:///"+path+"/.background.xml'")

    def RandomSet(self,files):      
                                    
        mymax = len(files) - 1
        num = random.randint(0,mymax)
        wallpeper = files[num] 

        os.system("gsettings set org.gnome.desktop.background picture-uri 'file:///"+wallpeper+"'")

