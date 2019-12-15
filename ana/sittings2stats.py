import ana
from datetime import date
from datetime import datetime
import os

def sli_stats(dir):
    """ Calculate the Storyline-items (sli) statistics given the sitting-data calculated
    from the Robomind Academy. The calculated sli statistics consist of
    the buckets:
      . by weeknumber, per year c
      . by day of the week, per year
      . by hour of the day, per year
    In each bucket the following counts are maintained:
      . all
      . ano student
      . ident classless student
      . class-student
      . teacher
    """
    walker = ana.SittingWalker(dir)
    dao = ana.RoboDAO(dir)
    stats = {}

    for sitting in walker:
        donetoffset=0
        sli = None
        person = sitting['person']
        stamp = datetime.strptime(sitting['starttime'], "%Y-%m-%dT%H:%M:%SZ")
        print(f"here {stamp}")

    pandastats = {}
    for sli in stats:
        cumtime = []
        count = []
        person = []
        completed = []
        for p in stats[sli]:
            sts = stats[sli][p]
            if sts['completed']:
                cumtime.append(sts['cumtime'])
                count.append(sts['count'])
                person.append(sts['person'])
        # if sli.startswith('Basis'):
        pandastats[sli] = {'cumtime': cumtime, 'count': count, 'person': person}
    return pandastats


def dump_storylines(np):
    """Dump the storylines from the sli-statistics."""
    slis = set()
    for sli in np.keys():
        slis.add(sli)
    slis = sorted(slis)
    for sli in slis:
        print(f"'{sli}',")


def generate_one_csv(np, handle, arr):
    """generate the CSV content from thje sli-statistics array"""
    import csv
    writer = csv.writer(handle)
    writer.writerow(["storyline", "person", "cumtime", "count"])
    for storyline in arr:
        cumtimes = np[storyline]['cumtime']
        counts = np[storyline]['count']
        persons = np[storyline]['person']
        for idx, person in enumerate(persons):
            cumtime = cumtimes[idx]
            count = counts[idx]
            writer.writerow([storyline, person, cumtime, count])


def generate_csv(np, dirname):
    """create compressed csv files for all sli-statistics"""
    import gzip
