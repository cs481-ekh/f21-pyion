import sys
from excel_reader import *
from voltage_stdev import *
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
    v_stdev = voltage_stdev(excel_data.voltage)
    c_ratios = get_ratios(excel_data.ci,excel_data.ci,excel_data.vi,excel_data.cs,excel_data.v_add)

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
    if len(sys.argv) > 2:
        print("Too many command line arguments given \n main.py [excel file location]")
        exit(1)


if __name__ == "__main__":
    runner()