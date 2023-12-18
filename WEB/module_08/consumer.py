import sys
from time import sleep

import pika
from bson import ObjectId

from model_contact import Contact


def contact_name_query(contact_id: ObjectId) -> str:
    contact = Contact.objects(id=contact_id).first()
    return contact.fullname


def update_sent_flag(contact_id: ObjectId) -> None:
    Contact.objects(id=contact_id).update(sent_flag=True)


def simulate_send_email(recipient: ObjectId) -> bool:
    sleep(1)
    recipient_name = contact_name_query(ObjectId(recipient))
    update_sent_flag(ObjectId(recipient))
    print(f"Message sent to {recipient_name} with id={ObjectId(recipient)}")
    return True


def main():
    credentials = pika.PlainCredentials("guest", "guest")
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host="localhost", port=5672, credentials=credentials)
    )

    channel = connection.channel()

    channel.queue_declare(queue="queue")

    def callback(ch, method, properties, body):
        simulate_send_email(body)

    channel.basic_consume(queue="queue", on_message_callback=callback, auto_ack=True)

    print(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        sys.exit(0)
