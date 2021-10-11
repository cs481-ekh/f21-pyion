import unittest

from src.pyion.averageGeneration import *

class averageGenerationTestCase(unittest.TestCase):

        def test_calculateAverage_returns_none(self):
            exampleVoltageInput = [0.3,0.5,0.6,0.7]
            #if the input voltage list contains no element,calculateAverage() should return none
            self.assertIsNone(calculateAverage(exampleVoltageInput))

        def test_calculateAverage_returns_empty(self):
            exampleVoltageInput = []
            #if the input voltage list is empty, then the calculateAverage() should return an empty list
            averagelist = calculateAverage(exampleVoltageInput)
            lengthofaveragelist = len(averagelist)
            self.assertEqual(lengthofaveragelist,0)

