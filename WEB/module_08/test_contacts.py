from datetime import datetime
from pprint import pprint
from random import choice, randint

from connect import client
from faker import Faker

db = client.book  # book is a database


def add_person(person_number) -> None:
    fake = Faker()
    for _ in range(person_number):
        name = fake.first_name()
        age = randint(18, 60)
        data = {
            "address": fake.address(),
            "age": age,
            "created_at": datetime.now(),
            "gender": choice(["male", "female"]),
            "modified_at": datetime.now(),
            "name": name,
        }
        client.book.persons.insert_one(
            data
        )  # "persons" is a collection in "book" database
        print(f"adding person: {name=}, {age=}")


def show_persons() -> None:
    for item in db.persons.find():
        pprint(item)


def delete_all() -> None:
    for item in db.persons.find():
        db.persons.delete_one(item)
    print("all deleted")


if __name__ == "__main__":
    add_person(5)
    show_persons()
    # delete_all()
