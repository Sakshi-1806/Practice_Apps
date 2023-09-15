# Write a program that will display the solutions to any number of quadratic equations.
# Your program will ask the user how many quadratic equations they would like to solve,
# ask for the coefficients of the equation in the standard form of ax2 + bx + c = 0 ,
# solve for x, and then display the solutions.
# Your program will allow for both real and complex solutions.

import cmath
print("Welcome to Quadratic Equation Solver App:")
print("\nA Quadratic Equation form should be: ax^2+bx+c=0")
print("Your Solution can be real or complex numbers.")
print("A complex number has two parts: a+bj")
print("Where the a is the real portion and bj is the imaginary portion.")

# user input
num_of_equations = int(input("\nHow many equations would you like to solve today:"))

# solution of equations
for i in range(num_of_equations):
    print("\nSolving equation #"+str(i+1))
    print("---------------------------------------")
    a = float(input("Enter the value of a (coefficient of x^2:)"))
    b = float(input("Enter the value of b (coefficient of x:)"))
    c = float(input("Enter the value of c (coefficient:)"))

    # solution of quadratic equation
    print("\nThe solution to "+str(a)+"x^2 + "+str(b)+"x + "+str(c)+" are:")
    x1 = (-b+cmath.sqrt(b**2-4*a*c))/(2*a)
    x2 = (-b+cmath.sqrt(b**2-4*a*c))/(2*a)
    print("\n x1= "+str(x1))
    print("\n x2= "+str(x2))

print("Thank you for using Quadratic Equation App")
