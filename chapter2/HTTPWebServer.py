from http.server import *
from socketserver import *

PORT = 8000


class MainHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("cache-control", "public,  max-age=31536000")
        self.end_headers()

handler = SimpleHTTPRequestHandler
httpd = TCPServer(("", PORT), MainHandler)

print("serving", PORT)
httpd.serve_forever()