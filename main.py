import csv
import time

def load_devices(file_name):
    devices = []
    with open(file_name, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            devices.append(row)
    return devices


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

    devices = load_devices("devices.csv")

    for device in devices:
        check_device(device)

    print("\nAll devices checked.")


if __name__ == "__main__":
    main()
