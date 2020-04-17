import http.server
import socketserver
import termcolor
from pathlib import Path


PORT = 8080
socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        request_line = self.requestline.split(' ')
        path = request_line[1]
        arguments = path.split('?')

        # Get the verb. It is the first argument
        verb = arguments[0]
        contents = Path('error.html').read_text()
        error_code = 404

        if verb == "/":
            # Open the form1.html file
            # Read the index from the file
            contents = Path('exercise1-form.html').read_text()
            error_code = 200

        elif verb == "/echo":
            # -- Get the argument to the right of the ? symbol
            pair = arguments[1]

            # -- Get the two elements: name and value
            name, value = pair.split("=")

            # -- Generate the html code
            contents = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="utf-8">
                <title>RESULT</title>
            </head>
            <body>
            <h2>Received message:</h2>
            """

            contents += f"<p>{value}</p>"
            contents += '<a href="/">Main page</a>'
            contents += "</body></html>"
            error_code = 200

        self.send_response(error_code)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()
        self.wfile.write(str.encode(contents))

        return


Handler = TestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
