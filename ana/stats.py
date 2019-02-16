import pandas as pd
import ana

# getting to run:
# import ana.stats
# np = ana.stats.sli_stats(ana.stats.SITTINGSDIR)
# stats = ana.stats.calc_stats(np)
# means = ana.stats.calc_means(np)


SITTINGSDIR = '/data/robodata/ano'
STORYLINES = [
    'Basis_1/Getting started/1',
    'Basis_1/Getting started/2',
    'Basis_1/Getting started/3',
    'Basis_1/Getting started/4',
    'Basis_1/Getting started/5',
    'Basis_1/Getting started/6',
    'Basis_1/Getting started/7',
    'Basis_1/Guarding and slalom/1',
    'Basis_1/Guarding and slalom/2',
    'Basis_1/Guarding and slalom/3',
    'Basis_1/Guarding and slalom/4',
    'Basis_1/Guarding and slalom/5',
    'Basis_1/Guarding and slalom/6',
    'Basis_1/Guarding and slalom/7',
    'Basis_1/Painting floors/1',
    'Basis_1/Painting floors/2',
    'Basis_1/Painting floors/3',
    'Basis_1/Painting floors/4',
    'Basis_1/Painting floors/5',
    'Basis_1/Painting floors/6',
    'Basis_1/Painting floors/7',
    'Basis_1/Factories/1',
    'Basis_1/Factories/2',
    'Basis_1/Factories/3',
    'Basis_1/Factories/4',
    'Basis_1/Factories/5',
    'Basis_1/Factories/6',
    'Basis_1/Navigating/1',
    'Basis_1/Navigating/2',
    'Basis_1/Navigating/3',
    'Basis_1/Navigating/4',
    'Basis_1/Navigating/5',
    'Basis_1/Navigating/6',
    'Basis_1/Navigating/7',
    'Basis_1/Tracking and tracing/1',
    'Basis_1/Tracking and tracing/2',
    'Basis_1/Tracking and tracing/3',
    'Basis_1/Tracking and tracing/4',
    'Basis_1/Tracking and tracing/5',
    'Basis_1/Line following/1',
    'Basis_1/Line following/2',
    'Basis_1/Line following/3',
    'Basis_1/Line following/4',
    'Basis_1/Line following/5',
    'Basis_2/Tracking and tracing 2/1',
    'Basis_2/Tracking and tracing 2/2',
    'Basis_2/Tracking and tracing 2/3',
    'Basis_2/Tracking and tracing 2/4',
    'Basis_2/Tracking and tracing 2/5',
    'Basis_2/Tracking and tracing 2/6',
    'Basis_2/Tracking and tracing 2/7',
    'Basis_2/Tracking and tracing 2/8',
    'Basis_2/Mazes/1',
    'Basis_2/Mazes/2',
    'Basis_2/Mazes/3',
    'Basis_2/Mazes/4',
    'Basis_2/Mazes/5',
    'Basis_2/Mazes/6',
    'Basis_2/Secret language/1',
    'Basis_2/Secret language/3',
    'Basis_2/Secret language/4',
    'Basis_2/Secret language/5',
    'Basis_2/Secret language/6',
    'Basis_2/Secret language/7',
    'Basis_2/Secret language/8',
    'Basis_2/Secret language/9',
    'Basis_2/Secret language/10',
    'Basis_2/Drawing portraits/1',
    'Basis_2/Drawing portraits/3',
    'Basis_2/Drawing portraits/4',
    'Basis_2/Drawing portraits/5',
    'Basis_2/Drawing portraits/6',
    'Basis_2/Drawing portraits/7',
    'Basis_2/Drawing portraits/8',
    'Basis_2/Reading barcodes/1',
    'Basis_2/Reading barcodes/2',
    'Basis_2/Reading barcodes/3',
    'Basis_2/Reading barcodes/4',
    'Basis_2/Reading barcodes/5',
    'Basis_2/Reading barcodes/6',
    'Basis_2/Reading barcodes/7',
    'Basis_2/Reading barcodes/8',
    'Basis_2/Vacuum cleaning/1',
    'Basis_2/Vacuum cleaning/3',
    'Basis_2/Vacuum cleaning/4',
    'Basis_2/Vacuum cleaning/5',
    'Basis_2/Vacuum cleaning/6',
    'Basis_2/Vacuum cleaning/7',
    'Basis_2/Vacuum cleaning/8',
    'Basis_2/Vacuum cleaning/9',
    'Basis_2/Repairing roads/1',
    'Basis_2/Repairing roads/2',
    'Basis_2/Repairing roads/3',
    'Basis_2/Repairing roads/4',
    'Basis_2/Repairing roads/5',
    'Basis_2/Repairing roads/6',
    'Basis_2/Repairing roads/7',
]

def sli_stats(dir):
    walker = ana.SittingWalker(dir)
    dao = ana.RoboDAO(dir)
    stats = {}

    def addtime(sli_id, person, cumtime, isdone):
        sli = dao.get_by_id('StorylineItem',sli_id)
        sli_name = sli.fullname()
        if sli_name not in stats:
            entry = {}
            stats[sli_name] = entry
        else:
            entry = stats[sli_name]
        if person not in entry:
            record = {'cumtime': 0, 'count': 0, 'completed': False, 'person': person}
            entry[person] = record
        else:
            record = entry[person]
        if not record['completed']:
            record['count'] = record['count'] + 1
            record['cumtime'] = record['cumtime'] + cumtime
            if isdone:
                record['completed'] = True

    for sitting in walker:
        donetoffset=0
        sli = None
        person = sitting['person']
        for action in sitting['actions']:
            if action['type'] == 'runscript':
                sli = action['storylineitem']
                if 'success' in action['details'] and action['details']['success']:
                    isdone = True
                else:
                    isdone = False
                cumtime = action['toffset'] - donetoffset
                addtime(sli, person, cumtime, isdone)
                donetoffset = action['toffset']

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
        if sli.startswith('Basis'):
            pandastats[sli] = {'cumtime': cumtime, 'count': count, 'person': person}
    return pandastats


def calc_stats(np):

    stats = []
    for storyline in STORYLINES:
        nps = pd.DataFrame(np[storyline])
        stats.append({'storyline': storyline, 'stats': nps.describe()})
    return stats


def calc_means(np):
    cumtimes = []
    counts = []
    indices = []
    for storyline in STORYLINES:
        nps = pd.DataFrame(np[storyline])
        indices.append(storyline)
        cumtimes.append(nps.mean().get('cumtime'))
        counts.append(nps.mean().get('count'))
    s_cumtimes = pd.Series(cumtimes, index=indices)
    s_counts = pd.Series(counts, index=indices)
    result = pd.DataFrame({'cumtimes':s_cumtimes, 'counts':s_counts})
    return result


def generate_csv (np, filename):
    import csv
    import gzip
    with gzip.open(filename, 'wt') as handle:
        writer = csv.writer(handle)
        writer.writerow(["storyline", "person", "cumtime", "count"])
        for storyline in STORYLINES:
            cumtimes = np[storyline]['cumtime']
            counts = np[storyline]['count']
            persons = np[storyline]['person']
            for idx, person in enumerate(persons):
                cumtime = cumtimes[idx]
                count = counts[idx]
                writer.writerow([storyline, person, cumtime, count])


import os.path
np = sli_stats(SITTINGSDIR)
generate_csv(np, os.path.join(SITTINGSDIR, "person_results.gz"))
