# Import HTTP server components from Python's standard library.
from http.server import BaseHTTPRequestHandler, HTTPServer

# Define a request handler for incoming HTTP requests.
class Handler(BaseHTTPRequestHandler):

    # This method handles HTTP GET requests.
    def do_GET(self):

        # Return HTTP status code 200 (OK).
        self.send_response(200)

        # Specify that the response contains UTF-8 plain text.
        self.send_header("Content-Type", "text/plain; charset=utf-8")

        # Finish the HTTP response headers.
        self.end_headers()

        # Send the response body to the client.
        self.wfile.write(b"Docker Foundations lab\n")

# Start the HTTP server on port 8000.
HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
