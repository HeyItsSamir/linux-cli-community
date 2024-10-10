import os
import random
import glob
import time

# Function to get user credentials
def get_credentials():
    for _ in range(3):  # Allow up to 3 attempts
        username = input("Enter your IKE username: ")
        password = input("Enter your IKE password: ")
        with open("credentials.txt", "w") as cred_file:
            cred_file.write(f"{username}\n{password}")
        
        if test_credentials():
            print("Credentials saved and verified!")
            return
        else:
            print("Invalid credentials. Please try again.")
    
    print("Failed to provide valid credentials after multiple attempts. Exiting.")
    exit()

# Function to test if the credentials are valid
def test_credentials():
    # Try a dummy connection or check to see if credentials work
    # This is a placeholder function; in a real scenario, you'd check against a known valid endpoint
    return True  # Replace with actual test

# Function to load credentials
def load_credentials():
    with open("credentials.txt", "r") as cred_file:
        lines = cred_file.readlines()
        username = lines[0].strip()
        password = lines[1].strip()
    return username, password

def get_region():
    regions = {
        "Japan": "J",
        "Netherlands": "N",
        "USA": "U"
    }
    print("Choose a region (you can type the full name or the abbreviation):")
    for name, abbrev in regions.items():
        print(f"{name} ({abbrev})")

    for _ in range(3):  # Allow up to 3 attempts
        choice = input("Enter your choice: ").strip().capitalize()
        for name, abbrev in regions.items():
            if choice in [name, abbrev, name.lower(), abbrev.lower()]:
                return name
        print("Invalid choice. Please try again.")
    
    print("Failed to provide a valid region after multiple attempts. Exiting.")
    exit()

def check_dns_manager():
    if os.system("command -v resolvconf") == 0:
        print("Using openresolv.")
        return "openresolv"
    elif os.system("command -v systemd-resolve") == 0:
        print("Using systemd-resolved.")
        return "systemd-resolved"
    else:
        print("No DNS manager found. Exiting.")
        exit()

def try_vpn_connection(vpn_file, credentials_file, dns_manager, protocol="udp", max_retries=3):
    up_script = ""
    down_script = ""
    
    if dns_manager == "openresolv":
        up_script = "--up /etc/openvpn/update-resolv-conf"
        down_script = "--down /etc/openvpn/update-resolv-conf"
    elif dns_manager == "systemd-resolved":
        up_script = "--up /etc/openvpn/update-systemd-resolved --down /etc/openvpn/update-systemd-resolved --down-pre"

    for attempt in range(max_retries):
        print(f"Attempting to connect using {vpn_file}")
        exit_code = os.system(f"sudo openvpn --config {vpn_file} --auth-user-pass {credentials_file} --proto {protocol} {up_script} {down_script}")
        if exit_code == 0:
            print("Connected successfully!")
            return True
        else:
            print(f"Connection attempt {attempt + 1} failed. Retrying...")
            time.sleep(3)  # Wait before retrying
    print("Failed to connect after multiple attempts.")
    return False

def setup_vpn():
    if not os.path.exists("credentials.txt"):
        get_credentials()

    username, password = load_credentials()
    region = get_region()
    dns_manager = check_dns_manager()

    home_directory = os.path.expanduser("~")
    vpn_paths = {
        "Japan": f"{home_directory}/linux-cli-community/protonvpn_cli/Regions/Japan/*.ovpn",
        "Netherlands": f"{home_directory}/linux-cli-community/protonvpn_cli/Regions/Netherlands/*.ovpn",
        "USA": f"{home_directory}/linux-cli-community/protonvpn_cli/Regions/USA/*.ovpn"
    }

    vpn_files = glob.glob(vpn_paths[region])
    random.shuffle(vpn_files)  # Shuffle the list to ensure randomness

    for vpn_file in vpn_files:
        if try_vpn_connection(vpn_file, "credentials.txt", dns_manager):
            return
    print(f"Could not connect to any {region} UDP servers.")

if __name__ == "__main__":
    setup_vpn()
