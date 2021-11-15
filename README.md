[![Unit Tests](https://github.com/cs481-ekh/f21-pyion/actions/workflows/main.yml/badge.svg)](https://github.com/cs481-ekh/f21-pyion/actions/workflows/main.yml)
[![Project Build](https://github.com/cs481-ekh/f21-pyion/actions/workflows/build.yml/badge.svg)](https://github.com/cs481-ekh/f21-pyion/actions/workflows/build.yml)

# **Pyion**
## Summary
Pyion is a python script that takes in cellular membrane data from an Excel file (which comes is exported from an RLT
file). Once the script has this data, it performs a series of 4 steps:
1. Convert the data from an Excel format, into a custom "Pyion" Class.
2. Calculates the average and standard deviation across the voltage column from the Excel file.
3. Calculates the concentration ratio using the data generated from step 2.
4. Calculate the permeability ratio from the data generated in step 3. Then save a plot showing concentration ratios plotted against the average voltage across the cell.

Optionally, the users of the program can choose to export the data generated to the console, an Excel file, or into a csv.
## Usage
To run the script, here is the following documentation:

usage: main.py [-h] [--c C] [--x X] [--csv CSV] [--graph GRAPH] f

Pyion main.py processing of file names, and flags for output.

positional arguments:
  f              File location of the input .xlsx file,

optional arguments:
  -h, --help     show this help message and exit
  --c C          Flag for printing to the console.
  --x X          Flag for writing to an excel file.
  --csv CSV      Flag for writing to an csv file.
  --graph GRAPH  Flag for outputing graph, followed by keywords

## Environment
Python version required: 3.9

Python libraries used:

|Library|Version|
|---|---|
|certifi|2021.10.8|
|et-xmlfile|1.1.0|
|numpy|1.21.2|
|matplotlib|3.4.3|
|openpyxl|3.0.9|
|python-dateutil|2.8.2|
|pytz|2021.3|
|six|1.16.0|
|tabulate|0.8.9|
|wincertstore|0.2|

## Future Plans / Stretch Goals

* Be able to import data from RLT Files
* Convert this script into Python library
