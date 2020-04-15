import socket
import termcolor

# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# to avoid a problem when a port is using
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

IP = "192.168.1.45"
PORT = 8080

number_connect = 0
connections_list = []
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
        number_connect += 1
        print("A client has connected to the server!")
        connections_list.append(client_ip_port)
        print("CONNECTION ",  number_connect, ". Client IP,PORT: ", client_ip_port)
        # Read the message in bytes
        msg_raw = cs.recv(2048)

        # decode to read it properly
        msg = msg_raw.decode()

        # Print the received message
        print("Message received: ", end="")
        termcolor.cprint(msg, "yellow")

        # Send the response message to the client
        response = "ECHO: " + msg + "\n"

        # The message has to be in bytes
        cs.send(response.encode())

        print("The following clients has connected to the server: ")
        for i, c in enumerate(connections_list):
            print("Client",  i, ":", c)

        cs.close()