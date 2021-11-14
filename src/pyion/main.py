import sys
import argparse
from src.pyion.excel_reader import *
from src.pyion.voltage_stdev import *
from src.pyion.averageGeneration import *
from src.pyion.cr import *
from src.pyion.pyion_filewriter import *
from src.pyion.pr import *


def runner():
    args = validate_cmd_line()
    step_one(args)
    step_two(args)
    step_three(args)
    step_four(args)
    pass


def step_one(args: dict):
    print("-> Running Step 1")
    print("    -> Reading Excel File")
    pyion_data = read_file(args['file_loc'])
    print("    -> Calculating Voltage Average")
    pyion_data.add_entry("v_stdev", "Voltage SD", "mV", voltage_stdev(pyion_data.voltage.value))
    print("    -> Calculating Voltage Standard Deviation")
    pyion_data.add_entry("v_avg", "Voltage Average", "mV", calculateAverage(pyion_data.voltage.value))
    print("    -> Calculating Concentration Ratios")
    pyion_data.add_entry("c_ratios", "Concentration Ratios", "None",
                         get_ratios(pyion_data.ci.value, pyion_data.vi.value,
                                    pyion_data.cs.value, pyion_data.v_add.value))
    print("    -> Calculating Permeability Ratios")
    pyion_data.add_entry("p_ratios", "Permeability Ratios", "None",
                         get_pr_list(pyion_data.v_add.value, pyion_data.temp.value,
                                    pyion_data.c_ratios.value))
    if args['c']:
        if len(args['c']) != pyion_data.entryCount:
            raise Exception(f"--c argument doesn't match the number of Pyion Unit entries, looking "
                            f"for {pyion_data.entryCount} number of flags in the --c argument. (eg. {pyion_data.entryCount * '1'})")
        print(pyion_data.create_table(args['c']))
    if args['x']:
        if len(args['x']) != pyion_data.entryCount:
            raise Exception(f"--x argument doesn't match the number of Pyion Unit entries, looking "
                            f"for {pyion_data.entryCount} number of flags in the --x argument. (eg. {pyion_data.entryCount * '1'})")
        write_file(pyion_data, "outputfile", args['x'], export_format="excel")
        print("  -> Wrote to execel file")
    if args['csv']:
        if len(args['csv']) != pyion_data.entryCount:
            raise Exception(f"--csv argument doesn't match the number of Pyion Unit entries, looking "
                            f"for {pyion_data.entryCount} number of flags in the --csv argument. (eg. {pyion_data.entryCount * '1'})")
        write_file(pyion_data, "outputfile", args['csv'], export_format="csv")
        print("  -> Wrote to csv file")


def step_two(args: dict):
    print("-> Running Step 2")
    pass


def step_three(args: dict):
    print("-> Running Step 3")
    pass


def step_four(args: dict):
    print("-> Running Step 4")
    pass


def validate_input():
    pass


def validate_cmd_line() -> dict:
    parser = argparse.ArgumentParser(description="Pyion main.py processing of file names, and flags for output.")
    parser.add_argument("file_loc", metavar='f', type=str, help="File location of the input .xlsx file,")  # File location Argument
    parser.add_argument("--c", required=False, type=str, help="Flag for printing to the console.")  # Print to console flag
    parser.add_argument("--x", required=False, type=str, help="Flag for writing to an excel file.")  # Write to Excel flag
    parser.add_argument("--csv", required=False, type=str, help="Flag for writing to an csv file.")  # Write to CSV flag
    parser.add_argument("--graph", type=str, help="Flag for outputing graph, followed by keywords")
    return vars(parser.parse_args())


if __name__ == "__main__":
    runner()
