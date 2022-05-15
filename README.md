# Robomind Academy Anonymization Data

This repository contains the anonymization data collected from the Robomind Academy. This data
was collected from (young) persons learning about Computational Thinking in the Robomind Academy 
website. 

Together with the data this repository contains some example Junyper notebooks and python code 
to analyse that data.

## Anonymized Data

The ./data directory contains the anonymized data collected over the last couple of years.
Here you can read more about the [Anonymized data](data/README.md)

## Data Format

The anonymized data is in a compressed JSON format.
Here you can read more about this [data format](docs/README.md)

## Example Analysis

The anonymized data from the Robomind Academy can be used for research and for improving
the way Computational Thinking is taught in the Academy. 

As an example this repo contains a Jupyter notebook which sketches a method for scoring 
the performance of pupils in a course. The raw compressed JSON data is not easy to handle 
in a Jupyter Notebook while CSV files are. This example therefor also contains some Python
code that extracts run-times (count) and accumulated time (cumtime) and stores it in CSV files.
Here you find more documentation about the [Example Analysis](notebooks/README.md).
