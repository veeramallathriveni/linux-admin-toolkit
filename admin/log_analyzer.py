print("=== Log Analyzer ===")

with open("sample.log", "r") as file:
    lines = file.readlines()

print(f"Total log entries: {len(lines)}")
