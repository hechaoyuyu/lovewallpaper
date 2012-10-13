# -*- coding: utf-8 -*-
#图片数据结构
class Picture:
    def __init__(self,key,small,big,original,detail):
        self.key = key
        self.small = small
        self.big = big
        self.original = original
        self.detail = detail

#图片详细信息数据

class Detail:
    """docstring for Detail"""
    def __init__(self, name, key, image, dlview,data, tags):
        self.name = name
        self.key = key
        self.image = image
        self.dlview = dlview
        self.data =data
        self.tags = tags

class Property:
    def __init__(self, key, value):
        self.key = key
        self.value = value

#标签数据结构
class Tag:
    def __init__(self,tid,name,total,url):
        self.tid = tid
        self.name = name
        self.total = total
        self.url = url

class TagCloumn:
    """docstring for TagCloumn"""
    def __init__(self, name, link, data):
        self.name = name
        self.link = link
        self.data = data

        

#目录数据结构
class Category:
    """docstring for Categroy"""
    def __init__(self, tid, name, bgimage, url):
        self.tid = tid
        self.name = name
        self.bgimage = bgimage
        self.url = url

#目录下的栏目的数据结构
class Column:
    """docstring for Clounm"""
    def __init__(self, name, color, url,link, data, colorlist, tags):
        self.name = name
        self.color = color
        self.url = url
        self.link = link
        self.data = data
        self.colorlist = colorlist
        self.tags = tags

#每日数据结构
class Everyday:
    """docstring for Everyday"""
    def __init__(self, image, name, url, total):
        self.image = image
        self.name = name
        self.url = url
        self.total = total

class EverydayClounm:
    """docstring for EverydayClounm"""
    def __init__(self, name, link, data):
        self.name = name
        self.link = link
        self.data = data

#专题数据模型
class Special:
    """docstring for Special"""
    def __init__(self, name, description,image ,detail):
        self.name = name
        self.description = description
        self.image = image
        self.detail = detail

class SpecialClounm:
    """docstring for SpecialClounm"""
    def __init__(self,name, description, image, data ):
        self.name = name
        self.description = description
        self.image = image
        self.data = data

#ImageTag
class ImageTag:
    """docstring for Everyday"""
    def __init__(self, image, name, url):
        self.image = image
        self.name = name
        self.url = url
