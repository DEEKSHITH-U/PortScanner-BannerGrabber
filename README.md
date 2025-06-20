# 🔍 Python Port Scanner & Banner Grabber

A fast and lightweight network reconnaissance tool built using Python. It scans common TCP ports (1–1024) on a target IP and attempts to retrieve service banners. The tool is multithreaded, which significantly reduces scan time compared to traditional sequential scans.

---

## 💡 Features
- Scans TCP ports from 1 to 1024
- Identifies open ports
- Attempts to grab banners from services running on those ports
- Implements multithreading for high-speed scanning
- Displays total scan time
- Easy-to-use command-line interface

---

## 🛠️ Technologies Used
- **Python 3**
- `socket` – to establish TCP connections and receive service banners
- `threading` – to scan multiple ports concurrently
- `datetime` – to calculate total time taken for the scan

---

## 🚀 How to Run

1. Open your terminal and navigate to the project directory.
2. Run the script:
   ```bash
   python port_scanner.py
3. When prompted, enter the IP address of the target host (e.g., 127.0.0.1, scanme.nmap.org, or your local network IP).

---

## 🧪 Sample Output

Enter target IP address (e.g., 127.0.0.1): 127.0.0.1

[+] Port 135 is OPEN - Banner: No banner received
[+] Port 139 is OPEN - Banner: No banner received
[+] Port 445 is OPEN - Banner: No banner received

[✓] Scan completed in: 0:00:08.394

Note: Not all ports return readable banners; this is expected behavior for system-level services like SMB and RPC.

---

## 📚 Skills Demonstrated

- Network reconnaissance and enumeration
- Python socket programming
- TCP port scanning
- Multithreaded performance optimization
- Exception handling and timeout control
- CLI design for real-world tools
- Banner grabbing and service identification logic

---

## 📁 Project Structure

PortScanner-BannerGrabber/
├── port_scanner.py   # Main Python script
└── README.md         # Documentation file (this file)

---

## 📌 Disclaimer

This tool is created strictly for educational purposes and ethical hacking practice.
Only scan networks and systems that you own or have explicit permission to test.
Unauthorized scanning is illegal and unethical.

---

## 🔗 Author
Deekshith U  
GATE 2024 Qualified | Cybersecurity Intern | Passionate about Ethical Hacking  
GitHub: DEEKSHITH-U  
🌐 Portfolio: [https://deekshith-u.github.io](https://deekshith-u.github.io)

---
