import socket
import termcolor

IP = "127.0.0.1"
PORT = 8080


def process_client(n):
    request_raw = n.recv(2000)
    request = request_raw.decode()

    print("Message from client : hello from web server 3 ")
    lines = request.split('\n')
    request_line = lines[0]

    print("Request line: ", end="")
    termcolor.cprint(request_line, "green")

    # Generate the response message
    # HTML language
    body = """
    <!DOCTYPE html>
    <html lang="en" dir="ltr">
      <head>
        <meta charset="utf-8">
        <title>Green server</title>
      </head>
      <body style="background-color: lightgreen;">
        <h1>GREEN SERVER</h1>
        <p>I am the Green Server! :-)</p>
      </body>
    </html>
    """
    # Status line
    status_line = "HTTP/1.1 200 OK\n"

    # Content-Type header
    header = "Content-Type: text/html\n"

    # Add the Content-Length
    header += "Content-Length: 5\n"

    # Build the message by joining together all the parts
    response_message = status_line + header + "\r\n" + body
    client_socket.send(response_message.encode())


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((IP, PORT))


s.listen()

print("SEQ Server configured!")


while True:
    print("Waiting for clients....")
    try:
        (client_socket, client_ip_port) = s.accept()
    except KeyboardInterrupt:
        print("Server Stopped!")
        s.close()
        exit()
    else:
        process_client(client_socket)
        client_socket.close()
