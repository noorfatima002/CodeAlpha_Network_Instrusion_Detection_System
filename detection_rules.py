# IDS Detection Rules

SUSPICIOUS_PORTS = {
    21: "FTP",
    23: "Telnet",
    445: "SMB",
    3389: "RDP"
}

def detect_suspicious_port(port):
    return port in SUSPICIOUS_PORTS


def get_service_name(port):
    return SUSPICIOUS_PORTS.get(port, "Unknown")