import os
import pika
import sys
import json
import logging

from id_creator import create_id


def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host="rabbitmq_local")
    )
    channel = connection.channel()
    channel.queue_declare(queue="create id")

    def callback(ch, method, properties, body):
        queue_message = json.loads(body.decode("UTF-8"))
        create_id(queue_message)

    channel.basic_consume(
        queue="create id",
        on_message_callback=callback,
        auto_ack=True,
    )
    logging.info(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
