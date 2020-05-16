import socket
import termcolor

# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# to avoid a problem when a port is using
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

IP = "127.0.0.1"
PORT = 8080

# bind the socket to the servers ip and port
s.bind((IP, PORT))

# listen
s.listen()

print("Server is configured")

while True:
    # waiting for a client
    print("Waiting for a client connection")

    try:
        (cs, client_ip_port) = s.accept()

    except KeyboardInterrupt:
        print("Server stopped by the user")

        s.close()
        exit()

    else:
        print("A client has connected to the server!")

        # Read the message in bytes
        msg_raw = cs.recv(2048)

        # decode to read it properly
        msg = msg_raw.decode()

        # Print the received message
        print("Message received: ", end="")
        termcolor.cprint(msg, "green")

        # Send the response message to the client
        response = "ECHO: " + msg + "\n"

        # The message has to be in bytes
        cs.send(response.encode())

        cs.close()