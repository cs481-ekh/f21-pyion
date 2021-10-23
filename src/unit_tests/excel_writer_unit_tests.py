import unittest
import src.pyion.excel_reader as rd
import src.pyion.excel_writer as wr

class ExcelWriterTestCase(unittest.TestCase):
    def __init__(self):
        super(ExcelWriterTestCase,self).__init__()
        self.test_xl_file = "src/data/KCl-2-26-21-yellow"


    def test_write_file_invalid_table(self):
        with self.assertRaises(Exception):
            wr.write_file(table=0.5,outfile_name="test.xlsx")

    def test_write_file_invalid_export_format(self):
        with self.assertRaises(Exception):
            data_table = rd.read_file(self.test_xl_file + ".xlsx")
            wr.write_file(data_table,self.test_xl_file,export_format="pdf")