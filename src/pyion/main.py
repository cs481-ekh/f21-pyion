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
    pyion_data = read_file(sys.argv[1])
    print("    -> Calculating Voltage Average")
    pyion_data.add_entry("v_stdev", "Voltage SD", "mV", voltage_stdev(pyion_data.voltage.value))
    print("    -> Calculating Voltage Standard Deviation")
    pyion_data.add_entry("v_avg", "Voltage Average", "mV", calculateAverage(pyion_data.voltage.value))
    print("    -> Calculating Concentration Ratios")
    pyion_data.add_entry("c_ratios", "Concentration Ratios", "None",
                         get_ratios(pyion_data.ci.value, pyion_data.vi.value,
                                    pyion_data.cs.value, pyion_data.v_add.value))

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
        PyionData.print_table();

    if sys.argv[2] == "-f":
        print("-f is entered, the output will be written to a file, and the filename should be provided")

    if sys.argv[1] == "-c" and sys.argv[2] == "-f":
        print("Both -c and -f are entered, set the flag indicator to 1\n")
        flagIndicator = 1



if __name__ == "__main__":
    runner()