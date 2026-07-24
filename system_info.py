import platform
import socket

print("=== System Information ===")
print(f"Operating System : {platform.system()}")
print(f"Release          : {platform.release()}")
print(f"Version          : {platform.version()}")
print(f"Machine          : {platform.machine()}")
print(f"Processor        : {platform.processor()}")
print(f"Hostname         : {socket.gethostname()}")
