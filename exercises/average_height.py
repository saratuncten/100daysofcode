#input python list of student heights
print("Input student heights:\n")
student_heights = input().split()
for n in range (0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

#get total height of all students
total_height = 0
for height in student_heights:
  total_height += height
print(f"Total height: {total_height}")

#get number of students
number_of_students = 0
for height in student_heights:
  number_of_students += 1
print(f"Number of students: {number_of_students}")

#get average height of students
average_height = round(total_height/number_of_students)
print(f"Average height: {average_height}")
