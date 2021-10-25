import unittest
from src.pyion.graph_maker import *
from src.pyion.objects.PyionUnit import PyionUnit


class GraphMakerTestCase(unittest.TestCase):
    # Data source none throws exception
    def test_graph_single_throws_issue_when_none_given(self):
        with self.assertRaises(Exception):
            graph_single(None)

    def test_graph_single_throws_issue_when_data_is_int(self):
        with self.assertRaises(Exception):
            data = PyionUnit("test", "none", 1)
            graph_single(data)


