import datetime
from ..utils import string2date, date2string
from . import Action


class Sitting:

    def __init__(self, id):
        self.id = id
        self.person = None
        self.starttime = None
        self.endtime = None
        self.active = True
        self.realsitting = False
        self.actions = []

    def add_action(self, action):
        self.actions.append(action)
        if action.type == 'runscript':
            self.realsitting = True

    def to_map(self):
        map = {}
        map['id'] = self.id
        map['person'] = self.person.id
        map['starttime'] = date2string(self.starttime)
        map['endtime'] = date2string(self.endtime)
        map['active'] = self.active
        map['realsitting'] = self.realsitting
        map['actions'] = []
        for action in self.actions:
            map['actions'].append(action.to_map())
        return map

    def type(self):
        return 'Sitting'

    @classmethod
    def from_map(cls, map, cache):
        item = Sitting(map.get('id', '0'))
        personid = map.get('person', '0')
        if personid.startswith('APupil'):
            item.person = cache.get_by_id('APupil', personid)
        elif personid.startswith('IPupil'):
            item.person = cache.get_by_id('IPupil', personid)
        elif personid.startswith('Teacher'):
            item.person = cache.get_by_id('Teacher', personid)
        item.starttime = string2date(map.get('starttime', date2string(datetime.datetime.now())))
        item.endtime = string2date(map.get('endtime', date2string(datetime.datetime.now())))
        item.active = map.get('active', False)
        item.realsitting = map.get('realsitting', True)
        for action in map.get('actions', []):
            item.actions.append(Action.from_map(action, cache))
        return item
