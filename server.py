import http.server
import socketserver
import os

PORT = 8000

handler = http.server.SimpleHTTPRequestHandler

os.chdir(r'C:\Users\donpr\Desktop\testserver\web')

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"server started, port: {PORT}")
    httpd.serve_forever()