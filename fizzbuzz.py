# Name: Ming Wei
# Course: CS 362
# Description: fizzbuzz implementation
# Due: 3/7/2021


def fizzbuzz(num):
    # Number divisible by 15, print 'FizzBuzz'
    if num % 15 == 0:
        return ("FizzBuzz")

    # Number divisible by 3, print 'Fizz'
    elif num % 3 == 0:     
        return ("Fizz")                                         

    # Number divisible by 5, print 'Buzz'
    elif num % 5 == 0:         
        return ("Buzz")

    else:
        return num                                

#  print num
# for num in range(1,100):
#     print(fizzbuzz(num))
