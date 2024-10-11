# OpenVPN-ProtonVPN CLI Script
##### You can refer to ProtonVPN official documentation: https://protonvpn.com/support/linux-openvpn/

## Clone the Repoistory
```
git clone https://github.com/HeyItsSamir/linux-cli-community.git
```
##### This will take you inside protonvpn_cli DIR. This DIR holds the setup_vpn.py
```
cd linux-cli-community/protonvpn_cli
```

## Dependencies
### Installing Dependcies
##### You can refer to ProtonVPN official documentation: https://protonvpn.com/support/linux-openvpn/#cli
##### You will need your OpenVPN credentials which are found in account.protonvpn.com, go to Account → OpenVPN / IKEv2 username to view your OpenVPN username and password. Note that these are not your regular Proton Account username and password

For the following Linux distribution(s), install the official protonvpn-cli package:

### Installing OpenVPN 

#### On Debian and Ubuntu-based distributions
```
sudo apt install openvpn
```
#### Fedora
```
sudo dnf install openvpn
```
#### Arch
```
sudo pacman -S openvpn
```

### Installing OpenResolv
##### You need openresolv (an open-source implementation of resolvconf) to properly configure DNS and prevent DNS leaks.
##### Some distributions may or may not use openresolv for DNS resolution.

#### On Debian and Ubuntu-based distributions (Ubuntu uses systemd-resolved)
```
sudo apt install openresolv
```
#### Fedora
```
sudo dnf install openresolv
```
#### Arch
```
sudo pacman -S openresolv
```

### Download and Configure DNS Update Script
#### Bash
```
sudo wget "https://raw.githubusercontent.com/ProtonVPN/scripts/master/update-resolv-conf.sh" -O "/etc/openvpn/update-resolv-conf"
sudo chmod +x "/etc/openvpn/update-resolv-conf"
```

### Run setup_vpn.py inside linux-cli-community/protonvpn_cli
```
python3 setup_vpn.py
```
