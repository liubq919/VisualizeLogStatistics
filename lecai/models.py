from mongoengine import *
# Create your models here.


class ApiInfo(EmbeddedDocument):
    api = StringField(max_length=600, required=True)
    max = StringField(max_length=10, required=True)
    min = StringField(max_length=10, required=True)
    average = StringField(max_length=10)
    counter = IntField(required=True)


class AllApiInfo(Document):
    date = StringField(required=True)
    info = ListField(EmbeddedDocumentField(ApiInfo))


class EveryFifteenMinutes(EmbeddedDocument):
    hour = IntField(required=True)
    counter1 = IntField(required=True, default=0)
    counter2 = IntField(required=True, default=0)
    counter3 = IntField(required=True, default=0)
    counter4 = IntField(required=True, default=0)


class AllEveryFifteenMinutes(Document):
    date = StringField(required=True)
    info = ListField(EmbeddedDocumentField(EveryFifteenMinutes))


class AllEveryFifMinLoginCount(Document):
    date = StringField(required=True)
    info = ListField(EmbeddedDocumentField(EveryFifteenMinutes))


class LecaiApiCounterInfo(Document):
    date = StringField(required=True)
    times = IntField(required=True, default=0)


class LecaiLoginCountInfo(Document):
    date = StringField(required=True)
    times = IntField(required=True, default=0)


class EventLogCitiesArea(EmbeddedDocument):
    # the name of City
    name = StringField(max_length=40, required=True)
    value = IntField(required=True)


class EventLogProvincesArea(EmbeddedDocument):
    # the name of City
    name = StringField(max_length=40, required=True)
    value = IntField(required=True)
    info = ListField(EmbeddedDocumentField(EventLogCitiesArea))


class EventLogProvincesAreaInfo(Document):
    date = StringField(max_length=20, required=True)
    info = ListField(EmbeddedDocumentField(EventLogProvincesArea))
