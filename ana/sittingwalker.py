import os
import re
import gzip
import json


class SittingWalker:

    SITTINGPATTERN = "^sittings-(\d+)-(\d+)-(\d+)\.gz$"

    def __init__(self, dir):
        self.dir = dir
        self.sittingpattern = re.compile(self.SITTINGPATTERN)
        self.files = sorted([file for file in os.listdir(self.dir) if self.sittingpattern.match(file)])
        self.cnt = 0
        self.handler = gzip.open(os.path.join(self.dir, self.files[self.cnt]), "rt")

    def __iter__(self):
        return self

    def __next__(self):
        line = self.handler.readline()
        if not line:
            print(f"opening {self.files[self.cnt]}")
            self.handler.close()
            self.cnt = self.cnt + 1
            if self.cnt >= len(self.files):
                raise StopIteration
            self.handler = gzip.open(os.path.join(self.dir, self.files[self.cnt]), "rt")
            line = self.handler.readline()
        map = json.loads(line)
        return map

