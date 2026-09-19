# Intrusion Response Mechanism

from datetime import datetime

def respond_to_intrusion(source_ip, port, service):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("alerts.log", "a") as log:
        log.write(
            f"{timestamp} | ALERT | Source IP: {source_ip} | "
            f"Port: {port} | Service: {service}\n"
        )

    print("⚠️ Intrusion Detected!")
    print(f"Source IP: {source_ip}")
    print(f"Port: {port}")
    print(f"Service: {service}")
    print(f"Alert logged at: {timestamp}")
