import psutil

memory = psutil.virtual_memory()

print("=== Memory Usage ===")
print(f"Total Memory : {memory.total / (1024**3):.2f} GB")
print(f"Used Memory  : {memory.used / (1024**3):.2f} GB")
print(f"Free Memory  : {memory.available / (1024**3):.2f} GB")
print(f"Usage        : {memory.percent}%")
