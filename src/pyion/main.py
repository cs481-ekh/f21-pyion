import sys
from excel_reader import *
from voltage_stdev import *
from src.pyion.averageGeneration import *
from cr import *
from excel_writer import *

# global variable
printIndicator = 0  # if -c is set, this will be set to 1
writeIndicator = 0  # if -f is set, this will be set to 1


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

    if printIndicator == 1:
        print(pyion_data.create_table())
    if writeIndicator == 1:
        write_file(pyion_data, "outputfile")
        print("  -> Wrote to execel file")


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
    if len(sys.argv) > 3:
        print(
            "Too many command line arguments given, the correct format is the following: \n [filename] [-f] [-c]")  # the arg0 is the entire directory
        exit(1)

    # for loop through the list to check if -c or -f are set, and change the indicators to 1
    for item in sys.argv:
        if item == "-c":
            printIndicator = 1

        if item == "-f":
            writeIndicator = 1


if __name__ == "__main__":
    runner()
