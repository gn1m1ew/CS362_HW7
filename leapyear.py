# Name: Ming Wei
# Course: CS 362
# Description: leap year implementation
# Due: 3/7/2021

# To get year (integer input) from the user
def leapyear(year):
	# if the input is invalid value
	if year < 0:
		raise ValueError ("Invalid Value")

	# main function of checking leap year
	if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
		return ("It is a leap year!")
	else:
		return ("It is not a leap year!")

# print result
# year = 2020
# print(leapyear(year))
