import socket as s

clientSocket = s.socket(s.AF_INET, s.SOCK_STREAM)

clientSocket.connect((s.gethostname(), 1234))

fp = open('01.txt','rb')

while True:
	data = fp.read(16)
	if not data:
		break
	clientSocket.send(data)

fp.close()
#data = clientSocket.recv(1024)
#print('receive:', data)

clientSocket.close()
