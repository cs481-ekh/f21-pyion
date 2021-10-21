import openpyxl as op

from excel_reader import PyionData

def write_file(table,export_format):
    headers = []
    headers.append(table.voltage.name + "(" + table.voltage.unit + ")")
    headers.append(table.ci.name + "(" + table.ci.unit + ")")
    headers.append(table.vi.name + "(" + table.vi.unit + ")")
    headers.append(table.cs.name + "(" + table.cs.unit + ")")
    headers.append(table.v_add.name + "(" + table.v_add.unit + ")")
    headers.append(table.temp.name + "(" + table.temp.unit + ")")
    headers.append(table.v_stdev.name + "(" + table.v_stdev.unit + ")")
    headers.append(table.v_avg.name + "(" + table.v_avg.unit + ")")

    if not isinstance(table,PyionData):
        Exception("Table is not a PyionData object")
    if export_format.lower() == "excel":
        write_excel(table,headers)
    else:
        Exception("Output file type not supported")

def write_excel(table,headers):
    xl_wb = op.Workbook()
    sheet = xl_wb["Sheet"]
    for col,header in enumerate(headers):
        sheet.cell(row=1,column=col) = header


