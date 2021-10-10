import unittest
from src.pyion.voltage_stdev import voltage_stdev
from statistics import stdev

class StdevTestCase(unittest.TestCase):

    def test_voltage_stdev_returns_none(self):
        example_v = [0.51334,-0.23475,0.83452,0.12362,1.35462,-2.54642,0.61371]
        #voltage_stdev should return none if the length of the volatage list is not divisible by 3
        ex_v = example_v
        self.assertIsNone(voltage_stdev(ex_v[:4]))
        self.assertIsNone(voltage_stdev(ex_v))

    def test_voltage_stdev_equality(self):
        example_v = [0.51334,-0.23475,0.83452,0.12362,1.35462,-2.54642,0.61371]
        ex_v = example_v
        self.assertEqual(voltage_stdev(ex_v[:6])[0],stdev(ex_v[:3]))
        self.assertEqual(voltage_stdev(ex_v[:6])[1],stdev(ex_v[3:6]))
