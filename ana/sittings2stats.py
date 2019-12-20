import ana
from datetime import datetime
import os, gzip, csv

CATEGORIES = {
    'weekofyear': 'weekofyear',
    'dayofweek': 'dayofweek',
    'hourofday': 'hourofday'
}

def sli_stats(dir):
    """ Calculate the Storyline-items (sli) statistics given the sitting-data calculated
    from the Robomind Academy. The calculated sli statistics consist of
    the buckets:
      . by weeknumber, per year
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
        person = dao.get(sitting['person'])
        stamp = datetime.strptime(sitting['starttime'], "%Y-%m-%dT%H:%M:%SZ")
        [year, weekno, dayofweek] = stamp.isocalendar()
        ano =  ident = inclass = teacher = 0
        if person.isteacher:
            teacher = 1
        elif len(person.teachers) > 0:
            inclass =  1
        elif person.id[0] == 'A':
            ano = 1
        else:
            ident = 1
        # score [all, ano, indent, inclass, teacher]
        score = [1, ano, ident, inclass, teacher]
        do_score(stats, 'weekofyear', year, weekno, score)
        do_score(stats, 'dayofweek', year, dayofweek, score)
        do_score(stats, 'hourofday', year, stamp.hour, score)
    return stats

def do_score(stats, type, year, bucket, score):
    if type not in stats:
        tcoll = {}
        stats[type] = tcoll
    else:
        tcoll = stats[type]
    if year not in tcoll:
        ycoll = {}
        tcoll[year] = ycoll
    else:
        ycoll = tcoll[year]
    if bucket not in ycoll:
        cscore = [0,0,0,0,0]
        ycoll[bucket] = cscore
    else:
        cscore = ycoll[bucket]
    for i, val in enumerate(score):
        cscore[i] += val

def generate_csv(allstats, dirname):
    """create compressed csv files for all """
    for type in CATEGORIES.keys():
        filename = os.path.join(dirname, f"stats_{type}.gz")
        stats = allstats[type]
        with gzip.open(filename, 'wt') as handle:
            writer = csv.writer(handle)
            writer.writerow(["year", CATEGORIES[type], "all", "ano", "ident", "inclass", "teacher"])
            for year in sorted(stats.keys()):
                ystats = stats[year]
                for val in sorted(ystats.keys()):
                    row = [year, val] + ystats[val]
                    writer.writerow(row)

