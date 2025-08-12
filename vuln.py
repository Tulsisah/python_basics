import os
import subprocess
from scapy.all import ARP, Ether, srp

def scan_subnet(subnet):
    """Scan the subnet to detect all devices."""
    print(f"Scanning subnet: {subnet}")
    devices = []

    # Create ARP request packet
    arp_request = ARP(pdst=subnet)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request

    # Send the request and capture responses
    answered_list = srp(arp_request_broadcast, timeout=2, verbose=False)[0]

    for sent, received in answered_list:
        devices.append({
            "ip": received.psrc,
            "mac": received.hwsrc
        })

    return devices


def check_open_ports():
    """Check for open ports on the system."""
    print("Checking for open ports...")
    try:
        result = subprocess.check_output("netstat -an", shell=True).decode()
        open_ports = [line for line in result.splitlines() if "LISTENING" in line or "ESTABLISHED" in line]
        return open_ports
    except subprocess.CalledProcessError as e:
        return [f"Error while checking open ports: {e.output.decode()}"]


def check_outdated_software():
    """Check for outdated software on the system."""
    print("Checking for outdated software...")
    outdated_check = subprocess.run(["wmic", "qfe", "list", "brief"], capture_output=True, text=True)
    if outdated_check.returncode == 0:
        return outdated_check.stdout.splitlines()
    return ["Unable to check for outdated software on this system."]


def check_firewall_status():
    """Check the status of the firewall."""
    print("Checking firewall status...")
    firewall_status = subprocess.run(["netsh", "advfirewall", "show", "allprofiles"], capture_output=True, text=True)
    if "State    OFF" in firewall_status.stdout:
        return "Firewall is inactive. Enable it using 'netsh advfirewall set allprofiles state on'."
    return "Firewall is active."


def check_weak_passwords():
    """Check for weak passwords on the system."""
    print("Checking for weak passwords...")
    weak_passwords = []
    try:
        with open("C:\\Windows\\System32\\config\\SAM", "r") as sam_file:
            for line in sam_file:
                if "PasswordNotRequired" in line:
                    weak_passwords.append(line.strip())
    except PermissionError:
        return ["Permission denied to access password database. Run as Administrator."]
    return weak_passwords


def check_insecure_services():
    """Check for insecure services running on the system."""
    print("Checking for insecure services...")
    insecure_services = []
    try:
        result = subprocess.check_output("sc query", shell=True).decode()
        for line in result.splitlines():
            if any(service in line for service in ["telnet", "ftp", "rsh"]):
                insecure_services.append(line)
    except subprocess.CalledProcessError:
        return ["Error while checking for insecure services."]
    return insecure_services


def detect_threats():
    """Detect all potential threats on the system."""
    threats = []

    # Open ports
    open_ports = check_open_ports()
    if open_ports:
        threats.append("Open ports detected:")
        threats.extend(open_ports)

    # Outdated software
    outdated_software = check_outdated_software()
    if outdated_software:
        threats.append("Outdated software detected:")
        threats.extend(outdated_software)

    # Firewall status
    firewall_status = check_firewall_status()
    if "inactive" in firewall_status:
        threats.append(firewall_status)

    # Weak passwords
    weak_passwords = check_weak_passwords()
    if weak_passwords:
        threats.append("Weak passwords detected:")
        threats.extend(weak_passwords)

    # Insecure services
    insecure_services = check_insecure_services()
    if insecure_services:
        threats.append("Insecure services detected:")
        threats.extend(insecure_services)

    return threats


if _name_ == "_main_":
    # Define the subnet (e.g., "192.168.1.0/24")
    subnet = input("Enter the subnet to scan (e.g., 192.168.1.0/24): ")

    # Scan the subnet
    devices = scan_subnet(subnet)
    print("\nDevices detected on the network:")
    for device in devices:
        print(f"IP: {device['ip']}, MAC: {device['mac']}")

    # Detect threats on the system
    print("\nAnalyzing threats on the system...")
    threats = detect_threats()
    print("\nPotential threats detected:")
    for threat in threats:
        print(f"- {threat}")