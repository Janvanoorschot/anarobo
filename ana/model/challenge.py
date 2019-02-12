class Challenge:

    def __init__(self, id):
        self.id = id
        self.name = None

    def to_map(self):
        map = {}
        map['id'] = self.id
        map['name'] = self.name
        return map

    def type(self):
        return 'Challenge'

    @classmethod
    def from_map(cls, map, cache):
        item = Challenge(map.get('id', '0'))
        item.name = map.get('name', '')
        return item



