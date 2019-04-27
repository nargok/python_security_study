from http.server import HTTPServer
from http.server import SimpleHTTPRequestHandler

ip = '127.0.0.1'
port = 8000

hander = SimpleHTTPRequestHandler
server = HTTPServer((ip, port), hander)

server.serve_forever()

