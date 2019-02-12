class StorylineItem:

    def __init__(self, id):
        self.id = id
        self.name = None
        self.challenge = None
        self.storyline = None

    def to_map(self):
        map = {}
        map['id'] = self.id
        map['name'] = self.name
        if self.challenge:
            map['challenge'] = self.challenge.id
        else:
            map['challenge'] = ''
        if self.storyline:
            map['storyline'] = self.storyline.id
        else:
            map['storyline'] = ''
        return map

    def fullname(self):
        return self.storyline.fullname() + "/" + self.name

    def type(self):
        return 'StorylineItem'

    @classmethod
    def from_map(cls, map, cache):
        item = StorylineItem(map.get('id', '0'))
        item.name = map.get('name', '')
        c = map.get('challenge', "")
        if c and c !="":
            item.challenge = cache.get_by_id('Challenge', c)
        else:
            item.challenge = None
        item.storyline = cache.get_by_id('Storyline', map.get('storyline', ""))
        return item


class Storyline:

    def __init__(self, id):
        self.id = id
        self.name = None
        self.course = None

    def to_map(self):
        map = {}
        map['id'] = self.id
        map['name'] = self.name
        if self.course:
            map['course'] = self.course.id
        else:
            map['course'] = ''
        return map

    def fullname(self):
        return self.course.fullname() + "/" + self.name

    def type(self):
        return 'Storyline'

    @classmethod
    def from_map(cls, map, cache):
        item = Storyline(map.get('id', '0'))
        item.name = map.get('name', '')
        item.course = cache.get_by_id('Course', map.get('course', ""))
        return item


class Course:

    def __init__(self, id):
        self.id = id
        self.name = None

    def to_map(self):
        map = {}
        map['id'] = self.id
        map['name'] = self.name
        return map

    def fullname(self):
        return self.name

    def type(self):
        return 'Course'

    @classmethod
    def from_map(cls, map, cache):
        item = Course(map.get('id', '0'))
        item.name = map.get('name', '')
        return item
