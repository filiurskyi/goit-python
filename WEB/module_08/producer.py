import os

from faker import Faker

import connect
from connect_redis import redis_get, redis_set
from model_contact import Contact


def seed_contact(contact_number):
    fake = Faker()
    for _ in range(contact_number):
        new_contact = Contact(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            personal_email=fake.email(),
        )
        new_contact.save()


if __name__ == "__main__":
    seed_contact(int(input("Enter int number of contacts to seed: ")))

    redis_set("first_key", "super value")

    print(redis_get("first_key"))
