import sys, os
sys.path.append("../../src/Chapter2")
import Gate as g
import unittest

class TestTestTest(unittest.TestCase):
    def twoGateTest(self, pattern, func):#pattern(p, x1, x2)
        map(lambda p : self.assertEqual(p[0], func((p[1], p[2]))), pattern)

    def test_and(self):
        pat = [(0,0,0),(0,1,0),(1,1,1),(0,0,1)]
        self.twoGateTest(pat, g.AND)
    def test_or(self):
        pat = [(0,0,0),(1,1,0),(1,1,1),(1,0,1)]
        self.twoGateTest(pat, g.OR)
    def test_NAND(self):
        pat = [(1,0,0),(1,1,0),(0,1,1),(1,0,1)]
        self.twoGateTest(pat, g.NAND)
    def test_XOR(self):
        pat = [(0,0,0),(1,1,0),(0,1,1),(1,0,1)]
        self.twoGateTest(pat, g.XOR)

if __name__ == "__main__":
    unittest.main()
