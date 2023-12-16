import json
from pathlib import Path
from pprint import pprint
from sys import argv

import connect
from model import Author, Quote

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


def model_mapper(data: dict) -> None:
    if data.get("fullname", None) is not None:
        # handle as importing authors
        author_mapper(data)
    elif data.get("author", None) is not None:
        # handle as importing quotes
        quote_mapper(data)
        pass
    else:
        print("not authors or quotes json...")


def author_mapper(data: dict) -> None:
    Author(
        fullname=data.get("fullname"),
        born_date=data.get("born_date"),
        born_location=data.get("born_location"),
        description=data.get("description"),
    ).save()


def quote_mapper(data: dict) -> None:
    tags = []
    author = db_authors_query(data.get("fullname"))
    for item in data.get("tags"):
        tags.append(item)
    Quote(
        author=author,
        tags=tags,
        quote=data.get("quote")
    ).save()


def db_authors_query(name):
    author = Author.objects(fullname=name).first()
    return author


def load_json(filename) -> None:
    try:
        path = Path(filename)
        with open(path, "r", encoding='utf-8') as f:
            text = json.loads(f.read())
            for item in text:
                print("adding new item ..")
                model_mapper(data=item)
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
            case "test":
                print(db_authors_query(1, 1))
            case _:
                print("unknown command")
                print(help_message)
    else:
        print(help_message)


if __name__ == "__main__":
    main()
