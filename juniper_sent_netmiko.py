
from netmiko import Netmiko
from getpass import getpass

my_device = {
    'host': '1.1.1.1'
	'ussername': 'password'
	'password': getpass()
	'device_type': 'juniper_junos'
}

net_conn = Netmiko(**my_device)

cfg_commands = ['set system syslog achive size 120k files 3']
output = net_connect.send_config_set(cfg_commands)
print(output)

output = net_connect.commit()
print(output)

output = net_connect.exit_config_mode()
output = net_connect.send_command("show configuration")
print(output)
