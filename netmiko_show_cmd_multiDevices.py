from netmiko import Netmiko
from getpass import getpass

### python -i netmiko_show_cmd.py
### dir(net_conn.send_command)
### dir()
###  help(net_conn.send_command)

password = getpass()

cisco = {
   'host': '1.1.1.1',
	 'username': 'python',
	 'password': password,
	 'device_type': 'cisco_iso'
}


arista = {
   'host': '1.1.1.1',
	 'username': 'python',
	 'password': password,
	 'device_type': 'cisco_iso'
}

srx1 = {
   'host': '1.1.1.1',
	 'username': 'python',
	 'password': password,
	 'device_type': 'cisco_iso'
}


for device in (cisco, arista, srx1):
net_conn = Netmiko(**device)

output = net_conn.send_command("show arp" , expect_string=r'#')
print(output)
print(net_conn.find_prompt())

output = net_conn.send.command("show ip int brief")
print(output)

print(net_conn.find_prompt())
