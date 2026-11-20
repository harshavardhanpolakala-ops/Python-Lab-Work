
# Student Data Manager Using Files

filename = "students.txt"

while True:
    print("\n--- STUDENT DATA MANAGER ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        usn = input("Enter student USN: ")

        with open(filename, "a") as file:
            file.write(name + "," + usn + "\n")

        print("Student details saved successfully.")

    elif choice == "2":
        try:
            with open(filename, "r") as file:
                print("\n--- STUDENT DETAILS ---")
                print(file.read())

        except FileNotFoundError:
            print("No student records found.")

    elif choice == "3":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Try again.")
