import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.interactive(True)

dataset = pd.read_csv("basis1.gz")

slis = dataset.groupby(['storyline']).describe()

dataset.loc[(dataset['storyline'] == 'Basis_1/Getting started/1') & (dataset['person'] == 'IPupil035952')]['cumtime']

# scoring the persons
# for pindex, person in dataset['person'].iteritems():
#     results = dataset[dataset['person'] == person]
#     for sindex, sli in results['storyline'].iteritems():
#         record = results[results['storyline'] == sli]
#         cumtime = record['cumtime'].iloc[0]
#         print(f"person:{person}, sli:{sli}, cumtime:{cumtime}")

# dataset['score'] = (dataset['cumtime'] < 100)

# create two python dictionaries to quickly determine scoring lines
twentyfives = {}
seventyfives = {}
for index, row in slis.iterrows():
    twentyfive = row['cumtime']['25%']
    seventyfive = row['cumtime']['75%']
    twentyfives[index] = twentyfive
    seventyfives[index] = seventyfive
# create a new score series
scores = []
for index, row in dataset.iterrows():
    cumtime = row['cumtime']
    if cumtime < twentyfives[row['storyline']]:
        score = 3
    elif cumtime > seventyfives[row['storyline']]:
        score = 1
    else:
        score = 2
    scores.append(score)
# add 'score' column to dataset
dataset['score'] = pd.Series(scores)

# calculate overal scores for each person
scoresbasis1 = dataset[['person','score']].groupby(['person']).describe()

# get the good/bad/weird_guys
bad_guys = scoresbasis1[(scoresbasis1['score']['count'] >= 43) & (scoresbasis1['score']['mean'] < 1.8)]
good_guys = scoresbasis1[(scoresbasis1['score']['count'] >= 43) & (scoresbasis1['score']['mean'] > 2.4) & (scoresbasis1['score']['mean'] != 3.0)]
weird_guys = scoresbasis1[(scoresbasis1['score']['count'] >= 43) & (scoresbasis1['score']['mean'] == 3.0)]

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

