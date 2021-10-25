import unittest
from src.pyion.objects.PyionUnit import PyionUnit
from src.pyion.objects.PyionData import PyionData


class GraphMakerTestCase(unittest.TestCase):
    # Data source none throws exception
    def test_create_table_returns_str(self):
        pyion_data = PyionData()
        pyion_data.add_entry("test1", "Test 1", "NA", [1,2,3])
        self.assertIsNotNone(pyion_data.create_table())


