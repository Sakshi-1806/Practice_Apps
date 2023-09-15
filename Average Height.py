import math
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

sum_height = 0
for i in range(0, len(student_heights)):
    sum_height = sum_height + student_heights[0]

ave_height = sum_height / len(student_heights)
ave_height = round(ave_height)

print(ave_height)



