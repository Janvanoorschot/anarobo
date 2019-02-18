import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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
dataset['score'] = (dataset['cumtime'] < 100)

for index, row in dataset.iterrows():
    pass


