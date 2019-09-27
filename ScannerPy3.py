### scanner.py

#!/bin/python3

import sys # allows us to enter command line argumants, among other thing
import socket 
from datetime from datatime 

#Define our target
python3 scanner.py 
if len(sys.argv) == 2:
    target = socket.gethostname(sys.argv[1]) # Translate a host name to IPV4
else: 
    print("Invalid amount of argumants.")
	print("Syntax: python3 scanner <ip>")
	sys.exit()

#Add a prytty banner
print("-" * 50)
print("Scanning target" + traget)
print("Time started: " + str(datetime.now()))
print("-" * 50)

try:
    for port in range(50,85):
	    s = socket.socket(socket.AF_INT, socket.SOCK_STREAM)
		socket.setdefulttimeout(1) # is a float
		result = s.connect_ex((target.port)) # returns error indicator
		print("Checking port {}".format(port))
		if result == 0:
		    print("Port {} is open".format(port))
		s.close()
		
		
except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()
	
except socket.gaierror:
    print("Hostname could not be resolved.")
	sys.exit()

except socket.error:
    print("Couldn't connect to server.")
	sys.exit()
	
