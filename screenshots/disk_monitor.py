import psutil

disk = psutil.disk_usage('/')

print("=" * 40)
print("Disk Space Monitor")
print("=" * 40)

print(f"Total Space : {round(disk.total/(1024**3),2)} GB")
print(f"Used Space  : {round(disk.used/(1024**3),2)} GB")
print(f"Free Space  : {round(disk.free/(1024**3),2)} GB")
print(f"Usage       : {disk.percent}%")
