import pika

from main import seed_contact


def main():
    credentials = pika.PlainCredentials("guest", "guest")
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host="localhost", port=5672, credentials=credentials)
    )
    channel = connection.channel()

    channel.queue_declare(queue="queue")

    contacts = seed_contact(int(input("Enter contacts count to seed: ")))
    for contact in contacts:
        channel.basic_publish(exchange="", routing_key="queue", body=contact.binary)
    connection.close()


if __name__ == "__main__":
    main()
