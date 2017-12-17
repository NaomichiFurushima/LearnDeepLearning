import sys, os
sys.path.append("../../src/Chapter2")
import Gate as g
import unittest

class TestTestTest(unittest.TestCase):
    def test_and(self):
        self.assertEqual(0, g.AND((0, 0)))
        self.assertEqual(0, g.AND((0, 1)))
        self.assertEqual(1, g.AND((1, 1)))
        self.assertEqual(0, g.AND((1, 0)))
    def test_or(self):
        self.assertEqual(0, g.OR((0, 0)))
        self.assertEqual(1, g.OR((0, 1)))
        self.assertEqual(1, g.OR((1, 1)))
        self.assertEqual(1, g.OR((1, 0)))
    def test_NAND(self):
        self.assertEqual(1, g.NAND((0, 0)))
        self.assertEqual(1, g.NAND((0, 1)))
        self.assertEqual(0, g.NAND((1, 1)))
        self.assertEqual(1, g.NAND((1, 0)))

if __name__ == "__main__":
    unittest.main()
