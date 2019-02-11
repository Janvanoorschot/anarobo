import ana
import json

SITTINGSDIR = '/data/robodata/ano'
walker = ana.SittingWalker(SITTINGSDIR)

stats = {}


def addtime(sli, person, cumtime, isdone):
    if sli not in stats:
        entry = {}
        stats[sli] = entry
    else:
        entry = stats[sli]
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
            cumtime = action['toffset'] - donetoffset
            donetoffset = action['toffset']
            if 'success' in action['details'] and action['details']['success']:
                isdone = True
            else:
                isdone = False
            addtime(sli, person, cumtime, isdone)
            # cnt = cnt + 1
            # str = json.dumps(sitting, indent=2)

print("done")
