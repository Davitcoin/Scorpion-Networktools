# Port Scanner and SSH Connector

This Python script provides a menu-driven interface for performing the following actions:

1. **Port Scanning**: Scans a target IP address for open ports within a specified range.

2. **IP Information**: Displays the local and public IP addresses of the computer.

3. **SSH Connection**: Allows the user to establish an SSH connection to a remote host by providing the necessary credentials.

4. **Exit**: Exits the program.

## Requirements
- Python 3.7 or higher
- Paramiko library (for SSH connectivity)
  - You can install it using: `pip install paramiko`

## Usage

1. Run the script using Python: `python scorpion.py (don´t forget to allow execution with chmod +x scorpion.py) `

2. The program will display a menu with the following options:

   - `Port Scanner`: Enter `1` to perform a port scan. You will be prompted to provide the target IP address. The script will scan for open ports within the range of 1 to 65535 and display the results.

   - `IP Information`: Enter `2` to display the local and public IP addresses of the computer.

   - `SSH Connection`: Enter `3` to initiate an SSH connection. You will be asked to provide the SSH host address, port (default is 22), SSH username, and SSH password. The script will attempt to connect to the remote host and print a success message if the connection is established, or an error message if there are connection issues.

   - `Exit`: Enter `4` to exit the program.

3. Follow the on-screen instructions for each option.

## Credits

This script was created by Davitcoin.


