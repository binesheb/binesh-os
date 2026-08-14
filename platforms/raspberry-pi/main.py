"""Minimal Raspberry Pi/Linux runtime entry point."""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os
import time

VERSION = os.getenv("BINESH_VERSION", "0.1.0-dev")
START = time.time()

class Handler(BaseHTTPRequestHandler):
    def _json(self, status: int, body: dict):
        data = json.dumps(body).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path == "/api/v1/health":
            self._json(200, {"status": "ok", "version": VERSION, "uptime_s": round(time.time()-START, 2)})
        elif self.path == "/api/v1/device":
            self._json(200, {"platform": "raspberry-pi", "version": VERSION})
        else:
            self._json(404, {"error": {"code": "NOT_FOUND", "message": "endpoint not found"}})

if __name__ == "__main__":
    host = os.getenv("BINESH_HOST", "0.0.0.0")
    port = int(os.getenv("BINESH_PORT", "8080"))
    print(f"B.I.N.E.S.H. OS {VERSION} listening on {host}:{port}")
    HTTPServer((host, port), Handler).serve_forever()
