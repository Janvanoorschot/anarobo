import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def generategifs(csv_dir, gif_dir):
    # get the csv data into a dataframe
    csv = pd.read_csv(os.path.join(csv_dir, "stats_weekofyear.csv.gz"))

    # create multiindex year/week so we can use it to calculate datatime index
    mi = csv.set_index(['year','weekofyear'])

    # create new index
    from datetime import datetime
    newindex = []
    for item in mi.index:
        str = f"{item[0]} {item[1]} 0"
        t = datetime.strptime(str, "%Y %W %w")
        newindex.append(t)

    # assign new index to our csv dataframe
    dt = csv.reset_index()
    dt.index = newindex

    # drop the year/week columns
    del dt['year']
    del dt['weekofyear']
    del dt['index']

    axes = dt.plot()
    axes.set_xlim(pd.Timestamp('2019-01-01'), pd.Timestamp('2022-05-07'))

    plt.savefig(os.path.join(gif_dir, "stats_weekofyear.jpg"))
