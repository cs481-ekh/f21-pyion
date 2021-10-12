import unittest
from unittest.mock import Mock
import src.pyion.excel_reader as er


class ExcelReaderTestCase(unittest.TestCase):
    # get_columns fails on null sheet
    def test_get_column_throws_error_given_null_sheet(self):
        with self.assertRaises(Exception):
            er.get_column(None, 'a', 1)

    # get_columns fails on null col letter
    def test_get_column_throws_error_given_null_col(self):
        sheet_mock = Mock()
        with self.assertRaises(Exception):
            er.get_column(sheet_mock, None, 1)

    # get_columns fails on null index
    def test_get_column_throws_error_given_null_index(self):
        sheet_mock = Mock()
        with self.assertRaises(Exception):
            er.get_column(sheet_mock, 'a', None)

    # Test file checking exception
    def test_read_file_throws_error_given_null_file(self):
        with self.assertRaises(Exception):
            er.read_file("abc")


    # Test check_headers on if sheet is none:
    def test_check_headers_throws_error_given_null_sheet(self):
        with self.assertRaises(Exception):
             er.check_headers(None)




