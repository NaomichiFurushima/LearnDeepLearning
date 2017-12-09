import sys, os
sys.path.append("../src")
import testTest as tt
import unittest

class TestTestTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(5, tt.add(2,3))

if __name__ == "__main__":
    unittest.main()
