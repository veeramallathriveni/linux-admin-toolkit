import psutil

disk = psutil.disk_usage('/')

print("=== Disk Usage ===")
print(f"Total Space : {disk.total / (1024**3):.2f} GB")
print(f"Used Space  : {disk.used / (1024**3):.2f} GB")
print(f"Free Space  : {disk.free / (1024**3):.2f} GB")
print(f"Usage       : {disk.percent}%")
