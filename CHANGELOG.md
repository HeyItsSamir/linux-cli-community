# ProtonVPN-CLI Changelog

## Table of Contents
- [v1.1.12](#v1112)
- [v1.1.11](#v1111)
  
## v1.1.12
- Bug-Fix: Secured Credentials.txt with base64 encoding and changed file permission to 600.
- Enahncement: Added a temp_credentials file. with decoded User/Pass for OpenVPN to authenticate to.
- Enhancement: The TEMP file automatically is removed once the VPN connection terminates.

## v1.1.11
- Enhancement: Added a setup_vpn.py script to this repoistory located in protonvpn-cli DIR.
- Bug-Fix: Added error-handling to credentials.
- Bug-Fix: Added Error Handling to choosing Region.
