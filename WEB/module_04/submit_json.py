import socket
import json
from time import sleep
from datetime import datetime
import urllib.parse
from pathlib import Path

HOST = "127.0.0.1"
PORT = 5000
file_location = Path("./storage")
file_path = file_location / "data.json"


def listen(host=HOST, port=PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Listening on {host}:{port}...")
        while True:
            conn, addr = s.accept()
            print(f"Connected by {addr}")
            data = conn.recv(1024)
            print(f"{data=}")
            if not data:
                conn.close()
                break
            else:
                parsed_data = urllib.parse.unquote_plus(data.decode())
                data_dict = {
                    key: value
                    for key, value in [el.split("=") for el in parsed_data.split("&")]
                }
                append_to_json(data_dict)
                print(f"Data received: {data_dict=}")
                conn.close()


def submit(data, host=HOST, port=PORT):
    with socket.socket() as s:
        while True:
            try:
                s.connect((host, port))
                s.sendall(data)
                break
            except ConnectionRefusedError:
                print("Connection refused. Retrying...")
                sleep(1)


def append_to_json(data: dict, path=file_path):
    new_data = {str(datetime.now()): data}
    if Path(path).exists():
        with open(path, "r") as f:
            exist_data = json.load(f)
        exist_data.update(new_data)
        with open(path, "w") as f:
            f.write(json.dumps(exist_data, sort_keys=True, indent=4))
    else:
        file_location.mkdir(parents=True, exist_ok=True)
        with open(path, "w") as f:
            f.write(json.dumps(new_data, sort_keys=True, indent=4))


if __name__ == "__main__":
    listen()
