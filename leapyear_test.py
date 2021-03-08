# Name: Ming Wei
# Course: CS 362
# Description: leap year test
# Due: 3/7/2021

import leapyear
import unittest

# first test 
class FirstTestCase(unittest.TestCase):
    def testleap0(self):
        self.assertEqual(leapyear.leapyear(2012), "It is a leap year!")

# after implement code test
class TestCase(unittest.TestCase):
    def testleap1(self):
        self.assertEqual(leapyear.leapyear(2020), "It is a leap year!")
    def testleap2(self):
        self.assertEqual(leapyear.leapyear(2019), "It is not a leap year!")
    
if __name__ == '__main__':
    unittest.main(verbosity=2)