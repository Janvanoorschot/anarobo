#!/usr/bin/env python3
#

from ana.sittings2stats import sli_stats, generate_csv
SITTINGSDIR = '/data/robodata/ano'
CVSDIR='/data/robodata/aggr'

if __name__ == "__main__":
    # execute only if run as a script
    import os.path
    np = sli_stats(SITTINGSDIR)
    generate_csv(np, CVSDIR)
