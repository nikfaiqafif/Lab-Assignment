import socket

# Now we can create socket object
s = socket.socket()

# Lets choose one port and start listening on that port

host_name = socket.gethostname() 
IPADDRESS = socket.gethostbyname(host_name) 

PORT = 9898
print(">>>IP address of the server: ", IPADDRESS)
print(">>>Server is listening on port: ", PORT)
print("\n>Waiting for connection from a client...")

# Now we need to bind to the above port at server side
s.bind(('', PORT))

# Now we will put server into listening  mode 
s.listen(10)

# Now we do not know when client will concatct server so server should be listening contineously  
while True:
    # Now we can establish connection with clien
    conn, addr = s.accept()

    # Send a hello message to client
    msg = "\n\nHi, Client [IP address: "+ addr[0] + "], \nThank you for using our storage service. \nYour files are safe with us.\n-Server\n"    
    conn.send(msg.encode())
    
    filename = conn.recv(1024).decode("utf-8")
    file = open(filename, "wb")
    
    # Receive any data from client side
    RecvData = conn.recv(99999)
    
    while RecvData:
        file.write(RecvData)
        RecvData = conn.recv(99999)

    # Close the file opened at server side once copy is completed
    file.close()
    print("\n>File has been copied successfully \n")

    # Close connection with client
    conn.close()
    print(">Server closed the connection \n")

    # Come out from the infinite while loop as the file has been copied from client.
    break
