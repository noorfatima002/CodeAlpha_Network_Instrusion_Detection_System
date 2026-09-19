# Network Intrusion Detection System

from detection_rules import detect_suspicious_port, get_service_name
from response import respond_to_intrusion
import time

traffic_events = [
    {"source_ip": "192.168.1.10", "destination_port": 80},
    {"source_ip": "192.168.1.20", "destination_port": 23},
    {"source_ip": "192.168.1.30", "destination_port": 443},
    {"source_ip": "192.168.1.40", "destination_port": 445},
]

print("=== Network Intrusion Detection System ===")
print("Monitoring simulated network traffic...\n")

for event in traffic_events:
    source_ip = event["source_ip"]
    port = event["destination_port"]

    if detect_suspicious_port(port):
        service = get_service_name(port)

        print(f"ALERT: Suspicious activity detected from {source_ip}")
        print(f"Port: {port} ({service})")

        respond_to_intrusion(source_ip, port, service)

    else:
        print(f"Normal traffic: {source_ip} -> Port {port}")

    time.sleep(1)