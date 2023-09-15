# Write a program that will collect any number of grades from a user.
# Your program will sort these grades numerically from highest to lowest and calculate the grade point average of the user.
# Your program will then ask for the average the user desires
# and calculate what the user must get on their next assignment to achieve this average.
# Lastly, your program will make a copy of the users grades and allow them to alter one of their previous grades
# to see how doing worse or better on an assignment would have changed their overall average.

print("Welcome to Grade Point Average Calculator App")
name = input("\nEnter Your Name:")
num = int(input("How many grades would you like to enter:"))
grades = []

# grade's input from user
for i in range(num):
    grade = int(input("Enter Grades: "))
    grades.append(grade)

# sorting the grades list from highest to lowest
grades.sort(reverse=True)
print("\nGrades from Highest to Lowest:")
for i in grades:
    print(str(i))

# average of grades
ave_grade = sum(grades)/len(grades)
ave_grade = round(ave_grade, 2)

# printing student summary:
print("\n"+name+" Grade Summary")
print("Your Name: "+name)
print("Total Number of Grades: "+str(num))
print("Highest Grade: "+str(max(grades)))
print("Lowest Grade: "+str(min(grades)))
print("Average ig Grades: "+str(ave_grade))

# desired average
desired_avg = float(input("\nWhat is your desired average: "))
req_grades = desired_avg * (len(grades)+1) - sum(grades)
req_grades = round(req_grades, 2)

print("\nGood Luck "+name+"!")
print("You will need to get a "+str(req_grades)+" on your next assignment to earn a "+str(desired_avg)+" average")

print("\nLet's see what your average could have been if you did better/worse on an assignment.")
new_grade = int(input("What grade would you like to change: "))
new_grade1 = int(input("What grade would you like to change "+str(new_grade)+" to: "))
original_grades = grades
grades.remove(new_grade)
grades.append(new_grade1)
grades.sort(reverse=True)

print("\nNew Grades from Highest to Lowest:")
print(grades)

# new average grades
new_ave_grade = sum(grades)/len(grades)
new_ave_grade = round(new_ave_grade, 2)

# printing student summary with new grades:
print(name+" Grade Summary")
print("Your Name: "+name)
print("Total Number of Grades: "+str(num))
print("Highest Grade: "+str(max(grades)))
print("Lowest Grade: "+str(min(grades)))
print("Average ig Grades: "+str(new_ave_grade))

print("\nYour new average would be a "+str(new_ave_grade)+" compared to your real average of "+str(ave_grade))
dif_avg = new_ave_grade - ave_grade
dif_avg = round(dif_avg, 2)
print("This is a change of "+str(dif_avg)+" points!")

# printing the original grades
print("\nToo bad your original grades are still the same!")
print(original_grades)
print("You should go and ask for extra credit!")


