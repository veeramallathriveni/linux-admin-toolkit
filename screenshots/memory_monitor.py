import psutil

print("=" * 40)
print("Memory Monitor")
print("=" * 40)

memory = psutil.virtual_memory()

print(f"Total Memory : {round(memory.total / (1024**3), 2)} GB")
print(f"Used Memory  : {round(memory.used / (1024**3), 2)} GB")
print(f"Free Memory  : {round(memory.available / (1024**3), 2)} GB")
print(f"Usage        : {memory.percent}%")
