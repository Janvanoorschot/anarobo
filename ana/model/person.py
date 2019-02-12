import datetime
from ..utils import string2date, date2string


class Person:

    def __init__(self, id):
        self.id = id
        self.locale = None
        self.birthdate = None
        self.registrationdate = None
        self.starttime = None
        self.endtime = None
        self.isteacher = False
        self.teachers = set()

    def to_map(self):
        map = {}
        map['id'] = self.id
        map['locale'] = self.locale
        map['registrationdate'] = date2string(self.registrationdate)
        map['starttime'] = date2string(self.starttime)
        map['endtime'] = date2string(self.endtime)
        map['isteacher'] = self.isteacher
        map['teachers'] = sorted(list(self.teachers))
        return map

    @classmethod
    def from_map(cls, item, map, cache):
        item.locale = map.get('locale', "en-GB")
        item.nick = map.get('nick', "QoM")
        item.registrationdate = string2date(map.get('registrationdate', datetime.datetime.now()))
        item.starttime = string2date(map.get('starttime', date2string(datetime.datetime.now())))
        item.endtime = string2date(map.get('endtime', date2string(datetime.datetime.now())))
        item.isteacher = map.get('isteacher', False)
        item.teachers = set(map.get('teachers', []))


class APupil(Person):

    def __init(self, id):
        super().__init__(id)

    @classmethod
    def from_map(cls, map, cache):
        item = APupil(map.get('id', '0'))
        super().from_map(item, map, cache)
        return item

    def type(self):
        return 'APupil'


class IPupil(Person):

    def __init(self, id):
        super().__init__(id)

    @classmethod
    def from_map(cls, map, cache):
        item = IPupil(map.get('id', '0'))
        super().from_map(item, map, cache)
        return item

    def type(self):
        return 'IPupil'


class Teacher(Person):

    def __init(self, id):
        super().__init__(id)

    @classmethod
    def from_map(cls, map, cache):
        item = Teacher(map.get('id', '0'))
        super().from_map(item, map, cache)
        return item

    def type(self):
        return 'Teacher'

