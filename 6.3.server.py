import socket
import math
import errno
import sys
from multiprocessing import Process

def process(client):
	while True:
		client.send(str.encode('..'))
		choice = client.recv(1024).decode()

		if choice == 'exp':
			no = client.recv(1024).decode()
			value = math.exp(float(no))

		elif choice == 'log':
			no = client.recv(5).decode()
			base = client.recv(4).decode()
			value = math.log(float(no),float(base))

		elif choice == 'sqrt':
			no = client.recv(1024).decode()
			value = math.sqrt(float(no))

		elif choice == 'exit':
			client.close()
			break


		client.sendall(str(value).encode())

if __name__ == '__main__':

	server = socket.socket()
	server.bind(("",8888))
	print('Waiting for connection')
	server.listen(5)
	try:
		while True:
			try:
				client,address = server.accept()
				print('Client from : ' + str(address))
				p = Process(target = process, args=(client,))
				p.start()

			except socket.error:
				print('socket error')
	except Exception as e:
		print('exception occurred')
		print(e)
		sys.exit(1)
	finally:
		server.close()
