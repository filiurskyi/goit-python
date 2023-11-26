import mimetypes
import threading
import urllib.parse
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

if __name__ == "__main__":
    web_serv = threading.Thread(target=run)
    web_serv.start()
