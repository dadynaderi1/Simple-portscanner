import socket
target = input("Please enter the host: ")
print("-"*60)
print ("Scanning started , Please wait...")
print("-"*60)
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostbyname((target))
def scan(port):
	try:
		s.connect((ip, port))
		return True
	except:
		return False
for port  in range (1,81):
	if scan(port):
		print ("Port %s is open !!!"%(port))
	else :
		print ("Port %s is close"%(port))
	