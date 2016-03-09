# -*- coding: utf-8 -*-
from mongoengine import *

__author__ = 'liubq'


class EveryFifteenMinutes(EmbeddedDocument):
    hour = IntField(required=True)
    counter1 = IntField(required=True, default=0)
    counter2 = IntField(required=True, default=0)
    counter3 = IntField(required=True, default=0)
    counter4 = IntField(required=True, default=0)


class QidaEveryFifMinLoginCount(Document):
    date = StringField(required=True)
    info = ListField(EmbeddedDocumentField(EveryFifteenMinutes))


class QidaOSInfo(Document):
    date = StringField(required=True)
    # desktop os
    windowsxp = IntField(required=True, default=0)
    windowsvista = IntField(required=True, default=0)
    windows7 = IntField(required=True, default=0)
    windows8 = IntField(required=True, default=0)
    windows8_1 = IntField(required=True, default=0)
    windows10 = IntField(required=True, default=0)
    windowsOthers = IntField(required=True, default=0)
    windows = IntField(required=True, default=0)
    osx = IntField(required=True, default=0)
    # mobile/tablet os
    iPhone = IntField(required=True, default=0)
    iPad = IntField(required=True, default=0)
    android = IntField(required=True, default=0)
    # other os
    osOthers = IntField(required=True, default=0)

    meta = {
        'collection': 'qida_os_info'
    }


class QidaBrowserInfo(Document):
    date = StringField(required=True)
    ie6 = IntField(required=True, default=0)
    ie7 = IntField(required=True, default=0)
    ie8 = IntField(required=True, default=0)
    ie9 = IntField(required=True, default=0)
    ie10 = IntField(required=True, default=0)
    ie11 = IntField(required=True, default=0)
    edge = IntField(required=True, default=0)
    firefox = IntField(required=True, default=0)
    chrome = IntField(required=True, default=0)
    safari = IntField(required=True, default=0)
    others = IntField(required=True, default=0)


class QidaLoginCount(Document):
    date = StringField(required=True)
    times = IntField(required=True, default=0)
