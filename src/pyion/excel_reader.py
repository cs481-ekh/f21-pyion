import openpyxl as op


class PyionData:
    def __init__(self):
        self.voltage = None
        self.ci = None
        self.vi = None
        self.cs = None
        self.v_add = None
        self.temp = None


# Returns all voltages from column A
def get_voltages(sheet, cell_int: int) -> list[float]:
    if sheet is None or cell_int is None:
        raise Exception("Sheet and cell_int cannot be null for get_voltages")

    cell = f"a{str(cell_int)}"
    if sheet[cell].value is None:
        values = [x[0].value for x in sheet["a2":f"a{str(cell_int-1)}"]]
        return values
    return get_voltages(sheet, cell_int+1)


# Returns all v_add from column E
def get_v_add(sheet, cell_int: int) -> list[float]:
    if sheet is None or cell_int is None:
        raise Exception("Sheet and cell_int cannot be null for get_v_add")

    cell = f"e{str(cell_int)}"
    if sheet[cell].value is None:
        values = [x[0].value for x in sheet["e2":f"e{str(cell_int-1)}"]]
        return values
    return get_v_add(sheet, cell_int+1)


def read_file(file_loc: str) -> PyionData:
    # Initializing all our variables
    data = PyionData()
    wb = op.load_workbook(file_loc, data_only=True, read_only=True)
    sheet = wb["Sheet1"]

    # Reading all the excel data
    data.voltage = get_voltages(sheet, 2)
    data.ci = sheet["b2"].value
    data.vi = sheet["c2"].value
    data.cs = sheet["d2"].value
    data.v_add = get_v_add(sheet, 2)
    data.temp = sheet["f2"].value

    return data