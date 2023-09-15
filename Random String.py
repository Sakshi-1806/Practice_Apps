import random
# Split string method

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

random_choice = str(random.choices(names))
print(random_choice+" is going to you meal today!")

