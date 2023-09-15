# write a program that will compute the first n terms of the Fibonacci Sequence.
# Your program will then display these terms.
# Next, your program will calculate the ratios of consecutive Fibonacci numbers
# To prove that these ratios approach the irrational mathematical constant of Phi; 1.618….


print("Welcome to Fibonacci Calculator App")
num = int(input("How many digits of the Fibonacci Sequence you like to Compute:"))

# compute the value of fibonacci:
fib = [1, 1]
for i in range(num-2):
    new_fib = fib[i]+fib[i+1]
    fib.append(new_fib)

# display fibonacci series:
print("The first "+str(num)+" numbers of Fibonacci Series are:")
for i in range(num):
    print(fib[i])

# calculating ratios of consecutive fibonacci series:
golden = []
for a in range(len(fib)-1):
    ratio_con = fib[a+1]/fib[a]
    golden.append(ratio_con)

# display golden ratio value:
print("\nThe corresponding golden ratio values are:")
for ratio_con in golden:
    print(ratio_con)

print("\nThe ratio of consecutive Fibonacci terms approaches Phi; 1.618...")
