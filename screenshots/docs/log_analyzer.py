import os

log_file = "sample.log"

if os.path.exists(log_file):
    with open(log_file, "r") as file:
        lines = file.readlines()

    print("Total log entries:", len(lines))
else:
    print("sample.log not found.")
