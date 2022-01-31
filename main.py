import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import colorsys

global port
global message

class Server(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_HEAD(self):
        self._set_headers()

    def do_GET(self):
        res = {
            "message": str(message)
        }
        self._set_headers()
        self.wfile.write(json.dumps(res).encode())


def run(port, server_class=HTTPServer, handler_class=Server):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)

    print ('Start port %d...' % port)
    httpd.serve_forever()



port = int(os.environ.get('PORT'))
message = os.environ.get('MESSAGE')


run(port)