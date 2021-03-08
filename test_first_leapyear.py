import unittest
import test_first_leapyear_implementation

class TestCase(unittest.TestCase):
	def test1(self):
		self.assertEqual(test_first_leapyear_implementation.leapyear(2020), "It is a leap year!")

if __name__ == '__main__':
	unittest.main()