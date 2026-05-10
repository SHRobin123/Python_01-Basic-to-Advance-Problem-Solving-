#Chat Application Client

import socket

# create socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to server
client.connect(("localhost", 5000))

# send message
client.send("Hello Server".encode())

# receive reply
reply = client.recv(1024).decode()

print("Server says:", reply)

# close connection
client.close()

'''
output:-

Server says: Hello from server
'''