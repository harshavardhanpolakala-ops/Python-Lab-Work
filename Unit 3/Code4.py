
# Attendance Tracker

students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    status = input("Enter attendance (Present/Absent): ").lower()
    students[name] = status

print("\n--- ATTENDANCE REPORT ---")

present = 0
absent = 0

for name, status in students.items():
    print(name, ":", status)

    if status == "present":
        present += 1
    else:
        absent += 1

print("\nTotal Students:", n)
print("Present:", present)
print("Absent:", absent)
