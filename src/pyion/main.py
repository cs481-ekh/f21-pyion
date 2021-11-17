"""This module assists in calculations and graphs for Dr.Fologea"""
import argparse
from src.pyion.pyion_filereader import read_file
from src.pyion.voltage_stdev import voltage_stdev
from src.pyion.averageGeneration import calculateAverage
from src.pyion.cr import get_ratios
from src.pyion.pyion_filewriter import write_file
from src.pyion.pr import get_pr_list
from src.pyion.graph_maker import graph_cr_vs_v


def runner():
    """Reads an input file and performs tasks according to arguments"""
    #pylint: disable=line-too-long
    #pylint: disable=undefined-variable
    #pylint: disable=no-member
    args = validate_cmd_line()
    print("-> Running Step 1")
    print("    -> Reading Excel File")
    pyion_data = read_file(args['file_loc'])
    print("-> Running Step 2")
    print("    -> Calculating Voltage Average")
    pyion_data.add_entry("v_stdev", "Voltage SD", "mV", voltage_stdev(pyion_data.voltage.value))
    print("    -> Calculating Voltage Standard Deviation")
    pyion_data.add_entry("v_avg", "Voltage Average", "mV", calculateAverage(pyion_data.voltage.value))
    print("-> Running Step 3")
    print("    -> Calculating Concentration Ratios")
    pyion_data.add_entry("c_ratios", "Concentration Ratios", "None",
                         get_ratios(pyion_data.ci.value, pyion_data.vi.value,
                                    pyion_data.cs.value, pyion_data.v_add.value))
    print("-> Running Step 4")
    print("    -> Calculating Permeability Ratios")
    pyion_data.add_entry("p_ratios", "Permeability Ratios", "None",
                         get_pr_list(pyion_data.v_add.value, pyion_data.temp.value,
                                     pyion_data.c_ratios.value))
    print("-> Saving Concentration Ratio vs Average Voltage to ./cr_vs_voltage.png")
    graph_cr_vs_v(pyion_data.c_ratios, pyion_data.v_avg)


    print("-> Executing command line argument requests.")
    if args['c']:
        if len(args['c']) != pyion_data.entryCount:
            raise Exception(f"--c argument doesn't match the number of Pyion Unit entries, looking "
                            f"for {pyion_data.entryCount} number of flags in the --c argument. (eg. {pyion_data.entryCount * '1'})")
        print(f"Console Table: \n{pyion_data.create_table(args['c'])}")
    if args['x']:
        if len(args['x']) != pyion_data.entryCount:
            raise Exception(f"--x argument doesn't match the number of Pyion Unit entries, looking "
                            f"for {pyion_data.entryCount} number of flags in the --x argument. (eg. {pyion_data.entryCount * '1'})")
        write_file(pyion_data, "outputfile", args['x'], export_format="excel")
        print("  -> Wrote to Excel file.")
    if args['csv']:
        if len(args['csv']) != pyion_data.entryCount:
            raise Exception(f"--csv argument doesn't match the number of Pyion Unit entries, looking "
                            f"for {pyion_data.entryCount} number of flags in the --csv argument. (eg. {pyion_data.entryCount * '1'})")
        write_file(pyion_data, "outputfile", args['csv'], export_format="csv")
        print("  -> Wrote to csv file.")


def validate_cmd_line() -> dict:
    """Validates command line arguments"""
    #pylint: disable=line-too-long
    parser = argparse.ArgumentParser(description="Pyion main.py processing of file names, and flags for output.")
    parser.add_argument("file_loc", metavar='f', type=str, help="File location of the input .xlsx file,")  # File location Argument
    parser.add_argument("--c", required=False, type=str, help="Flag for printing to the console.")  # Print to console flag
    parser.add_argument("--x", required=False, type=str, help="Flag for writing to an excel file.")  # Write to Excel flag
    parser.add_argument("--csv", required=False, type=str, help="Flag for writing to an csv file.")  # Write to CSV flag
    parser.add_argument("--graph", type=str, help="Flag for outputing graph, followed by keywords")
    return vars(parser.parse_args())


if __name__ == "__main__":
    runner()
