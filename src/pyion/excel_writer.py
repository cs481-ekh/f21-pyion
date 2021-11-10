import openpyxl as op

from excel_reader import PyionData

def write_file(table,outfile_name,export_format="excel"):
    if not isinstance(table,PyionData):
        Exception("Table is not a PyionData object")
    
    if export_format.lower() == "excel" or export_format.lower() == "xlsx":
        if ".xlsx" in outfile_name:
            write_excel(table,outfile_name)
        else:
            write_excel(table,outfile_name=outfile_name+".xlsx")
    else if export_format.lower() == "csv":
        if ".csv" in outfile_name:
            write_csv(table,outfile_name)
        else:
            write_csv(table,outfile_name=outfile_name+".csv")
    else:
        Exception("Output file type not supported")

def write_csv(table,outfile_name):
    f = open(outfile_name,"w")
    headers = get_headers(table)
    write_csv_row(f,headers)
    curr_row = []
    row_num = 0
    col_num = 0
    #do this loop until all table written
    for key in table.__dict__.keys():
        value = table.__dict__[key].value
        if isinstance(value,list):
            if(row_num < len(value)):
                curr_row.append(value[row_num])
            else:
                curr_row.append("")
        else:
            if(row_num == 0):
                curr_row.append(value)
            else:
                curr_row.append("")
    write_csv_row(curr_row)
    row_num += 1


def write_csv_row(file,data):
    for element in data[:len(data)-1]:
        f.write(element)
        f.write(",")
    f.write(data[len(data)-1])

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
            write_excel_col(sheet,value,curr_col)
        else:
            write_excel_col(sheet,[value],curr_col)
        curr_col += 1

    xl_wb.save(filename=outfile_name)

def write_excel_col(work_sheet,data_list,column_num,row_offset=2):
    for row,value in enumerate(data_list):
        work_sheet.cell(row=row+row_offset,column=column_num,value=value)

def get_headers(table):
    if not isinstance(table,PyionData):
        Exception("Table is not a PyionData object")
    headers = []
    for key in table.__dict__.keys():
        name = table.__dict__[key].name
        unit = table.__dict__[key].unit
        headers.append(name + "(" + unit + ")")
    return headers
