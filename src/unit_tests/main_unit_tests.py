import unittest
import src.pyion.main as main


class MainTestCase(unittest.TestCase):
    #Runner returns nothing
    def test_runner_returns_none(self):
        self.assertIsNone(main.runner())
