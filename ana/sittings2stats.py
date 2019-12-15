import ana
import os

def sli_stats(dir):
    """ Calculate the Storyline-items (sli) statistics given the sitting-data calculated
    from the Robomind Academy. The sli statistics consist of storyline/person/count/cumtime
    vectors. Count is the number of time the person executed a program for the storyline
    and cumtime is the accumulated time spend on that solution.
    """
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
                # there are 'cumtimes' that are negative, due to invalid timestamps, ignore those
                if cumtime >= 0:
                    addtime(sli, person, cumtime, isdone)
                else:
                    print("eikel")
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
    filename = os.path.join(dirname, "perf_teaser.gz")
    with gzip.open(filename, 'wt') as handle:
        generate_one_csv(np, handle, STORYLINES_TEASER)
    filename = os.path.join(dirname, "perf_hourofcode.gz")
    with gzip.open(filename, 'wt') as handle:
        generate_one_csv(np, handle, STORYLINES_HOUROFCODE)
    filename = os.path.join(dirname, "perf_basis1.gz")
    with gzip.open(filename, 'wt') as handle:
        generate_one_csv(np, handle, STORYLINES_BASIS1)
    filename = os.path.join(dirname, "perf_basis2.gz")
    with gzip.open(filename, 'wt') as handle:
        generate_one_csv(np, handle, STORYLINES_BASIS2)

