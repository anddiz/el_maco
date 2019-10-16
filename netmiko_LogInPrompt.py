
from netmiko import Netmiko
from getpass import getpass

my_device = {
   'host': '1.1.1.1',
	 'username': 'python',
	 'password': getpass(),
	 'device_type': 'cisco_iso'
}

net_conn = Netmiko(**my_device)
				
print(net_conn.find_prompt())
