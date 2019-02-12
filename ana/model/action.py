class Action:

    def __init__(self, type):
        self.type = type
        self.toffset = 0
        self.storylineitem = None
        self.details = {}

    def to_map(self):
        map = {}
        map['type'] = self.type
        map['toffset'] = self.toffset
        map['storylineitem'] = self.storylineitem.id if self.storylineitem else None
        map['details'] = self.details
        return map

    def type(self):
        return 'Action'

    @classmethod
    def from_map(cls, map, cache):
        item = Action(map.get('type', 'unknown'))
        item.toffset = map.get('toffset', 0)
        item.storylineitem = cache.get_by_id('StorylineItem', map.get('storylineitem', ""))
        item.details = map.get('details', None)
        return item



