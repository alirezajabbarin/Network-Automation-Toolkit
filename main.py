import time

devices = [
    {"name": "Router-1", "ip": "192.168.1.1"},
    {"name": "Switch-1", "ip": "192.168.1.2"},
    {"name": "Firewall-1", "ip": "192.168.1.3"},
]

def check_device(device):
    print(f"Connecting to {device['name']} ({device['ip']}) ...")
    time.sleep(1)

    print("Running command: show ip interface brief")
    time.sleep(1)

    print("Result:")
    print("Interface    IP Address      Status")
    print("Gig0/0       192.168.1.1     up")
    print("Gig0/1       unassigned      down")
    print("-" * 40)

def main():
    print("Network Health Check Started\n")

    for device in devices:
        check_device(device)

    print("\nAll devices checked.")

if __name__ == "__main__":
    main()
