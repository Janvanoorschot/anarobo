import os
import re
import gzip
import json


class SittingWalker:

    SITTINGPATTERN = "^sittings-(\d+)-(\d+)-(\d+)\.gz$"

    def __init__(self, anodir, files):
        self.dir = anodir
        self.files = files
        self.cnt = -1
        self.handler = self.next_handler()

    @staticmethod
    def from_dir(cls, dir):
        sittingspattern = re.compile(SittingWalker.SITTINGPATTERN)
        files = sorted([file for file in os.listdir(dir) if sittingspattern.match(file)])
        return SittingWalker(dir, files)

    def from_files(anodir, files):
        return SittingWalker(anodir, files)

    def next_handler(self):
        if self.cnt < 0:
            self.cnt = 0
        else:
            self.cnt = self.cnt + 1
        if self.cnt >= len(self.files):
            raise StopIteration
        print(f"opening {self.files[self.cnt]}")
        return gzip.open(os.path.join(self.dir, self.files[self.cnt]), "rt")

    def __iter__(self):
        return self

    def __next__(self):
        line = self.handler.readline()
        if not line:
            self.handler.close()
            self.handler = self.next_handler()
            line = self.handler.readline()
        map = json.loads(line)
        return map

