#!/usr/bin/env python3
#

from ana.sittings2usage import sli_usage, generate_csv
SITTINGSDIR = '/data/robodata/ano'
CVSDIR='/data/robodata/aggr'

if __name__ == "__main__":
    np = sli_usage(SITTINGSDIR)
    generate_csv(np, CVSDIR)
