import socket

# Configure the Server's IP and PORT
PORT = 8080
IP = "192.168.1.45"

# -- Step 1: create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# -- Optional: This is for avoiding the problem of Port already in use
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
s.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
s.listen()

print("The server is configured!")

while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")

    # The accept() method returns a pair of values:
    # the new socket used for communicating with the client
    # and the client's ip and port values

    try:
        # We use the rcv() method of the cs socket for receiving
        # the client's message and printing it on the console

        (cs, client_ip_port) = s.accept()

    except KeyboardInterrupt:
        print("Server stopped by the user")

        # -- Close the listenning socket
        s.close()

        exit()
    else:
        print("A client has connected to the server!")

        # Read the message from the client
        # The received message is in raw bytes
        msg_raw = cs.recv(2048)

        # We decode it for converting it
        # into a human-redeable string
        msg = msg_raw.decode()

        # Print the received message
        print("Received Message: ",  msg)

        # Send a response message to the client
        response = "HI!. I am the Happy Server :)\n"

        # The message has to be encoded into bytes
        cs.send(response.encode())

        # Close the client socket
        cs.close()