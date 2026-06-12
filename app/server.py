"""web — hello 에 의존하는 두 번째 모듈 (cascade·backdrop 실증용 echo)."""
import json
import os
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8080


class Echo(BaseHTTPRequestHandler):
    def do_GET(self):
        body = json.dumps({
            "module": "web",
            "env": os.environ.get("BEE_ENV", "unknown"),
            "host": socket.gethostname(),
            "path": self.path,
        }).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        print(f"{self.address_string()} {fmt % args}")


if __name__ == "__main__":
    print(f"web listening :{PORT}")
    HTTPServer(("", PORT), Echo).serve_forever()
