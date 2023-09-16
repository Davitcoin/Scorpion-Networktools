import socket
import os
import sys
import requests
import paramiko  # For SSH connection


class color:
    NOTICE = '\033[33m'
    END = '\033[0m'



def print_scorpion():
    os.system("clear" if os.name == "posix" else "cls")  # Clear the screen
    scorpion = r"""
                        @@@@@@@@@@@
                       @@          @@
                          @@         @@
                             @@       @
                          @@@@ @      @    @
                         @@          @ @    @@    @
                           @@@@@@@@@@@  @@   @@   @@
                                      @@  @  @ @@ @@    @
                                        @@@  @  @ @ @   @@
                                        @ @   @@  @  @  @@
                                        @ @ @@  @@ @@@ @ @
                                          @@@ @@@      @ @
                                   @@@ @@@@@@@   @@@@@   @
                                     @@      @@@   @@@@@
        @@    @@ @@@               @@          @@@
        @ @@@  @    @@           @@@           @   @@                   Made by @Davitcoin
        @    @@@@     @           @           @     @@@       |--- https://github.com/Davitcoin ---|
         @            @        @@ @          @@     @   @@
          @@          @ @@@@@@@ @@ @@      @@      @     @@@
            @@@   @@@@@@    @@@   @@  @  @@       @@     @   @                       @@@@@
                          @@     @    @@@@       @      @    @@@                  @@@@     @
                                 @@   @ @@ @@ @@       @     @ @                @@ @   @@ @@@@
                       @@@@@@@@@@    @@  @ @  @      @@     @@ @@               @   @@   @   @@
                                @@   @@  @  @   @@@@       @   @ @@            @@    @   @    @
                             @@@@@@@  @@  @  @     @@    @@   @@   @@           @@    @@ @@@  @
                                          @  @        @@@  @@@      @ @@           @@@   @   @
                                         @ @                   @@  @    @@@             @    @
                                        @@                        @@    @   @@       @@@@  @@
                                                                     @@      @    @      @@
                                                                        @@@ @      @  @@@
                                                                             @@@@@@@@
                                                                                                         
                                                                                                    
                                                                                                    
                                                                                                                                                                                                 
 """
    print(scorpion)


#Port scanner
def get_ip_address(target):
    try:
        
        ip_address = socket.gethostbyname(target)
        return ip_address
    except socket.gaierror:
        return target

def scan_ports(target, start_port, end_port):
    open_ports = []
    
    target_ip = get_ip_address(target)  # Obtener la dirección IP
    print(target_ip)
    
    total_ports = end_port - start_port + 1
    scanned_ports = 0

    
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
        
        scanned_ports += 1
        progress = (scanned_ports / total_ports) * 100
        print(f"Looking for open ports from 1 to 65535, this might take a while: [{progress:.2f}%]", end="\r")
    
    print("\n")
    return open_ports
#My Ip
def get_local_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

def get_public_ip_address():
    try:
        response = requests.get("https://api64.ipify.org?format=json")
        data = response.json()
        public_ip = data["ip"]
        return public_ip
    except Exception as e:
        print(f"Error fetching public IP address: {e}")
    return "Not available"
#SSH
def ssh_connect():
    
    ssh_host = input("Enter SSH host address: ")
    ssh_port = int(input("Enter SSH port (default is 22): ") or 22)
    ssh_username = input("Enter SSH username: ")
    ssh_password = input("Enter SSH password: ")
    try:
        #SSHClient instance
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        #Connect to the SSH host
        ssh_client.connect(ssh_host, port=ssh_port, username=ssh_username, password=ssh_password)

        #connection info
        print(f"SSH connection successful to {ssh_host}:{ssh_port} as {ssh_username}")

        #Close SSH connection
        ssh_client.close()
    except Exception as e:
        print(f"Error connecting to SSH: {e}")


#Menu
def main_menu():
    while True:
        print_scorpion()
        print("Menu")
        print("1. Ip/url port scanner")
        print("2. My IP (Local and Public)")
        print("3. SSH Connection")
        #print("4. Devices") Pendiente
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            target_ip = input("Type IP or Website (www.123.com) to scan: ")
            start_port = 1  
            end_port = 65535 
            open_ports = scan_ports(target_ip, start_port, end_port)
            if open_ports:
                print("Open ports:")
                for port in open_ports:
                    print(f"Port {port} is open")
            else:
                print("No open ports found in this range.")
        
        elif choice == "2":
            local_ip = get_local_ip_address()
            public_ip = get_public_ip_address()
            print(f"Your computer's local IP address is: {local_ip}")
            print(f"Your public IP address is: {public_ip}")
            input("Press Enter to return to the menu...")

        elif choice == "3":
            ssh_connect()
        
        #--*elif choice == "4":
             

        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please select a valid option.")

if __name__ == "__main__":
    main_menu()
