import unittest
from src.pyion.cr import *

class CrTestCase(unittest.TestCase):
    def __init__(self):
        super(CrTestCase,self).__init()
        self.ex_c_init = 50
        self.ex_vol_init = 1000
        self.ex_c_add = 3000
        self.ex_vol_add_list = [0,10,10,10,10,15,15,20,20,30,40,45,55]

    def test_cr_get_ratios_returns_list(self):
        ratios_list = get_ratios(self.ex_c_init,self.ex_vol_init,self.ex_c_add,self.ex_vol_add_list)
        self.assertTrue(isinstance(ratios_list,list))

    def test_cr_get_ratios_neg_c_init(self):
        with self.assertRaises(Exception):
            get_ratios(-1*self.ex_c_init,self.ex_vol_init,self.ex_c_add,self.ex_vol_add_list)

    def test_cr_get_ratios_neg_vol_init(self):
        with self.assertRaises(Exception):
            get_ratios(self.ex_c_init,-1*self.ex_vol_init,self.ex_c_add,self.ex_vol_add_list)

    def test_cr_get_ratios_neg_c_add(self):
        with self.assertRaises(Exception):
            get_ratios(self.ex_c_init,self.ex_vol_init,-1*self.ex_c_add,self.ex_vol_add_list)

    def test_cr_get_ratios_neg_vol_add_list(self):
        with self.assertRaises(Exception):
            neg_vol_add_list = [10.0,20.0,-20.0,-30.0,15.0]
            get_ratios(self.ex_c_init,self.ex_vol_init,self.ex_c_add,neg_vol_add_list)

    def test_cr_get_ratios_without_vol_add_list(self):
        with self.assertRaises(Exception):
            get_ratios(self.ex_c_init,self.ex_vol_init,self.ex_c_add)

    def test_cr_get_ratios_empty_vol_add_list(self):
        with self.assertRaises(Exception):
            empty_list = []
            get_ratios(self.ex_c_init,self.ex_vol_init,self.ex_c_add,empty_list)
