import json
from pathlib import Path
from pprint import pprint
from sys import argv

from bson import ObjectId
from faker import Faker
from mongoengine import Q

from connect import connect
from connect_redis import redis_get, redis_set
from model import Author, Quote
from model_contact import Contact

help_message = """Usage:\n
name:Steve Martin      - find all quotes by author
tag:life                 - find by one tag
tags:life,live          - find by multiple tags
exit                     - exit CLI"""


def search():
    not_exit = True
    print(help_message)
    while not_exit:
        command = input(">> ").split(":")
        # print("----command-----", command)
        match command[0]:
            case "name":
                result = db_lookup_name(command[1])
                # print(f"name {command=}, {result=}")
                for quote in result:
                    pprint(quote)
            case "tag":
                result = db_lookup_tag(command[1])
                # print(f"name {command=}, {result=}")
                for quote in result:
                    pprint(quote)
            case "tags":
                result = db_lookup_tags(command[1].strip().split(","))
                print(f"name {command=}, {result=}")
                for quote in result:
                    pprint(quote)
            case "exit":
                print(f"exiting...")
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
    author_name = data.get("author")
    print("adding quote for author ", author_name)
    author = db_authors_query(author_name)
    for item in data.get("tags"):
        tags.append(item)
    Quote(author=author.id, tags=tags, quote=data.get("quote")).save()


def db_authors_query(name: str) -> Author:
    author = Author.objects(fullname__contains=name).first()
    return author


def db_lookup_name(name: str) -> list[Quote]:
    cached_query = redis_get(name)
    print(f"{cached_query=}")
    if cached_query is not None:
        print("getting cached")
        return cached_query
    else:
        print("getting uncached")
        author = db_authors_query(name)
        quotes = Quote.objects(author=author).all()
        result = []
        for quote in quotes:
            result.append(quote.to_mongo().to_dict())
        redis_set(name, result)
        return result


def db_lookup_tag(tag: str) -> list[Quote]:
    cached_query = redis_get(tag)
    print(f"{cached_query=}")
    if cached_query is not None:
        print("getting cached")
        return cached_query
    else:
        print("getting uncached")
        quotes = Quote.objects(tags__contains=tag)
        result = []
        for quote in quotes:
            result.append(quote.to_mongo().to_dict())
        redis_set(tag, result)
        return result


def db_lookup_tags(tags: list[str]) -> list[Quote]:
    cached_query = redis_get(",".join(tags))
    print(f"{cached_query=}")
    if cached_query is not None:
        print("getting cached")
        return cached_query
    else:
        print("getting uncached")
        queries = [Q(tags__contains=tag) for tag in tags]
        combined_query = Q()
        for q in queries:
            combined_query &= q
        quotes = Quote.objects(combined_query)

        result = []
        for quote in quotes:
            result.append(quote.to_mongo().to_dict())
        redis_set(",".join(tags), result)
        return result


def seed_contact(contacts_count) -> list[ObjectId]:
    fake = Faker()
    contacts_ids = []
    for _ in range(contacts_count):
        new_contact = Contact(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            personal_email=fake.email(),
        )
        new_contact.save()
        contacts_ids.append(new_contact.id)
        # print(f"{contacts_ids=}")
    return contacts_ids


def load_json(filename) -> None:
    try:
        path = Path(filename)
        with open(path, "r", encoding="utf-8") as f:
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
    connect
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
                print(db_authors_query("Steve Martin"))
            case "seed":
                seed_contact(int(input("Enter int number of contacts to seed: ")))
            case _:
                print("unknown command")
                print(help_message)
    else:
        print(help_message)


if __name__ == "__main__":
    main()
