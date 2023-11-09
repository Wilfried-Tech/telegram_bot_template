import importlib
import json
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

sys.path.insert(0, Path(__file__).parent.parent.as_posix())

main = importlib.import_module('bot.main')


class handler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode('utf-8'))

        main.start_bot(data)

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'')

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<h1>Hello, World</h1>')


if __name__ == '__main__':
    h = HTTPServer(('localhost', 1234), handler)
    try:
        print(h.server_address)
        h.serve_forever()
    except KeyboardInterrupt:
        pass
