def leapyear(year):
	# main function of checking leap year
	if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
		return ("It is a leap year!")
	else:
		return ("It is not a leap year!")