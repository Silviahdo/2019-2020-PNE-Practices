import socket

# SERVER IP, PORT
PORT = 8080
IP = "192.168.124.179"  #my ip

while True:
  # -- Ask the user for the message
    m=input("Enter the message: ")
  # -- Create the socket
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  # -- Establish the connection to the Server
    s.connect((IP, PORT))
  # -- Send the user message
    s.send(str.encode(m))
  # -- Close the socket
    s.close()