# Import necessary modules
from http.server import SimpleHTTPRequestHandler, HTTPServer

# Set up the server address
host = 'localhost'
port = 8000

# Define the handler for serving static files
class MyHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        # Set the path to the directory containing the JSON file
        self.directory = '.'
        super().__init__(*args, directory=self.directory, **kwargs)

# Start the HTTP server
if __name__ == '__main__':
    try:
        server_address = (host, port)
        httpd = HTTPServer(server_address, MyHandler)
        print(f'Starting server on {host}:{port}')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\nServer stopped.')
