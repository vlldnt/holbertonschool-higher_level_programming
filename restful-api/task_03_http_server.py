#!/usr/bin/python3
'''http.server module use'''


import http.server
import socketserver
import json


class Handler(http.server.BaseHTTPRequestHandler):
    '''Subclass of http.server.BaseHTTPRequestHandler'''

    def do_GET(self):
        '''DO GET method'''
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header("Content-type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Ok")

        elif self.path == "/info":
            info = {"version": "1.0",
                    "description": "A simple API built with http.server"}
            self.send_response(200)
            self.send_header("Content-type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(info).encode('utf-8'))

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


port = 8000


with socketserver.TCPServer(("", port), Handler) as httpd:
    print(f"Opening server at {port}")
    httpd.serve_forever()
