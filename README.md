Advanced Network Mapper (ANM) is a Python 3-based utility that performs fast and efficient subnet scanning using nmap, and generates both JSON and HTML formatted reports of open ports and detected services.

This tool is ideal for system administrators, cybersecurity professionals, and penetration testers looking to quickly assess the state of hosts on a network.

**FEATURES**

~ Parses nmap XML output directly

~ Outputs JSON report for machine-readable integration

~ Generates clean and styled HTML reports

~ Fast scanning with multithreaded Nmap (-T4)

~ Works with any /subnet format (e.g., /24, /16)

~ No database or external service dependencies

**HOW TO RUN THE SCRIPT**

python -m venv /path/to/new/virtual/environment #Create a venv Environment

Source /path/to/new/virtual/environment/bin/activate # Activate venv

apt install nmap # nmap

pip3 install jinja2 # Jinja

chmod +x ANM.py # permission

./ANM.py # Run the script

**CONFIGURE THE SCRIPT**

Before running the script, you'll need to update a few variables at the top of the file to match your network environment and scanning needs.

Open the Python script (ANM.py) in your favorite text editor and locate the following section near the top:

**SETTINGS**
subnet = "your IP Here/subnet"  # example: 192.168.0.0/24

common_ports = "22,80,443,3306,8080,8443"  # Ports

output_json = "scan_report.json"

output_html = "scan_report.html"

Avoid wide scans in production environments unless you know the risks.

DISCLAIMER:
This script is intended for authorized network scanning and cybersecurity research only.
You must have proper permission to scan and analyze any network using this tool.
Unauthorized use of this script against systems you do not own or have explicit consent to test
is illegal and unethical.

The author is not responsible for any misuse, damage, or legal consequences that may result
from using this script. Use responsibly and stay within the boundaries of the law.



