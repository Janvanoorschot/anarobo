import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def loaddata():
    print("i am")


def plotdata():
    plt.interactive(True)
    plt.close('all')
    ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
    df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list('ABCD'))
    df = df.cumsum()
    plt.figure()
    df.plot()
