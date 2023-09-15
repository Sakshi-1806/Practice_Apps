import random

n1 = 0
n2 = 1
dec = random.randint(n1, n2)
# just to check if it's working
print(str(dec))
if dec == 0:
    print("Tails")
else:
    print("Heads")
