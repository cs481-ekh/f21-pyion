import sys
from excel_reader import *
from voltage_stdev import *
from src.pyion.averageGeneration import *
from cr import *

def runner():
    validate_cmd_line()
    step_one()
    step_two()
    step_three()
    step_four()
    pass


def step_one():
    print("-> Running Step 1")
    print("    -> Reading Excel File")
    excel_data = read_file(sys.argv[1])
    print("    -> Calculating Voltage Average")
    excel_data.v_stdev.value = voltage_stdev(excel_data.voltage.value)
    print("    -> Calculating Voltage Standard Deviation")
    excel_data.v_avg.value = calculateAverage(excel_data.voltage.value)
    print("    -> Calculating Concentration Ratios")
    c_ratios = get_ratios(excel_data.ci.value, excel_data.vi.value, excel_data.cs.value, excel_data.v_add.value)

def step_two():
    print("-> Running Step 2")
    pass


def step_three():
    print("-> Running Step 3")
    pass


def step_four():
    print("-> Running Step 4")
    pass


def validate_input():
    pass


def validate_cmd_line() -> None:

    flagIndicator = 0; #if both -c and -f are set, this will be set to 1

    if len(sys.argv) > 4:
        print("Too many command line arguments given, the correct format is the following: \n main.py [-f] [-c] [filename]")
        exit(1)

    if sys.argv[0] != "main.py":
        print("The python file name should be main.py\n")
        exit(1)

    if sys.argv[1] == "-c":
        print("-c is entered, the table will be printed to the console\n")

    if sys.argv[2] == "-f":
        print("-f is entered, the output will be written to a file, and the filename should be provided")

    if sys.argv[1] == "-c" and sys.argv[2] == "-f":
        print("Both -c and -f are entered, set the flag indicator to 1\n")
        flagIndicator = 1



if __name__ == "__main__":
    runner()