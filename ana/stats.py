import ana


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
            record = {'cumtime': 0, 'count': 0, 'completed': False}
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
        completed = []
        for pupil in stats[sli]:
            sts = stats[sli][pupil]
            if sts['completed']:
                cumtime.append(sts['cumtime'])
                count.append(sts['count'])
        if sli.startswith('Basis'):
            pandastats[sli] = {'cumtime': cumtime, 'count': count}
    return pandastats
