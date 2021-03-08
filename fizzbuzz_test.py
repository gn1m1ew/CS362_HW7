import fizzbuzz
import unittest

class TestCase(unittest.TestCase):
    def testfizz1(self):
        self.assertEqual(fizzbuzz.fizzbuzz(3), "Fizz")
    def testfizz2(self):
        self.assertEqual(fizzbuzz.fizzbuzz(6), "Fizz")
    def testfizz3(self):
        self.assertEqual(fizzbuzz.fizzbuzz(9), "Fizz")

    def testbuzz1(self):
        self.assertEqual(fizzbuzz.fizzbuzz(5), "Buzz")
    def testbuzz2(self):
        self.assertEqual(fizzbuzz.fizzbuzz(25), "Buzz")
    def testbuzz3(self):
        self.assertEqual(fizzbuzz.fizzbuzz(55), "Buzz")

    def testfizzbuzz1(self):
        self.assertEqual(fizzbuzz.fizzbuzz(15), "FizzBuzz")
    def testfizzbuzz2(self):
        self.assertEqual(fizzbuzz.fizzbuzz(30), "FizzBuzz")
    def testfizzbuzz3(self):
        self.assertEqual(fizzbuzz.fizzbuzz(60), "FizzBuzz")

    def testinteger1(self):
        self.assertEqual(fizzbuzz.fizzbuzz(2), 2)
    def testinteger2(self):
        self.assertEqual(fizzbuzz.fizzbuzz(37), 37)
    def testinteger3(self):
        self.assertEqual(fizzbuzz.fizzbuzz(79), 79)
    
if __name__ == '__main__':
    unittest.main(verbosity=2)