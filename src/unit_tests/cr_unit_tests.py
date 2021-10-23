import unittest
from src.pyion.cr import *

class StdevTestCase(unittest.TestCase):
    def __init__(self):
        super(StdevTestCase,self).__init()
        self.ex_c_init = 50
        self.ex_vol_init = 1000
        self.ex_c_add = 3000
        self.ex_vol_add_list = [0,10,10,10,10,15,15,20,20,30,40,45,55]

    def test_cr_get_ratios_returns_list(self):
        ratios_list = get_ratios(self.ex_c_init,self.ex_vol_init,self.ex_c_add,self.ex_vol_add_list)
        self.assertTrue(isinstance(ratios_list,list))
