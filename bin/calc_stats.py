#!/usr/bin/env python3
import sys
import os
import argparse
from ana.sittings2stats import sli_stats, generate_csv

# discover paths
scriptpath = os.path.dirname(__file__)
modpath = os.path.abspath(os.path.join(scriptpath, os.pardir))
os.chdir(modpath)
sys.path.append(modpath)

SITTINGSDIR = os.path.join(modpath, 'data/ano')
CVSDIR=os.path.join(modpath, 'data/cvs')

# get commandline parameters and mix everything
parser = argparse.ArgumentParser(description='Logging all Babacom messages and events.')
parser.add_argument("--sdir", type=str, default=os.environ.get("SCRIBEVIEW_CONFIG", SITTINGSDIR), help="sitting directory")
parser.add_argument("--cdir", type=str, default=os.environ.get("SCRIBEVIEW_CONFIG", CVSDIR), help="cvs directory")
parser.add_argument("--debug", type=bool,  default=False, help="output debugging information")
args = parser.parse_args()

debug = False
if args.debug:
    debug = True

if __name__ == "__main__":
    np = sli_stats(args.sdir)
    generate_csv(np, args.cdir)
