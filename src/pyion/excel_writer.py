import openpyxl as op

from excel_reader import PyionData

def write_file(table,outfile_name,export_format="excel"):
    if not isinstance(table,PyionData):
        Exception("Table is not a PyionData object")
    
    if export_format.lower() == "excel":
        write_excel(table,outfile_name)
    else:
        Exception("Output file type not supported")

def write_excel(table,outfile_name):
    if not isinstance(table,PyionData):
        Exception("Table is not a PyionData object")

    xl_wb = op.Workbook()
    sheet = xl_wb["Sheet"]
    headers = get_headers(table)
    sheet.append(headers)

    curr_col = 1
    row_off = 2
    for key in table.__dict__.keys():
        value = table.__dict__[key].value
        if isinstance(value,list):
            write_col(sheet,value,curr_col)
        else:
            write_col(sheet,[value],curr_col)
        curr_col += 1

    xl_wb.save(filename=outfile_name + ".xlsx")

def write_col(work_sheet,data_list,column_num,row_offset=2):
    for row,value in enumerate(data_list):
        work_sheet.cell(row=row+row_offset,column=column_num,value=value)

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
