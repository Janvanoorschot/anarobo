import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
########################################################################
# experimenting with plotting in a 'experiments.py' base

plt.interactive(True)

# start with the plotting
x = np.linspace(0, 2, 100)
plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()
plt.show()

# get an array from existing data
