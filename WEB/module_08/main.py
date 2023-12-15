from pprint import pprint
from sys import argv
from connect import db
from pathlib import Path
import json


# db_a = client.authors
# db_q = client.quotes

help_message = """Usage:\n
name: Steven Martin      - find all quotes by author
tag:life                 - find by one tag
tags:life, live          - find by multiple tags
exit                     - exit CLI"""


def search():
    not_exit = True
    print(help_message)
    while not_exit:
        command = input(">> ").split(":")
        match command[0]:
            case "name":
                print(f"name {command=}")
            case "tag":
                print(f"tag {command=}")
            case "tags":
                print(f"tags {command=}")
            case "exit":
                print(f"exit {command=}")
                break
            case _:
                print(f"Unknown {command=}")


def load_json(filename) -> None:
    try:
        path = Path(filename)
        with open(path, "r") as f:
            text = json.loads(f.read())
            for item in text:
                db_a = db.authors
                db_a.insert_one(item)
                # print("=" * 80)
                # pprint(item)
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(e)


def main() -> None:
    arg = argv[1:]
    if len(arg) >= 1:
        match arg[0]:
            case "search":
                search()
            case "load":
                load_json("".join(arg[1:]))
            case "help":
                print(help_message)
            case _:
                print("unknown command")
                print(help_message)
    else:
        print(help_message)


if __name__ == "__main__":
    main()