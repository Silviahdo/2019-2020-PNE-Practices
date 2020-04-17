import socket
import termcolor
from pathlib import Path


IP = "127.0.0.1"
PORT = 8080


def get_resource(path):

    if path == "/info/A":
        response = Path("A.html").read_text()
    elif path == "/info/C":
        response = Path("C.html").read_text()
    elif path == "/info/G":
        response = Path("G.html").read_text()
    elif path == "/info/T":
        response = Path("T.html").read_text()
    else:
        response = ""

    return response


def process_client(n):
    # -- Receive the request message
    request_raw = n.recv(2000)
    request = request_raw.decode()

    print("Message FROM CLIENT: ")

    lines = request.split('\n')

    request_line = lines[0]

    print("Request line: ", end="")
    termcolor.cprint(request_line, "green")

    # -- Process the request line
    words = request_line.split(' ')

    method = words[0]
    path = words[1]

    print(f"Method: {method}")
    print(f"Path: {path}")

    response_body = ""

    if method == "GET":
        response_body = get_resource(path)

    status_line = f"HTTP/1.1 200 OK\n"

    # -- Add the Content-Type header
    header = "Content-Type: text/html\n"

    # -- Add the Content-Length
    header += f"Content-Length: {len(response_body)}\n"

    # -- Build the message by joining together all the parts
    response_message = status_line + header + "\r\n" + response_body
    client_socket.send(response_message.encode())


ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))


ls.listen()

print("SEQ Server configured!")

# -- Main program
while True:
    print("Waiting for clients....")
    try:
        (client_socket, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server Stopped!")
        ls.close()
        exit()
    else:
        process_client(client_socket)
        client_socket.close()
