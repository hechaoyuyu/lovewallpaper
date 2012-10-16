# -*- coding: utf-8 -*-

import json
import urllib2
import thread
import os
from gi.repository import Notify

from gi.repository import Gtk, Gdk, GdkPixbuf
from gi.repository.GdkPixbuf import Pixbuf

from ubuntutweak.modules  import TweakModule


class LovewallpaperHD(TweakModule):
    __title__ = _("Love Wallpaper HD")
    __desc__ = _('Browse online gallery and find your wallpaper')
#    __icon__ = 'love-wallpaper.png'
    __icon__ = 'love-wallpaper'
    __category__ = 'desktop'

    __author__ = 'kevinzhow <kevinchou.c@gmail.com>'
    __url__ = 'http://imkevin.me'
    __url_title__ = 'Kevin Blog'

    def __init__(self):
        TweakModule.__init__(self)
        Notify.init("LoveWallpaperHD")
        self.usr_home = os.path.expanduser('~')
        self.jsonman = JsonMan(Gdk.Screen.width(), Gdk.Screen.height())
        
            
        self.jsonman.get_json()
        
        self.image_list = self.jsonman.create_tryluck()

        self.image_model = Gtk.ListStore(Pixbuf, str)

        for image in self.image_list:
            thread.start_new_thread(self.add_image, (image,))

        self.image_view = Gtk.IconView.new_with_model(self.image_model)
        self.image_view.set_property('halign', Gtk.Align.CENTER)
        self.image_view.set_column_spacing(5)
        self.image_view.set_item_padding(5)
        self.image_view.set_item_width(175)
        self.image_view.set_pixbuf_column(0)
        self.image_view.connect("item-activated", self.set_wallpaper)
        
        label = Gtk.Label()
        label.set_markup("Powered by <a href=\"http://www.lovebizhi.com/linux\" "
                         "title=\"Click to find out more\">LoveWallpaper HD</a>.")
        label.set_line_wrap(True)
        
        fresh_btn =  Gtk.Button("TryLuck!")
        
        self.add_start(self.image_view, False, False, 0)
        self.add_start(fresh_btn, False, False, 0)
        self.add_start(label, False, False, 0)
        

        self.connect('size-allocate', self.on_size_allocate)
        fresh_btn.connect('clicked',self.load_imageview)
        
    def load_imageview(self,button):
        print "tryluck"
        self.jsonman.get_json()
        
        self.image_list = self.jsonman.create_tryluck()

        self.image_model = Gtk.ListStore(Pixbuf, str)

        for image in self.image_list:
            thread.start_new_thread(self.add_image, (image,))
        self.image_view.set_model(self.image_model)

    def on_size_allocate(self, width, allocation):
        if allocation.width > 0:
            self.image_view.set_columns(allocation.width / 195)

    def add_image(self, image):
        gtkimage = Gtk.Image()
        response = urllib2.urlopen(image.small)

        loader = GdkPixbuf.PixbufLoader()
        loader.write(response.read())
        loader.close()
        gtkimage.set_from_pixbuf(loader.get_pixbuf())
        self.image_model.append([gtkimage.get_pixbuf(), image.big])
        
    def download(self,url):
        f = open(self.usr_home+"/wallpaper.jpg",'wb')
        f.write(urllib2.urlopen(url,timeout=15).read())
        f.close()
        return self.usr_home+"/wallpaper.jpg"

    def set_wallpaper(self, view, path):
        url = self.image_model[path][1]
        url = self.download(url)
        print url
        os.system( "gsettings set org.gnome.desktop.background picture-uri \"file://%s\""%(url))
        n = Notify.Notification.new(" LoveWallpaperHD", "Success!",None)
        n.show()


class Picture:
    def __init__(self, small, big, num):
        self.small = small
        self.big = big
        self.key = num


class JsonMan:
    def __init__(self, screen_width=None, screen_height=None, parent=None):
        self.screen_height = str(screen_height)
        self.screen_width = str(screen_width)

    def get_json(self):
        json_init_url = "http://partner.lovebizhi.com/ubuntutweak.php?width=" + self.screen_width + "&height=" + self.screen_height
        fd = urllib2.urlopen(json_init_url, timeout=10).read().decode("utf-8")
        self.index = json.loads(fd)

    def create_tryluck(self):
        self.tryluck_list = []
        num = 0
        for tryluck_image in self.index:
            num += 1
            self.tryluck_list.append(Picture(tryluck_image["s"],
                                             tryluck_image['b'],
                                             str(num)))
        return self.tryluck_list
