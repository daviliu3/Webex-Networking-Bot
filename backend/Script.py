from netmiko import ConnectHandler
import json

class SSH_Connection():
    def __init__(self, Hostname, Type, Username='', Password=''):
        device = {
            'device_type': Type,
            'ip':   Hostname,
            'username': Username,
            'password': Password,
            'port': 5000,   # default port for Telnet
            'secret': '',  # optional, fill if needed
        }
        try:
            self.connection = ConnectHandler(**device)
            print(f"Successfully connected to {Hostname}")
        except Exception:
            print(f'Connection {Hostname} failed!')

# Create an instance of SSH_Connection
R1 = SSH_Connection('172.16.12.128', 'cisco_ios_telnet',)


