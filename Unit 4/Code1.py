
# Log File Reader Program

filename = input("Enter log file name: ")

try:
    with open(filename, "r") as file:
        print("\n--- LOG FILE CONTENTS ---")

        for line in file:
            print(line.strip())

except FileNotFoundError:
    print("Error: Log file not found.")
