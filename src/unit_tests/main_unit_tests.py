import unittest
import src.pyion.main as main


class MainTestCase(unittest.TestCase):
    #Runner returns nothing
    def test_validate_cmd_line_returns_none(self):
        self.assertIsNone(main.validate_cmd_line())

        