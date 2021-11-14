import sys
import openpyxl as op
from src.pyion.objects.PyionData import PyionData
from src.pyion.objects.PyionUnit import PyionUnit

#Writes the provided PyionData table to a file specified by outfile_name
#export_format controls the type of file created
def write_file(table, outfile_name, flags, export_format="excel"):
    if not isinstance(table,PyionData):
        Exception("Table is not a PyionData object")
    
    if export_format.lower() == "excel" or export_format.lower() == "xlsx":
        if ".xlsx" in outfile_name:
            write_excel(table,outfile_name, flags)
        else:
            write_excel(table, outfile_name+".xlsx", flags)
    elif export_format.lower() == "csv":
        if ".csv" in outfile_name:
            write_csv(table,outfile_name, flags)
        else:
            write_csv(table,outfile_name+".csv", flags)
    else:
        Exception("Output file type not supported")

#writes the table to a csv file
def write_csv(table,outfile_name, flags):
    if not isinstance(table,PyionData):
        Exception("Table is not a PyionData object")

    try:
        f = open(outfile_name,"w")
        headers = get_headers(table, flags)
        write_csv_row(f,headers)

        max_len = 0
        for key in table.__dict__.keys():
            if isinstance(table.__dict__[key], PyionUnit):
                value = table.__dict__[key].value
                if isinstance(value,list):
                    if(len(value) > max_len):
                        max_len = len(value)
                elif (1 > max_len):
                    max_len = 1

        col_num = 0
        for row in range(0,max_len):
            curr_row = []
            for key in table.__dict__.keys():
                if isinstance(table.__dict__[key], PyionUnit):
                    value = table.__dict__[key].value
                    if isinstance(value,list):
                        if(row < len(value)):
                            curr_row.append(value[row])
                        else:
                            curr_row.append("")
                    else:
                        if(row == 0):
                            curr_row.append(value)
                        else:
                            curr_row.append("")
            csv_flag_checker(curr_row, flags)
            write_csv_row(f,curr_row)
    except IOError:
        print("could not open outputfile",file=sys.stderr)

def csv_flag_checker(row, flags):
    for x in range(0, len(row)):
        if flags[x] == "0":
            del row[x]

#writes a single row of csv data to a file
def write_csv_row(file,data):
    if file.closed:
        Exception("output file is closed")
    if len(data) > 1:
        for element in data[:len(data)-1]:
            file.write(str(element))
            file.write(",")
        file.write(str(data[len(data)-1]))
    elif len(data) == 1:
        file.write(str(data[0]))      
    file.write("\n")

#writes the table to an excel file
def write_excel(table, outfile_name, flags: str):
    if not isinstance(table,PyionData):
        Exception("Table is not a PyionData object")

    xl_wb = op.Workbook()
    sheet = xl_wb["Sheet"]
    headers = get_headers(table, flags)
    sheet.append(headers)

    curr_col = 1
    var_count = 0
    row_off = 2
    for key in table.__dict__.keys():
        if isinstance(table.__dict__[key], PyionUnit):
            value = table.__dict__[key].value
            if flags[var_count] == "1":
                if isinstance(value,list):
                    write_excel_col(sheet,value,curr_col)
                else:
                    write_excel_col(sheet,[value],curr_col)
                curr_col += 1
            var_count += 1

    xl_wb.save(filename=outfile_name)

#writes a single column of data to the excel file
def write_excel_col(work_sheet,data_list,column_num,row_offset=2):
    for row,value in enumerate(data_list):
        work_sheet.cell(row=row+row_offset,column=column_num,value=value)

#returns a list of the tables headers
def get_headers(table, flags: str):
    if not isinstance(table,PyionData):
        Exception("Table is not a PyionData object")
    headers = []
    count = 0
    for key in table.__dict__.keys():
        if isinstance(table.__dict__[key], PyionUnit):
            if flags[count] == "1":
                name = table.__dict__[key].name
                unit = table.__dict__[key].unit
                headers.append(name + "(" + unit + ")")
            count += 1
    return headers
