# write a program that will calculate the factorial of any given number.
# Your program will display the mathematical relationship of the factorial.
# It will then use the math library to compute the value of the given factorial.
# Lastly, your program will use its own algorithm to compute the value of the given factorial and compare the results.

import math

print("Welcome Factorial Calculator App")

num = int(input("\nWhat number would you like to compute the factorial of?"))
print(str(num)+"! =", end="")
fact = 1
for i in range(1, num):
    print(str(i), end="*")
print(num)
# factorial using for loop:
for i in range(1, num):
    fact = fact*i
print("\nHere is the result from the Math Library:")
print("Factorial of "+str(num)+" is "+str(fact)+"!")

# factorial using in-built function:
fact = math.factorial(num)
print("\nHere is the result from the Math Library:")
print("Factorial of "+str(num)+" is "+str(fact)+"!")

print("\nIt shows twice that "+str(num)+"! = "+str(fact)+" (with excitement)")
