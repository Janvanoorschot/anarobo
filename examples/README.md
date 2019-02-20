# Robomind Academy example analysis

This directory contains data aggregated from the
anonymized Robomind Academy data. 

The code that does the aggregation can be found in this repo
in ana.sittingswalker.py. It reads the anonymized data and 
generates one file per course in the Academy. Each of those 
CSV files consist of records containing: 


* storyline: id for a storyline item
* person: anonymized id for a person.
* cumtime: cummulated time the person spend on the storyline item
* count: number of runs the person performs on the storyline item

The Jupyter notebook Basis1.ipynb takes the CSV file of course
Basis1 and scores the performance of the persons taking that course.

