
# CSV-Based Payroll Management System

import csv

filename = "payroll.csv"

while True:
    print("\n--- PAYROLL MANAGEMENT SYSTEM ---")
    print("1. Add Employee Salary")
    print("2. View Payroll")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter employee name: ")
        salary = float(input("Enter basic salary: "))
        bonus = float(input("Enter bonus: "))

        total_salary = salary + bonus

        with open(filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, salary, bonus, total_salary])

        print("Employee payroll saved successfully.")

    elif choice == "2":
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)

                print("\n--- PAYROLL DETAILS ---")
                print("Name | Basic Salary | Bonus | Total Salary")

                for row in reader:
                    print(" | ".join(row))

        except FileNotFoundError:
            print("No payroll records found.")

    elif choice == "3":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Try again.")
