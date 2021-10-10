import openpyxl as op
from os.path import exists


class PyionData:
    def __init__(self):
        self.voltage = None
        self.ci = None
        self.vi = None
        self.cs = None
        self.v_add = None
        self.temp = None


def check_headers(sheet) -> None:
    if sheet is None:
        raise Exception("Sheet cannot be null")

    headers = list(sheet.rows)[0]
    if len(headers) != 6:
        raise Exception("Number of columns is off, should only have 6 columns.")

    if "vm" not in headers[0].value.lower():
        raise Exception("Vm should be column 1")

    if "ci" not in headers[1].value.lower():
        raise Exception("Ci should be column 2")

    if "vi" not in headers[2].value.lower():
        raise Exception("Vi should be column 3")

    if "cs" not in headers[3].value.lower():
        raise Exception("Cs should be column 4")

    if "vadd" not in headers[4].value.lower():
        raise Exception("Vadd should be column 5")

    if "temp" not in headers[5].value.lower():
        raise Exception("temp should be column 6")


# Returns all of a column recursively after row 1
def get_column(sheet, col:  str, cell_int: int) -> list[float]:
    if sheet is None or cell_int is None or col is None:
        raise Exception("Null paramter given in get_column method")

    cell = f"{col}{str(cell_int)}"
    if sheet[cell].value is None:
        values = [x[0].value for x in sheet[f"{col}2":f"{col}{str(cell_int-1)}"]]
        return values
    return get_column(sheet, col, cell_int+1)


def read_file(file_loc: str) -> PyionData:
    # Making sure the file exists
    if not exists(file_loc):
        raise Exception(f"File {file_loc} doesn't exist or cant be found.")

    # Initializing all our variables
    try:
        data = PyionData()
        wb = op.load_workbook(file_loc, data_only=True, read_only=True)
        sheet = wb["Sheet1"]
    except Exception:
        raise Exception("Error trying to load excel file, make sure the file is a .xlsx file "
                        "and the main sheet is titled 'Sheet1'.")

    check_headers(sheet)
    # Reading all the excel data
    data.voltage = get_column(sheet, 'a', 2)
    if len(data.voltage) % 3 != 0:
        raise Exception("Voltage column should be in multiples of 3, current column is not.")
    for value in data.voltage:
        if type(value) is not float:
            raise Exception("Non-float value found in voltage column")

    data.ci = sheet["b2"].value
    if type(data.ci) != int and type(data.ci) != float:
        raise Exception("Ci value must be an int or float")

    data.vi = sheet["c2"].value
    if type(data.vi) != int and type(data.vi) != float:
        raise Exception("Vi value must be an int or float")

    data.cs = sheet["d2"].value
    if type(data.cs) != int and type(data.cs) != float:
        raise Exception("Cs value must be an int or float")

    data.v_add = get_column(sheet, 'e', 2)
    if len(data.voltage)/3 != len(data.v_add):
        raise Exception("V_add column length should equal voltage column divided by 3, currently does not.")
    for value in data.v_add:
        if type(value) is not float and type(value) is not int:
            raise Exception("Non-float / Non-int value found in voltage column")

    data.temp = sheet["f2"].value
    if type(data.temp) != int and type(data.temp) != float:
        raise Exception("Temp value must be an int or float")

    return data