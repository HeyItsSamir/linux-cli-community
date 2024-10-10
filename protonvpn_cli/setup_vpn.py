import os
import random
import glob
import time

# Function to get user credentials
def get_credentials():
    username = input("Enter your IKE username: ")
    password = input("Enter your IKE password: ")
    with open("credentials.txt", "w") as cred_file:
        cred_file.write(f"{username}\n{password}")
    print("Credentials saved!")

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

    choice = input("Enter your choice: ").strip().capitalize()
    for name, abbrev in regions.items():
        if choice in [name, abbrev, name.lower(), abbrev.lower()]:
            return name
    
    print("Invalid choice. Please try again.")
    return get_region()

def try_vpn_connection(vpn_file, credentials_file, protocol="udp", max_retries=3):
    for attempt in range(max_retries):
        print(f"Attempting to connect using {vpn_file}")
        exit_code = os.system(f"sudo openvpn --config {vpn_file} --auth-user-pass {credentials_file} --proto {protocol}")
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

    home_directory = os.path.expanduser("~")
    vpn_paths = {
        "Japan": f"{home_directory}/linux-cli-community/protonvpn_cli/Regions/Japan/*.ovpn",
        "Netherlands": f"{home_directory}/linux-cli-community/protonvpn_cli/Regions/Netherlands/*.ovpn",
        "USA": f"{home_directory}/linux-cli-community/protonvpn_cli/Regions/USA/*.ovpn"
    }

    vpn_files = glob.glob(vpn_paths[region])
    random.shuffle(vpn_files)  # Shuffle the list to ensure randomness

    for vpn_file in vpn_files:
        if try_vpn_connection(vpn_file, "credentials.txt"):
            return
    print(f"Could not connect to any {region} UDP servers.")

if __name__ == "__main__":
    setup_vpn()