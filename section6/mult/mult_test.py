import unittest
from mult import mult
import random

class MultTests(unittest.TestCase):
    def test1(self):
        """3x4 = 12"""
        self.assertEqual(mult(3, 4), 12)
    def test2(self):
        """-5x4 = -20"""
        self.assertEqual(mult(-5, 4), -20)
    def test3(self):
        """Nested (2x3)x4 = 24"""
        self.assertEqual(mult(mult(2, 3), 4), 24)
    def test4(self):
        """1000 random tests"""
        for _ in range(1000):
            a = random.randint(-100, 100)
            b = random.randint(-100, 100)
            # This seems pointless, but imagine a more complicated function 
            # Or imagine testing a fast algorithm!
            self.assertEqual(mult(a, b), a*b)

def main():
    unittest.main()

main()
