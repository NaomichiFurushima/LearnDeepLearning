import sys, os
sys.path.append("../../src/Chapter2")
import Gate as g
import unittest

class Chapter2Test(unittest.TestCase):
    def test_and(self):
        self.assertEqual(0, g.AND([{0:0.5},{0:0.5}],-0.7))
        self.assertEqual(0, g.AND([{0:0.5},{1:0.5}],-0.7))
        self.assertEqual(1, g.AND([{1:0.5},{1:0.5}],-0.7))
        self.assertEqual(0, g.AND([{0:0.5},{0:0.5}],-0.7))

if __name__ == "__main__":
    unittest.main()
