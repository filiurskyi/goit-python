from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import threading
import mimetypes
from pathlib import Path
import submit_json


class HttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        pr_url = urllib.parse.urlparse(self.path)
        match pr_url.path:
            case "/":
                self.send_html_file("index.html")
            case "/message":
                self.send_html_file("message.html")
            case _:
                file = pr_url.path[1:]
                if Path(file).exists():
                    self.send_static()
                else:
                    self.send_html_file("error.html", 404)

    def do_POST(self):
        data = self.rfile.read(int(self.headers["Content-Length"]))
        submit_json.submit(data)
        self.send_response(302)
        self.send_header("Location", "/")
        self.end_headers()

    def send_html_file(self, filename, status=200):
        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open(filename, "rb") as file:
            self.wfile.write(file.read())

    def send_static(self):
        self.send_response(200)
        mt = mimetypes.guess_type(self.path)
        if mt:
            self.send_header("Content-type", mt[0])
        else:
            self.send_header("Content-type", "text/plain")
        self.end_headers()
        with open(f".{self.path}", "rb") as file:
            self.wfile.write(file.read())


def run(server_class=HTTPServer, handler_class=HttpHandler):
    server_address = ("", 3000)
    http = server_class(server_address, handler_class)
    try:
        http.serve_forever()
    except KeyboardInterrupt:
        http.server_close()


if __name__ == "__main__":
    sock_serv = threading.Thread(target=submit_json.listen)
    web_serv = threading.Thread(target=run)
    web_serv.start()
    sock_serv.start()
