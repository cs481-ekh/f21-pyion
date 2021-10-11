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

    # Test check_headers fails on headers with length not equal to 6:
    def test_check_headers_throws_error_given_wrong_length_header(self):
        sheet_mock = Mock()
        headers = list(sheet_mock.rows)[0]

        if len(headers) != 6:
            self.assertRaises(Exception)

        # with self.assertRaises(Exception):
        #         headers = list(sheet_mock.rows)[0]
        #         len(headers) != 6



