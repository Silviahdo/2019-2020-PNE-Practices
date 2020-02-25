import socket

# SERVER IP, PORT
# Write here the correct parameter for connecting to the
# Teacher's server
PORT = 8080
IP = "212.128.253.128"


# First, create the socket
# We will always use this parameters: AF_INET y SOCK_STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT))

# Send data. No strings can be send, only bytes
# It necesary to encode the string into bytes
s.send(str.encode("Vendo Opel Corsa"))

# -- Receive data from the server (el utf es para que el ordenador pueda reconocer caracteres especiales )
msg = s.recv(2000)
print("Message from the server: \n")
print(msg.decode("utf-8"))

# Closing the socket
s.close()
