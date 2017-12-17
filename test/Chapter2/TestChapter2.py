import sys, os
sys.path.append("../../src/Chapter2")
import Gate as g
import unittest

class TestTestTest(unittest.TestCase):
    def test_and(self):
        self.assertEqual(0, g.AND([0, 0]))

if __name__ == "__main__":
    unittest.main()
