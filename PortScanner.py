import socket
import sys
target = input("Please enter the host: ")
print("-"*60)
print ("Scanning started , Please wait...")
print("-"*60)
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		 
def scan(port):
	try:
		ip = socket.gethostbyname((target))
		s.connect((ip, port))
		s.settimeout(5)
		return True
	except socket.error as err:
		print("Can't connect to host")
		sys.exit()
	except  :
		return False
		
		
for port  in range (1,81):
	if scan(port):
		print ("Port %s is open !!!"%(port))
	else :
		print ("Port %s is close"%(port))
	
