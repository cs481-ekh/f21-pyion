# Pyion
## Team Members
Monte Hedrick, Donovan Wright, Zixiao Chen
## Sponsor
Daniel Fologea
## Abstract
The current software used to record measurements of transmembrane voltage provides plots, and a table of collected data, but does not provide all of the plots and data desired for measuring the selectivity of lysenin channels. Using the experimental data from a table, more data can be calculated and plotted to aid in measuring the selectivity of lysenin channels.  
From the experimental data provided in a table, we have been able to calculate average voltages, standard deviation of voltages, concentration ratios, and permeability ratios and output all of these calculated values as columns of an output table. These new calculations have also allowed us to create a plot of voltages versus concentration ratios.  
Since these calculations and plots can now be done automatically by our program, Dr.Fologea and his team will not have to spend time manually solving equations and plotting points. Our program allows more flexibility in the format of input and output since it can read and write to both excel, and csv file formats. Our program saves time and allows for customization of output tables.

## Description
### The Project
Our project (Pyion), is a command line interface program that allows our sponsor, Dr. Fologea to plug in data from his research to perform calculations and ultimately 
check to make sure that the data that his lab has produced is valid. To know that the data is valid, the end-goal calculations of this project should produce a graph similar to the one below.


![cr_graph](https://i.imgur.com/j8rN4ZM.png)


### How it Works
This program works by running in the command line space and uses the following command line arguments:
```
usage: main.py [-h] [--c C] [--x X] [--csv CSV] [--graph GRAPH] f

Pyion main.py processing of file names, and flags for output.

positional arguments:
  f              File location of the input .xlsx file,

optional arguments:
  -h, --help     show this help message and exit
  --c C          Flag for printing to the console.
  --x X          Flag for writing to an excel file.
  --csv CSV      Flag for writing to an csv file.
 ```
To run the basic program, the user just needs to supply a file name. The base program with no command line arguments will save a graph which validates or invalids the data. An example of this picture can be seen above. To run this configuration, an example is below: 
 
 
python -m src.pyion.main .\src\data\KCl-2-26-21-yellow.xlsx
![basic.png](https://i.imgur.com/svzuvT2.png)


If the user wants to also see the data displayed in the console, they can add the --c argument flag. Following the flag, they need to supply 10 one's or zero's in order to signify which columns they want to display. An example of this can be seen below:


python -m src.pyion.main .\src\data\KCl-2-26-21-yellow.xlsx --c 1111111111
![console.png](https://i.imgur.com/1o7Oi5d.png)


Using the same method as the console printing, a user can either save the output to an Excel or CSV file. An example of this can be seen below:


python -m src.pyion.main .\src\data\KCl-2-26-21-yellow.xlsx --x 1111111111
![excel.png](https://i.imgur.com/Wo0ezrI.png)
