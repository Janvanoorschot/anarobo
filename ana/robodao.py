import gzip
import os
import json
from .model import Sitting, Action, Teacher, IPupil, APupil, Storyline, StorylineItem, Course, Challenge


class RoboDAO:
    """Gives access to the Robo model objects as defined in the model module. Objects
    are preloaded from the ano-directory which contains the Robomind Academy
    sitting datafiles"""

    TYPE2NAME = {
        'Action': None,
        'Sitting': None,
        'APupil': "apupil",
        'IPupil': "ipupil",
        'Teacher': "teacher",
        'Challenge': "challenge",
        'Course': "course",
        'Storyline': "storyline",
        'StorylineItem': "storylineitem"
    }

    TYPE2CLASS = {
        'Action': Action,
        'Sitting': Sitting,
        'APupil': APupil,
        'IPupil': IPupil,
        'Teacher': Teacher,
        'Challenge': Challenge,
        'Course': Course,
        'Storyline': Storyline,
        'StorylineItem': StorylineItem
    }

    def __init__(self, anodir):
        self.anodir = anodir
        self.caches = {}
        for otype, fname in self.TYPE2NAME.items():
            if self.TYPE2NAME[otype]:
                self.caches[otype] = {}
        self.preload()

    def preload(self):
        """Preload model objects as defined in the model module from the
        anonymised sittings file in the ano-directory."""
        # load the objects
        for otype, fname in self.TYPE2NAME.items():
            if fname:
                path = os.path.join(self.anodir, fname + ".gz")
                if os.path.isfile(path):
                    with gzip.open(path, "rt") as handler:
                        for line in handler:
                            omap = json.loads(line)
                            cls = self.TYPE2CLASS[otype]
                            item = cls.from_map(omap, self)
                            self.caches[otype][item.id] = item

    def get(self, id):
        type = self._id2type(id)
        return self.get_by_id(type, id)

    def get_by_id(self, otype, id):
        if otype not in self.TYPE2NAME:
            raise KeyError("no such type %s" % (otype,))
        if id in self.caches[otype]:
            return self.caches[otype][id]
        else:
            print(f"request for non-existing object: {otype}/{id}")
            return None

    def _id2type(self, id):
        import re
        return re.search(r"\D+", id).group()


