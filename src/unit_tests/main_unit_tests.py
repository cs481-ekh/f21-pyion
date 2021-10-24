import sys
import unittest
import src.pyion.main as main
import src.pyion.objects as objects
from src.pyion.averageGeneration import calculateAverage
from src.pyion.cr import get_ratios
from src.pyion.excel_reader import read_file
from src.pyion.voltage_stdev import voltage_stdev


class MainTestCase(unittest.TestCase):
    #Runner returns nothing
    def test_validate_cmd_line_returns_none(self):
        self.assertIsNone(main.validate_cmd_line())


    def test_create_table_is_not_none(self):

        pyion_data = read_file(sys.argv[1])
        pyion_data.add_entry("v_stdev", "Voltage SD", "mV", voltage_stdev(pyion_data.voltage.value))
        pyion_data.add_entry("v_avg", "Voltage Average", "mV", calculateAverage(pyion_data.voltage.value))
        pyion_data.add_entry("c_ratios", "Concentration Ratios", "None",
                             get_ratios(pyion_data.ci.value, pyion_data.vi.value,
                                        pyion_data.cs.value, pyion_data.v_add.value))

        self.assertIsNotNone(pyion_data.create_table())