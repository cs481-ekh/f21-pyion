import openpyxl as op

from excel_reader import PyionData

def write_file(table,outfile,export_format="excel"):
    if not isinstance(table,PyionData):
        Exception("Table is not a PyionData object")
    
    if export_format.lower() == "excel":
        write_excel(table,outfile)
    else:
        Exception("Output file type not supported")

def write_excel(table,outfile):
    if not isinstance(table,PyionData):
        Exception("Table is not a PyionData object")

    headers = get_headers(table)
    
    xl_wb = op.Workbook()
    sheet = xl_wb["Sheet"]

    for col,header in enumerate(headers):
        sheet.cell(row=1,column=col+1,value=headers[col])

    curr_col = 1
    row_off = 2
    v_list = table.voltage.value
    for r,v in enumerate(v_list):
        sheet.cell(row=r+row_off,column=curr_col,value=v)
    curr_col += 1

    sheet.cell(row=row_off,column=curr_col,value=table.ci.value)
    curr_col += 1
    sheet.cell(row=row_off,column=curr_col,value=table.vi.value)
    curr_col += 1

    sheet.cell(row=row_off,column=curr_col,value=table.cs.value)
    curr_col += 1

    v_add_list = table.v_add.value
    for r,v in enumerate(v_add_list):
        sheet.cell(row=r+row_off,column=curr_col,value=v)
    curr_col += 1

    sheet.cell(row=row_off,column=curr_col,value=table.temp.value)
    curr_col += 1

    stdev_list = table.v_stdev.value
    for r,s in enumerate(stdev_list):
        sheet.cell(row=r+row_off,column=curr_col,value=s)
    curr_col += 1

    v_avg_list = table.v_avg.value
    for r,v in enumerate(v_add_list):
        sheet.cell(row=r+row_off,column=curr_col,value=v)
    curr_col += 1

    c_ratios_list = table.c_ratios.value
    for r,c in enumerate(c_ratios_list):
        sheet.cell(row=r+row_off,column=curr_col,value=c)
    curr_col += 1

    xl_wb.save(filename=outfile + ".xlsx")

def get_headers(table):
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
    return headers
