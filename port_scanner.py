import socket
from datetime import datetime
import threading

# Prompt user for target IP
target = input("Enter target IP address (e.g., 127.0.0.1): ")

# Mark the start time
start_time = datetime.now()
print(f"\n[+] Starting scan on {target}...\n")

# Function to scan a single port and grab banner
def scan_port(port):
    try:
        s = socket.socket()
        s.settimeout(0.5)
        s.connect((target, port))
        try:
            banner = s.recv(1024).decode().strip()
        except:
            banner = "No banner received"
        print(f"[+] Port {port} is OPEN - Banner: {banner}")
        s.close()
    except:
        pass  # Ignore closed ports or timeouts silently

# Create and start threads
threads = []
for port in range(1, 1025):
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

# Mark the end time
end_time = datetime.now()
print(f"\n[✓] Scan completed in: {end_time - start_time}")
