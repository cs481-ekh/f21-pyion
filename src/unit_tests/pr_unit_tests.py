import unittest
from src.pyion.pr import *

class PrTestCase(unittest.TestCase):
    def __init__(self):
        super(PrTestCase,self).__init()
        self.ex_temp = 22.5
        self.ex_voltage_list = [0.137903333,-3.915056667,-10.44966333,
                                -19.37291667,-30.32007667,-43.84314333,
                                -59.29757333,-77.23134667,-97.02810333,
                                -119.0028033,-143.4083133,-169.5869,-196.1884967]
        self.ex_cr_list = [1,1.584158416,2.156862745,
                            2.718446602,3.269230769,4.075829384,
                            4.859813084,5.871559633,6.846846847,
                            8.245614035,10,11.83673469,13.90625]



    def test_get_pr_list_returns_list(self):
        pr_list = get_pr_list(self.ex_voltage_list,self.ex_temp,self.ex_cr_list)
        self.assertTrue(isinstance(pr_list,list))

    def test_get_pr_list_unequal(self):
        pr_list = get_pr_list(self.ex_voltage_list,self.ex_temp,self.ex_cr_list[:3])
        self.assertIsNone(pr_list)

    

    