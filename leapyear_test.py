import leapyear
import unittest

class TestCase(unittest.TestCase):
    def testleap1(self):
        self.assertEqual(leapyear.leapyear(2020), "It is a leap year!")
    def testleap2(self):
        self.assertEqual(leapyear.leapyear(2019), "It is not a leap year!")
    
if __name__ == '__main__':
    unittest.main(verbosity=2)