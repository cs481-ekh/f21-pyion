import unittest
import src.pyion.voltage_stdev.py as v_stdev
from statistics import stdev

class StdevTestCase(unittest.TestCase):
    def test_voltage_stdev_returns_none(self):
        #voltage_stdev should return none if the length of the volatage list is not divisible by 3
        self.assertIsNone(v_stdev.voltage_stdev([0.51334,-0.23475,0.83452,0.12362]))
        self.assertEqual(v_stdev.voltage_stdev([0.51334,-0.23475,0.83452])[0],stdev([0.51334,-0.23475,0.83452]))

