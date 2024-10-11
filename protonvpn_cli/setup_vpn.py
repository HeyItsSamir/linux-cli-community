import os
import random
import glob
import time
import base64

# Function to get user credentials
def get_credentials():
    username = input("Enter your IKE username: ")
    password = input("Enter your IKE password: ")
    encoded_credentials = base64.b64encode(f"{username}\n{password}".encode()).decode()
    with open("credentials.txt", "w") as cred_file:
        cred_file.write(encoded_credentials)
    os.chmod("credentials.txt", 0o600)  # Secure the file
    print("Credentials saved!")

# Function to load credentials
def load_credentials():
    with open("credentials.txt", "r") as cred_file:
        encoded_credentials = cred_file.read()
        decoded_credentials = base64.b64decode(encoded_credentials).decode()
        username, password = decoded_credentials.split('\n')
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

# Function to try connecting to the VPN
def try_vpn_connection(vpn_file, credentials_file, protocol, max_retries=5):
    for attempt in range(max_retries):
        exit_code = os.system(f"sudo openvpn --config {vpn_file} --auth-user-pass {credentials_file} --proto {protocol}")
        if exit_code == 0:
            print("Connected successfully!")
            return True
        else:
            print(f"Connection attempt {attempt + 1} failed. Retrying...")
            time.sleep(10)  # Wait before retrying (time in seconds)
    print("Failed to connect after multiple attempts.")
    return False

# Main function to setup the VPN connection
def setup_vpn():
    if not os.path.exists("credentials.txt"):
        get_credentials()

    username, password = load_credentials()
    region = get_region()

    home_directory = os.path.expanduser("~")  # Define home_directory
    vpn_paths = {
        "Japan": f"{home_directory}/linux-cli-community/protonvpn_cli/Regions/Japan/*.ovpn",
        "Netherlands": f"{home_directory}/linux-cli-community/protonvpn_cli/Regions/Netherlands/*.ovpn",
        "USA": f"{home_directory}/linux-cli-community/protonvpn_cli/Regions/USA/*.ovpn"
    }

    vpn_files = glob.glob(vpn_paths[region])
    random.shuffle(vpn_files)  # Shuffle the list to ensure randomness

    # Decode and save credentials to a temporary file
    with open("temp_credentials.txt", "w") as temp_cred_file:
        temp_cred_file.write(f"{username}\n{password}")
    os.chmod("temp_credentials.txt", 0o600)  # Secure the file

    for vpn_file in vpn_files:
        if try_vpn_connection(vpn_file, "temp_credentials.txt", "udp"):
            os.remove("temp_credentials.txt")  # Clean up the temporary file
            return
    os.remove("temp_credentials.txt")  # Clean up the temporary file
    print(f"Could not connect to any {region} UDP servers.")

if __name__ == "__main__":
    setup_vpn()
