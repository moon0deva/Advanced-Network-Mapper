#!/usr/bin/env python3

import json
import subprocess
from jinja2 import Template
from datetime import datetime
from pathlib import Path

# -------- SETTINGS --------
subnet = "your IP HEre/subnet" # example: 192.168.0.0/24
common_ports = "22,80,443,3306,8080,8443" # Ports
output_json = "scan_report.json"
output_html = "scan_report.html"

# -------- NMAP SCAN --------
def run_nmap_scan():
    print(f"[*] Scanning subnet: {subnet} for ports: {common_ports}")
    cmd = [
        "nmap", "-Pn", "-n", "-T4",
        "-p", common_ports,
        "-oX", "-",  # XML to stdout
        subnet
    ]
    try:
        result = subprocess.check_output(cmd).decode()
        return result
    except subprocess.CalledProcessError as e:
        print(f"[!] Nmap scan failed: {e}")
        return None

# -------- XML PARSE (BASIC) --------
def parse_nmap_xml(xml_output):
    from xml.etree import ElementTree as ET
    root = ET.fromstring(xml_output)
    results = []

    for host in root.findall("host"):
        ip = host.find("address").get("addr")
        status = host.find("status").get("state")
        ports = []

        for port in host.find("ports").findall("port"):
            portid = port.get("portid")
            proto = port.get("protocol")
            state = port.find("state").get("state")
            service = port.find("service").get("name", "unknown")
            ports.append({
                "port": portid,
                "proto": proto,
                "state": state,
                "service": service
            })

        results.append({
            "ip": ip,
            "status": status,
            "ports": ports
        })

    return results

# -------- HTML REPORT --------
def generate_html_report(data):
    html_template = """
    <html>
    <head>
        <title>Advanced Network Scan Report</title>
        <style>
            body { font-family: Arial; background-color: #f4f4f4; }
            table { border-collapse: collapse; width: 100%; background: white; }
            th, td { padding: 8px 12px; border: 1px solid #ccc; text-align: left; }
            th { background: #222; color: white; }
            h2 { background: #333; color: white; padding: 10px; }
        </style>
    </head>
    <body>
        <h2>Advanced Network Scan Report</h2>
        <p>Scan Date: {{ date }}</p>
        {% for host in data %}
        <h3>{{ host.ip }} ({{ host.status }})</h3>
        <table>
            <tr><th>Port</th><th>Protocol</th><th>State</th><th>Service</th></tr>
            {% for port in host.ports %}
            <tr>
                <td>{{ port.port }}</td>
                <td>{{ port.proto }}</td>
                <td>{{ port.state }}</td>
                <td>{{ port.service }}</td>
            </tr>
            {% endfor %}
        </table>
        {% endfor %}
    </body>
    </html>
    """
    template = Template(html_template)
    report = template.render(data=data, date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    with open(output_html, "w") as f:
        f.write(report)
    print(f"[+] HTML report saved: {output_html}")

# -------- MAIN --------
def main():
    print("[🔥] Running Advanced Network Mapper...\n")
    xml_result = run_nmap_scan()
    if not xml_result:
        return

    parsed_data = parse_nmap_xml(xml_result)

    with open(output_json, "w") as f:
        json.dump(parsed_data, f, indent=2)
    print(f"[+] JSON report saved: {output_json}")

    generate_html_report(parsed_data)

    print("\n[✅] Scan complete. Reports generated.")

if __name__ == "__main__":
    main()
