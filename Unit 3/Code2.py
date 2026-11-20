
# Student Grading System

name = input("Enter student name: ")
marks = []

for i in range(1, 6):
    mark = float(input("Enter marks for subject " + str(i) + ": "))
    marks.append(mark)

total = sum(marks)
average = total / 5

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
elif average >= 40:
    grade = "E"
else:
    grade = "F"

print("\n--- STUDENT RESULT ---")
print("Student Name:", name)
print("Total Marks:", total)
print("Average Marks:", average)
print("Grade:", grade)
