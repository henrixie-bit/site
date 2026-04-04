import http.server
import socketserver
import os

os.chdir("/Users/xieziheng/Downloads/henri-site")

Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", 3456), Handler) as httpd:
    httpd.serve_forever()
