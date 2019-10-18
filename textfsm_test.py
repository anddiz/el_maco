
### https://github.com/networktocode/ntc-templates/tree/master/templates
### https://github.com/networktocode/
### netmiko is going to seach after net-templates in your home directory, use git to download ...
### export NET_TEXTFSM=~/net-templates_foo2/templates/
### textfsm_test.py
### 


from netmiko import Netmiko
from getpass import getpass
 
my_device = {
    'host': '1.1.1.1'
	'ussername': 'password'
	'password': getpass()
	'device_type': 'cisco_iso'
}
