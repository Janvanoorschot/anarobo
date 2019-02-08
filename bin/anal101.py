import argparse
import eh
import ph

# define the commandline arguments
parser = argparse.ArgumentParser()
parser.add_argument("--events", default="/data/robodata/events")
parser.add_argument("--periods", default="/data/robodata/periods")
parser.add_argument("--anoindex", default="/data/robodata/anoindex")
parser.add_argument("--ano", default="/data/robodata/ano")

args = parser.parse_args()

ready = False

while not ready:

    # create the core handlers
    phandler = eh.PeriodHandler(args.events, args.periods)
    ahandler = ph.AnoHandler(args.ano, args.anoindex, phandler)
    phcreator = ph.ObjectCreator()
    phcache = ph.ObjectCache(phcreator)

    nextperiods = ahandler.next_periods()
    if len(nextperiods) <= 0:
        ready = True
    else:
        ahandler.preload(phcache)
        for period in nextperiods:
            print(f"handling period: {period}")
            ehcache = eh.ObjectCache()
            ahandler.open_period(period, ehcache)
            ahandler.handle_period(ehcache, phcache)
            ahandler.close_period()
        ahandler.close(phcache)

