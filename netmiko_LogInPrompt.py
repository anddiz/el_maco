
from netmiko import Netmiko
from getpass import getpass


### To see all devices, change device_type to a non existing device name, like "foo". 
### You will get a list with all devices as result.
my_device = {
   'host': '1.1.1.1',
	 'username': 'python',
	 'password': getpass(),
	 'device_type': 'cisco_iso'
}

net_conn = Netmiko(**my_device)
				
print(net_conn.find_prompt())
