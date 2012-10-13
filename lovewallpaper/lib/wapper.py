# -*- coding: utf-8 -*-
from PySide import QtCore
from PySide import QtGui
from PySide.QtCore import Qt

class UserImageWapper(QtCore.QObject):
    """docstring for UserImageWapper"""
    def __init__(self, image):
        QtCore.QObject.__init__(self)
        self._image = image

    def _url(self):
        return self._image.url

    def _index(self):
        return self._image.index
        
    changed = QtCore.Signal()

    url = QtCore.Property(unicode, _url, notify=changed)
    index = QtCore.Property(unicode, _index, notify=changed)

class UserImageListModel(QtCore.QAbstractListModel):
    URL_ROLE = Qt.UserRole + 1
    INDEX_ROLE = Qt.UserRole + 2


    def __init__(self, images, parent=None):
        super(UserImageListModel, self).__init__(parent)
        self._images = images
        keys = {}
        keys[UserImageListModel.URL_ROLE] = "url"
        keys[UserImageListModel.INDEX_ROLE] = "index"

        self.setRoleNames(keys)

    def rowCount(self, index):
        return len(self._images)


    def data(self, index, role):
        if not index.isValid():
            return None

        if index.row() > len(self._images):
            return None

        image = self._images[index.row()]
        if role == UserImageListModel.URL_ROLE:
            return image.url
        elif role == UserImageListModel.INDEX_ROLE:
            return image.index
        else:
            return None


class SpecialWrapper(QtCore.QObject):
    def __init__(self, special):
        QtCore.QObject.__init__(self)
        self._special = special
 
    def _description(self):
        return self._special.description
    def _name(self):
        return self._special.name
    def _small(self):
        return self._special.image["small"]
    def _detail(self):
        return self._special.detail
    def _big(self):
        return self._special.image["big"]

 
    changed = QtCore.Signal()
 
    small = QtCore.Property(unicode, _small, notify=changed)
    name = QtCore.Property(unicode, _name, notify=changed)
    description = QtCore.Property(unicode, _description, notify=changed)
    detail = QtCore.Property(unicode, _detail, notify=changed)
    big = QtCore.Property(unicode, _big, notify=changed)

class SpecialListModel(QtCore.QAbstractListModel):
    SMALL_ROLE = Qt.UserRole + 1
    NAME_ROLE = Qt.UserRole + 2
    DESCRIPTION_ROLE = Qt.UserRole + 3
    DETAIL_ROLE = Qt.UserRole + 4
    BIG_ROLE = Qt.UserRole + 5

    def __init__(self, specials, parent=None):
        super(SpecialListModel, self).__init__(parent)
        self._specials = specials
        keys = {}
        keys[SpecialListModel.SMALL_ROLE] = "small"
        keys[SpecialListModel.BIG_ROLE] = "big"
        keys[SpecialListModel.NAME_ROLE] = "name"
        keys[SpecialListModel.DESCRIPTION_ROLE] = "description"
        keys[SpecialListModel.DETAIL_ROLE] = "detail"
        self.setRoleNames(keys)

    def rowCount(self, index):
        return len(self._specials)


    def data(self, index, role):
        if not index.isValid():
            return None

        if index.row() > len(self._specials):
            return None

        special = self._specials[index.row()]
        if role == SpecialListModel.SMALL_ROLE:
            return special.small
        elif role == SpecialListModel.NAME_ROLE:
            return special.name
        elif role == SpecialListModel.DESCRIPTION_ROLE:
            return special.description
        elif role == SpecialListModel.DETAIL_ROLE:
            return special.detail
        if role == SpecialListModel.BIG_ROLE:
            return special.big
        else:
            return None



class EverydayWrapper(QtCore.QObject):
    def __init__(self, everyday):
        QtCore.QObject.__init__(self)
        self._everyday = everyday
 
    def _image(self):
        return self._everyday.image
    def _name(self):
        return self._everyday.name
    def _total(self):
        return str(self._everyday.total)
    def _url(self):
        return self._everyday.url

 
    changed = QtCore.Signal()
 
    image = QtCore.Property(unicode, _image, notify=changed)
    name = QtCore.Property(unicode, _name, notify=changed)
    total = QtCore.Property(unicode, _total, notify=changed)
    url = QtCore.Property(unicode, _url, notify=changed)

class EverydayListModel(QtCore.QAbstractListModel):
    IMAGE_ROLE = Qt.UserRole + 1
    NAME_ROLE = Qt.UserRole + 2
    TOTAL_ROLE = Qt.UserRole + 3
    URL_ROLE = Qt.UserRole + 4

    def __init__(self, everydays, parent=None):
        super(EverydayListModel, self).__init__(parent)
        self._everydays = everydays
        keys = {}
        keys[EverydayListModel.IMAGE_ROLE] = "image"
        keys[EverydayListModel.NAME_ROLE] = "name"
        keys[EverydayListModel.TOTAL_ROLE] = "total"
        keys[EverydayListModel.URL_ROLE] = "url"
        self.setRoleNames(keys)

    def rowCount(self, index):
        return len(self._everydays)


    def data(self, index, role):
        if not index.isValid():
            return None

        if index.row() > len(self._everydays):
            return None

        everyday = self._everydays[index.row()]
        if role == EverydayListModel.IMAGE_ROLE:
            return everyday.image
        elif role == EverydayListModel.NAME_ROLE:
            return everyday.name
        elif role == EverydayListModel.TOTAL_ROLE:
            return everyday.total
        elif role == EverydayListModel.URL_ROLE:
            return everyday.url
        else:
            return None




class TagWrapper(QtCore.QObject):
    def __init__(self, tag):
        QtCore.QObject.__init__(self)
        self._tag = tag
 
    def _tid(self):
        return self._tag.tid
    def _name(self):
        return self._tag.name
    def _total(self):
        return str(self._tag.total)
    def _url(self):
        return self._tag.url

 
    changed = QtCore.Signal()
 
    tid = QtCore.Property(unicode, _tid, notify=changed)
    name = QtCore.Property(unicode, _name, notify=changed)
    total = QtCore.Property(unicode, _total, notify=changed)
    url = QtCore.Property(unicode, _url, notify=changed)

class TagListModel(QtCore.QAbstractListModel):
    TID_ROLE = Qt.UserRole + 1
    NAME_ROLE = Qt.UserRole + 2
    TOTAL_ROLE = Qt.UserRole + 3
    URL_ROLE = Qt.UserRole + 4

    def __init__(self, tags, parent=None):
        super(TagListModel, self).__init__(parent)
        self._tags = tags
        keys = {}
        keys[TagListModel.TID_ROLE] = "tid"
        keys[TagListModel.NAME_ROLE] = "name"
        keys[TagListModel.TOTAL_ROLE] = "total"
        keys[TagListModel.URL_ROLE] = "url"
        self.setRoleNames(keys)

    def rowCount(self, index):
        return len(self._tags)


    def data(self, index, role):
        if not index.isValid():
            return None

        if index.row() > len(self._tags):
            return None

        img = self._tags[index.row()]
        if role == TagListModel.TID_ROLE:
            return img.tid
        elif role == TagListModel.NAME_ROLE:
            return img.name
        elif role == TagListModel.TOTAL_ROLE:
            return img.total
        elif role == TagListModel.URL_ROLE:
            return img.url
        else:
            return None

class CategoryWrapper(QtCore.QObject):
    def __init__(self, category):
        QtCore.QObject.__init__(self)
        self._category = category
 
    def _tid(self):
        return str(self._category.tid)
    def _name(self):
        return self._category.name
    def _bgimage(self):
        return self._category.bgimage
    def _url(self):
        return self._category.url

 
    changed = QtCore.Signal()
 
    tid = QtCore.Property(unicode, _tid, notify=changed)
    name = QtCore.Property(unicode, _name, notify=changed)
    bgimage = QtCore.Property(unicode, _bgimage, notify=changed)
    url = QtCore.Property(unicode, _url, notify=changed)

class CategoryListModel(QtCore.QAbstractListModel):
    TID_ROLE = Qt.UserRole + 1
    NAME_ROLE = Qt.UserRole + 2
    bgimage_ROLE = Qt.UserRole + 3
    URL_ROLE = Qt.UserRole + 4

    def __init__(self, categorys, parent=None):
        super(CategoryListModel, self).__init__(parent)
        self._categorys = categorys
        keys = {}
        keys[CategoryListModel.TID_ROLE] = "tid"
        keys[CategoryListModel.NAME_ROLE] = "name"
        keys[CategoryListModel.bgimage_ROLE] = "bgimage"
        keys[CategoryListModel.URL_ROLE] = "url"
        self.setRoleNames(keys)

    def rowCount(self, index):
        return len(self._categorys)


    def data(self, index, role):
        if not index.isValid():
            return None

        if index.row() > len(self._categorys):
            return None

        img = self._categorys[index.row()]
        if role == CategoryListModel.TID_ROLE:
            return img.tid
        elif role == CategoryListModel.NAME_ROLE:
            return img.name
        elif role == CategoryListModel.bgimage_ROLE:
            return img.bgimage
        elif role == CategoryListModel.URL_ROLE:
            return img.url
        else:
            return None


class PictureWrapper(QtCore.QObject):
    def __init__(self, picture):
        QtCore.QObject.__init__(self)
        self._picture = picture
 
    def _key(self):
        return str(self._picture.key)
    def _small(self):
        return str(self._picture.small)
    def _big(self):
        return str(self._picture.big)
    def _original(self):
        return str(self._picture.original)
    def _detail(self):
        return str(self._picture.detail)
 
    changed = QtCore.Signal()
 
    key = QtCore.Property(unicode, _key, notify=changed)
    small = QtCore.Property(unicode, _small, notify=changed)
    big = QtCore.Property(unicode, _big, notify=changed)
    original = QtCore.Property(unicode, _original, notify=changed)
    detail = QtCore.Property(unicode, _detail, notify=changed)

class PhotoListModel(QtCore.QAbstractListModel):
    SMALL_ROLE = Qt.UserRole + 1
    BIG_ROLE = Qt.UserRole + 2
    ORIGINAL_ROLE = Qt.UserRole + 3
    DETAIL_ROLE = Qt.UserRole + 4
    KEY_ROLE = Qt.UserRole + 5
    BUDDY_ROLE = Qt.UserRole + 6

    def __init__(self, photos, parent=None):
        super(PhotoListModel, self).__init__(parent)
        self._photos = photos
        keys = {}
        keys[PhotoListModel.SMALL_ROLE] = "small"
        keys[PhotoListModel.BIG_ROLE] = "big"
        keys[PhotoListModel.ORIGINAL_ROLE] = "original"
        keys[PhotoListModel.DETAIL_ROLE] = "detail"
        keys[PhotoListModel.KEY_ROLE] = "key"
        keys[PhotoListModel.BUDDY_ROLE] = "buddy"
        self.setRoleNames(keys)

    def rowCount(self, index):
        return len(self._photos)




    def data(self, index, role):
        if not index.isValid():
            return None

        if index.row() > len(self._photos):
            return None

        img = self._photos[index.row()]
        if role == PhotoListModel.SMALL_ROLE:
            return img.small
        elif role == PhotoListModel.BIG_ROLE:
            return img.big
        elif role == PhotoListModel.ORIGINAL_ROLE:
            return img.original
        elif role == PhotoListModel.DETAIL_ROLE:
            return img.detail
        elif role == PhotoListModel.KEY_ROLE:
            return img.key
        elif role == PhotoListModel.BUDDY_ROLE:
            return index.row()
        else:
            return None

class ImageTagWrapper(QtCore.QObject):
    def __init__(self, imagetag):
        QtCore.QObject.__init__(self)
        self._imagetag = imagetag
 
    def _image(self):
        return self._imagetag.image
    def _name(self):
        return self._imagetag.name
    def _url(self):
        return self._imagetag.url

 
    changed = QtCore.Signal()
 
    image = QtCore.Property(unicode, _image, notify=changed)
    name = QtCore.Property(unicode, _name, notify=changed)
    url = QtCore.Property(unicode, _url, notify=changed)

class ImageTagListModel(QtCore.QAbstractListModel):
    IMAGE_ROLE = Qt.UserRole + 1
    NAME_ROLE = Qt.UserRole + 2
    URL_ROLE = Qt.UserRole + 3

    def __init__(self, imagetags, parent=None):
        super(ImageTagListModel, self).__init__(parent)
        self._imagetags = imagetags
        keys = {}
        keys[ImageTagListModel.IMAGE_ROLE] = "image"
        keys[ImageTagListModel.NAME_ROLE] = "name"
        keys[ImageTagListModel.URL_ROLE] = "url"
        self.setRoleNames(keys)

    def rowCount(self, index):
        return len(self._imagetags)


    def data(self, index, role):
        if not index.isValid():
            return None

        if index.row() > len(self._imagetags):
            return None

        imagetag = self._imagetags[index.row()]
        if role == ImageTagListModel.IMAGE_ROLE:
            return imagetag.image
        elif role == ImageTagListModel.NAME_ROLE:
            return imagetag.name
        elif role == ImageTagListModel.URL_ROLE:
            return imagetag.url
        else:
            return None

class PropertyWrapper(QtCore.QObject):
    def __init__(self, myproperty):
        QtCore.QObject.__init__(self)
        self._myproperty = myproperty
 
    def _key(self):
        return self._myproperty.key
    def _value(self):
        return self._myproperty.value

 
    changed = QtCore.Signal()
 
    key = QtCore.Property(unicode, _key, notify=changed)
    value = QtCore.Property(unicode, _value, notify=changed)

class PropertyListModel(QtCore.QAbstractListModel):
    KEY_ROLE = Qt.UserRole + 1
    VALUE_ROLE = Qt.UserRole + 2


    def __init__(self, mypropertyes, parent=None):
        super(PropertyListModel, self).__init__(parent)
        self._imypropertyes = mypropertyes
        keys = {}
        keys[PropertyListModel.KEY_ROLE] = "key"
        keys[PropertyListModel.VALUE_ROLE] = "value"
        self.setRoleNames(keys)

    def rowCount(self, index):
        return len(self._imypropertyes)


    def data(self, index, role):
        if not index.isValid():
            return None

        if index.row() > len(self._imypropertyes):
            return None

        kv = self._imypropertyes[index.row()]
        if role == PropertyListModel.KEY_ROLE:
          
            return kv.key

        elif role == PropertyListModel.VALUE_ROLE:

            return kv.value
        else:
            return None

