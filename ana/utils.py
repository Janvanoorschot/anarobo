import datetime

DATEFORMAT = '%Y-%m-%dT%H:%M:%SZ'


def date2string(d):
    if d:
        return d.strftime(DATEFORMAT)
    else:
        return datetime.datetime.now().strftime(DATEFORMAT)


def string2date(s):
    try:
        d = datetime.datetime.strptime(s, DATEFORMAT)
    except ValueError:
        print("invalid date-string: " + s)
        d = datetime.datetime.now()
    return d
