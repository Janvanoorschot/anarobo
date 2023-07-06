import ana
import os
from pathlib import Path

def courses_percentiles(dir):
    """ Calculate the precentiles for time/attempts for each storyline_item in each course.
    """
    cp = {}
    pathlist = Path(dir   ).glob("perf_*.gz")
    for path in pathlist:
        coursename = path.stem[5:]
        cp[coursename] = {}
    return cp


def generate_one_csv(cp, handle, arr):
    """generate the CSV content. """
    import csv
    writer = csv.writer(handle)
    writer.writerow(["storyline", "person", "cumtime", "count"])


def generate_csvs(cp, dirname):
    """create compressed csv files"""
    import gzip
    filename = os.path.join(dirname, "perf_teaser.csv.gz")
    with gzip.open(filename, 'wt') as handle:
        generate_one_csv(cp, handle, "teaser")

