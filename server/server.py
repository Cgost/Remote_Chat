import socket as s

serverSocket = s.socket(s.AF_INET, s.SOCK_STREAM)

serverSocket.bind((s.gethostname(), 1234, ))

serverSocket.listen(5)

while True:
    conn, addr = serverSocket.accept()
    print("connect from", addr)

    while True:
    	data = conn.recv(1024)
    	if not data:
    		break
    	print(data)
    #conn.send(data)

    conn.close()

serverSocket.close()
