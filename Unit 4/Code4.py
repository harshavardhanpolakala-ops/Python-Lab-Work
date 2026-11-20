
import json

# Read JSON log file
with open("logs.json", "r") as file:
    logs = json.load(file)

print("\n--- LOG FILE ANALYZER ---")

error_count = 0
warning_count = 0
info_count = 0

for log in logs:
    print("Level:", log["level"])
    print("Message:", log["message"])
    print("--------------------")

    if log["level"] == "ERROR":
        error_count += 1
    elif log["level"] == "WARNING":
        warning_count += 1
    elif log["level"] == "INFO":
        info_count += 1

print("\n--- LOG SUMMARY ---")
print("Total Logs:", len(logs))
print("Errors:", error_count)
print("Warnings:", warning_count)
print("Info:", info_count)
