import unittest
from unittest.mock import Mock
import src.pyion.excel_reader as er


class ExcelReaderTestCase(unittest.TestCase):
    #get_voltages fails on null
    def test_voltages_throws_error_given_null_sheet(self):
        with self.assertRaises(Exception):
            er.get_voltages(None, 1)

    #get_voltages fails on null
    def test_voltages_throws_error_given_null_row(self):
        sheet_mock = Mock()
        with self.assertRaises(Exception):
            er.get_voltages(sheet_mock, 1)

    # get_v_add fails on null
    def test_v_add_throws_error_given_null_sheet(self):
        with self.assertRaises(Exception):
             er.get_v_add(None, 1)

    # get_v_add fails on null
    def test_v_add_throws_error_given_null_row(self):
        sheet_mock = Mock()
        with self.assertRaises(Exception):
            er.get_v_add(sheet_mock, 1)

    def test_read_file_throws_error_given_null_file(self):
        with self.assertRaises(Exception):
            er.get_voltages(er.read_file("abc"), 1)