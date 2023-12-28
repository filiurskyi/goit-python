import json
from pathlib import Path

from test_app.models import Author, Quote, Tag


def load_json_to_db(filename) -> None:
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
        new_tag = Tag(word=item)
        tags.append(new_tag)
        new_tag.save()
    if author:
        quote = Quote(author=author, quote=data.get("quote"))
        quote.save()
        quote.tags.set(tags)
        print("Quote added successfully.")
    else:
        print("Author not found.")


def db_authors_query(name: str) -> Author:
    author = Author.objects.filter(fullname=name).first()
    return author


if __name__ == '__main__':
    load_json_to_db("../authors.json")
    load_json_to_db("quotes.json.json")
