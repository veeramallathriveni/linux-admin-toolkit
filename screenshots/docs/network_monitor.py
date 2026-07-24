import psutil

print("=" * 40)
print("Network Monitor")
print("=" * 40)

network = psutil.net_io_counters()

print(f"Bytes Sent     : {network.bytes_sent}")
print(f"Bytes Received : {network.bytes_recv}")
print(f"Packets Sent   : {network.packets_sent}")
print(f"Packets Received: {network.packets_recv}")
