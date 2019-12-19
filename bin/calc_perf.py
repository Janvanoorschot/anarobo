#!/usr/bin/env python3
#

from ana.sittings2perf import sli_perf, generate_csv
SITTINGSDIR = '/data/robodata/ano'
CVSDIR='/data/robodata/aggr'

if __name__ == "__main__":
    np = sli_perf(SITTINGSDIR)
    generate_csv(np, CVSDIR)
