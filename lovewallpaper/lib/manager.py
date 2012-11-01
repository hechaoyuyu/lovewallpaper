# -*- coding: utf-8 -*-
import ConfigParser
import urllib2
import os
import sys
try:
    import pynotify
except:
    print "No model"

#管理设置壁纸，下载壁纸
class Manager:
    """docstring for Manager"""
    def __init__(self):
        try:
            pynotify.init("LoveWallpaperHD")
        except:
            print "done"
        #初始化读取    
        self._cf = ConfigParser.ConfigParser()
        self.usr_home = os.path.expanduser('~') + "/.config/lovewallpaper"
        self._cf.read("%s/config"%(self.usr_home))
        #获取下载路径
        self.download_path = self._cf.get("Path", "Download") 
        try:
            self.palform =  self._cf.get("Config", "platform") 
        except:
            self.palform =  self._cf.set('Config', 'platform', '')
            self._cf.write(open("%s/config" % (self.usr_home), "w"))
        
	if not self.palform:
	    self.palform = self.getPlatform()
        self.loadPlugin(self.palform)

    def getPlatform(self):
    
    	#判断MacOS
    	if sys.platform in ('mac', 'darwin'):
            return "Mac"
        
	#判断桌面环境
    	plaform = os.environ.get("DESKTOP_SESSION")
    	if plaform == "gnome":
	    return "Gnome"
	elif plaform == "kde-plasma":
	    return "KDE"
	elif plaform in ("xfce4", "xfce"):
	    return "XFCE"
	else:
	   return "Gnome-shell"

    def loadPlugin(self, platform):

        if platform == "KDE":
            from Plugin.KDE import WallpaperSetter, AutoSlide
        elif platform == "Gnome-shell":
            from Plugin.GnomeShell import WallpaperSetter, AutoSlide
        elif platform == "XFCE":
            from Plugin.Xfce import WallpaperSetter, AutoSlide
        elif platform == "Mac":
            from Plugin.Mac import WallpaperSetter, AutoSlide
        elif platform == "Gnome":
            from Plugin.Gnome import WallpaperSetter, AutoSlide
        else:
            try:
                    if os.environ['KDE_FULL_SESSION'] == 'true':
                        from Plugin.KDE import  WallpaperSetter, AutoSlide
            except Exception, e:
                        try:
                            if os.environ['XDG_CURRENT_DESKTOP'] == 'XFCE':
                                from Plugin.Xfce import WallpaperSetter, AutoSlide
                            elif  os.environ['XDG_CURRENT_DESKTOP'] == 'Pantheon':
                                from Plugin.Gnome import WallpaperSetter, AutoSlide
                            else:
                                from Plugin.Gnome import WallpaperSetter, AutoSlide
                        except Exception, e:
                             from Plugin.Gnome import WallpaperSetter, AutoSlide
                # print self.download_path
        self.Setter = WallpaperSetter()
        self.AutoSlider = AutoSlide()

    def _reload(self):
        self.usr_home = os.path.expanduser('~') + "/.config/lovewallpaper"
        self._cf.read("%s/config"%(self.usr_home))
        self.download_path = self._cf.get("Path", "Download") 

    def download(self,key,url):
        """docstring for download"""
        # print url
        self._reload()
        try:
            # print self.download_path+key+".jpg"
            #创建下载
            f = open(self.download_path+key+".jpg",'wb')
            f.write(urllib2.urlopen(url,timeout=15).read())
            f.close()
            return True
        except Exception, e:
            #各种出错提示
            try:
                n = pynotify.Notification(" 爱壁纸HD", "网络出现错误，请检查后重试")
                n.show()
            except:
                print "No model"
            return False


    def setWallpaper(self, key, url):
            self._reload()
            try:
                if os.path.exists(self.download_path+key + ".jpg"):
                    self.Setter.setWallpaper(self.download_path, key)
                else:
                    self.download(key,url)
                    self.Setter.setWallpaper(self.download_path, key)
            except Exception, e:
                try:
                    n = pynotify.Notification("爱壁纸HD", "很抱歉因为不明原因，设置失败，请尝试手动设置")
                    n.show()
                except:
                    print "False"

            finally:
                return True

    def puresetWallpaper(self, url):
         self.Setter.puresetWallpaper(url)
         return True

    def prepareFiles(self):
        self._reload()
        self.format = ['jpg','jpeg','png','bmp']
        self.files = []
        print "path is " + self.download_path
        for p,d,f in os.walk(self.download_path):
            for myfile in f:
                if myfile.split(".")[-1].lower() in self.format:
                    self.files.append(os.path.join(p, myfile))
        print self.files
        return self.files
