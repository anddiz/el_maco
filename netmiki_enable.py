from netmiko import Netmiko
from getpass import getpass


my_device = {
   'host': '1.1.1.1',
	 'username': 'python',
	 'password': password,
   'secret' : password,
	 'device_type': 'cisco_iso'
}



net_conn = Netmiko(**my_device)
net_conn.send_command_timing("disable")
print(net_conn.find_prompt())

net_conn.enable()
print(net_conn.find_prompt())
