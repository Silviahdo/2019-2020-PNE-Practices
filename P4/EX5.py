import socket
import termcolor
from pathlib import Path


IP = "127.0.0.1"
PORT = 8080


def get_resource(path):
    cod = 200

    if path == "/info/A":
        response = Path("A.html").read_text()
    elif path == "/info/C":
        response = Path("C.html").read_text()
    elif path == "/info/G":
        response = Path("G.html").read_text()
    elif path == "/info/T":
        response = Path("T.html").read_text()
    else:
        response = Path("Error.html").read_text()
        cod = 404

    return response, cod


def process_client(s):
    # -- Receive the request message
    req_raw = s.recv(2000)
    req = req_raw.decode()

    print("Message FROM CLIENT: ")

    # -- Split the request messages into lines
    lines = req.split('\n')

    # -- The request line is the first
    req_line = lines[0]

    print("Request line: ", end="")
    termcolor.cprint(req_line, "green")

    # -- Process the request line
    words = req_line.split(' ')

    method = words[0]
    path = words[1]

    print(f"Method: {method}")
    print(f"Path: {path}")

    resp_body = ""

    # -- Error code
    code = 0

    if method == "GET":
        resp_body, code = get_resource(path)

    if code == 200:
        status_str = "OK"
    else:
        status_str = "Not Found"

    # -- Status line: We respond that everything is ok (200 code)
    status_line = f"HTTP/1.1 {code} {status_str}\n"

    # -- Add the Content-Type header
    header = "Content-Type: text/html\n"

    # -- Add the Content-Length
    header += f"Content-Length: {len(resp_body)}\n"

    # -- Build the message by joining together all the parts
    response_msg = status_line + header + "\r\n" + resp_body
    cs.send(response_msg.encode())


ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()

print("SEQ Server configured!")

# -- Main program
while True:
    print("Waiting for clients....")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server Stopped!")
        ls.close()
        exit()
    else:
        process_client(cs)
        cs.close()
