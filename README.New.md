<h1 align="center">ProtonVPN-CLI</h1>
<p align="center">
  <img src="resources/images/linux-cli-banner.png" alt="Logo"></img>
</p>

# ProtonVPN-OpenVPN CLI Setup Guide
##### You can refer to ProtonVPN official documentation: https://protonvpn.com/support/linux-openvpn/
##### You will need your OpenVPN credentials which are found in account.protonvpn.com, go to Account → OpenVPN / IKEv2 username to view your OpenVPN username and password. Note that these are not your regular Proton Account username and password.

## Clone the Repoistory
```
git clone https://github.com/HeyItsSamir/linux-cli-community.git
cd linux-cli-community/protonvpn_cli
```

## Installation & Updating
### Installing ProtonVPN-CLI from Distribution Repositories

For the following Linux distribution(s), install the official protonvpn-cli package:

#### On Debian and Ubuntu-based distributions
```
sudo apt install -y protonvpn-cli
```
#### Fedora
```
sudo dnf install -y protonvpn-cli
```
#### CentOS & RHEL 7.x:
```
sudo yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
sudo yum install protonvpn-cli
```
#### CentOS & RHEL 8.x:
```
sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
sudo dnf install -y protonvpn-cli
```

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
#### You need openresolv (an open-source implementation of resolvconf) to properly configure DNS and prevent DNS leaks.
#### On Debian and Ubuntu-based distributions
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
