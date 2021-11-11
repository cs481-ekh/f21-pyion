from excel_reader import read_file as read_excel
import csv
import sys

from pyion.objects.PyionData import PyionData

def read_file(file_loc):
    data = None

    file_type = ""
    if ".xlsx" in file_loc:
        file_type = "excel"
    elif ".csv" in file_loc:
        file_type = ".csv"
    else:
        print("input file extension not recognized",sys.stderr)
        return data

    if file_type == "excel":
        data = read_excel(file_loc)
    elif file_type == "csv":
        data = read_csv(file_loc)
    
    return data
    
def read_csv(file_loc):
    data = None

    try:
        in_file = open(file_loc,"r")
        data = PyionData()
        reader = csv.reader(in_file,delimiter=",")

        ROW_LEN = 6
        headers = csv.reader.__next__()
        if len(headers) != ROW_LEN:
            Exception("input file should have 6 columns in header")
        else:
            if "vm" not in headers[0].lower():
                raise Exception("Vm should be column 1")

            if "ci" not in headers[1].lower():
                raise Exception("Ci should be column 2")

            if "vi" not in headers[2].lower():
                raise Exception("Vi should be column 3")

            if "cs" not in headers[3].lower():
                raise Exception("Cs should be column 4")

            if "vadd" not in headers[4].lower():
                raise Exception("Vadd should be column 5")

            if "temp" not in headers[5].lower():
                raise Exception("temp should be column 6")

        for row_num,row in enumerate(csv.reader):
            if len(row) != ROW_LEN:
                Exception("input file should have 6 columns per row")
            if row_num == 0:
                data.ci.value.append(row[1])
                data.vi.value.append(row[2])
                data.cs.value.append(row[3])
                data.temp.value.append(row[5])

            data.voltage.value.append(row[0])
            data.v_add.value.append(row[4])

    except IOError:
        print("input file could not be opened",sys.stderr)
        return data
