import openpyxl as op

from excel_reader import PyionData

def write_file(table,export_format):
    if not isinstance(table,PyionData):
        Exception("Table is not a PyionData object")
    headers = []
    headers.append(table.voltage.name + "(" + table.voltage.unit + ")")
    headers.append(table.ci.name + "(" + table.ci.unit + ")")
    headers.append(table.vi.name + "(" + table.vi.unit + ")")
    headers.append(table.cs.name + "(" + table.cs.unit + ")")
    headers.append(table.v_add.name + "(" + table.v_add.unit + ")")
    headers.append(table.temp.name + "(" + table.temp.unit + ")")
    headers.append(table.v_stdev.name + "(" + table.v_stdev.unit + ")")
    headers.append(table.v_avg.name + "(" + table.v_avg.unit + ")")
    headers.append(table.c_ratios.name + "(" + table.c_ratios.unit + ")")
    if export_format.lower() == "excel":
        write_excel(table,headers)
    else:
        Exception("Output file type not supported")

def write_excel(table,headers):
    if not isinstance(table,PyionData):
        Exception("Table is not a PyionData object")
    xl_wb = op.Workbook()
    sheet = xl_wb["Sheet"]

    for col,header in enumerate(headers):
        sheet.cell(row=1,column=col) = header

    curr_col = 1
    v_list = table.voltage.value
    for r,cell in enumerate(sheet[curr_col][1:]):
        sheet.cell(row=r+1,column=curr_col) = v_list[r]
    curr_col += 1

    sheet.cell(row=2,column=curr_col) = table.ci.value
    curr_col += 1

    sheet.cell(row=2,column=curr_col) = table.vi.value
    curr_col += 1

    sheet.cell(row=2,column=curr_col) = table.cs.value
    curr_col += 1

    v_add_list = table.v_add.value
    for r,cell in enumerate(sheet[curr_col][1:]):
        sheet.cell(row=r+1,column=curr_col) = v_add_list[r]
    curr_col += 1

    sheet.cell(row=2,column=curr_col) = table.temp.value
    curr_col += 1

    stdev_list = table.v_stdev.value
    for r,cell in enumerate(sheet[curr_col][1:]):
        sheet.cell(row=r+1,column=curr_col) = stdev_list[r]
    curr_col += 1

    v_avg_list = table.v_avg.value
    for r,cell in enumerate(sheet[curr_col][1:]):
        sheet.cell(row=r+1,column=curr_col) = v_avg_list[r]
    curr_col += 1

    c_ratios_list = table.c_ratios.value
    for r,cell in enumerate(sheet[curr_col][1:]):
        sheet.cell(row=r+1,column=curr_col) = c_ratios_list[r]
    curr_col += 1


