import math
number = int(input("please Enter integer number: "))
if number < 0:
    print("Sorry, factorial does not exist for negative numbers")
else:
    result = math.factorial(number)
    print("The factorial of {} is: {}".format(number, result))
