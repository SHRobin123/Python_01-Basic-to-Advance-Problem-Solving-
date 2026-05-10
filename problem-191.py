#Chat Application Server

import socket

# create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind host and port
server.bind(("localhost", 5000))

# listen for connection
server.listen(1)

print("Server is waiting for connection...")

# accept client
client_socket, address = server.accept()

print("Connected to:", address)

# receive message
message = client_socket.recv(1024).decode()

print("Client says:", message)

# send reply
client_socket.send("Hello from server".encode())

# close connection
client_socket.close()

'''
output:-

Server is waiting for connection...

Connected to: ('127.0.0.1', 50000)

Client says: Hello Server
'''