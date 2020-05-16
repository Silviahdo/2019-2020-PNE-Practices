import socket
import termcolor


PORT = 8080
IP = "127.0.0.1"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Avoid the problem of Port already in use
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


s.bind((IP, PORT))


s.listen()

number_con = 0

print("The server is configured!")

while True:
    print("Waiting for Clients to connect")

    try:
        (client_socket, client_ip_port) = s.accept()
    except KeyboardInterrupt:
        print("Server stopped by the user")
        s.close()
        exit()

    else:

        # -- New client
        number_con += 1
        print("CONNECTION: ", number_con, "ClientIP, PORT: ",client_ip_port)

        message_raw = client_socket.recv(2000)
        message = message_raw.decode()

        print("Message received: ", end="")
        termcolor.cprint(message, "green")

        response = "ECHO: " + message + "\n"

        client_socket.send(response.encode())
        client_socket.close()