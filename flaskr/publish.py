import pika
from pika.exceptions import AMQPConnectionError
import logging


def publish_text(message: str):
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host="rabbitmq_local")
        )
        channel = connection.channel()
        channel.queue_declare(queue="create id")
        channel.basic_publish(
            exchange="", routing_key="create id", body=message
        )
        connection.close()
        return True
    except AMQPConnectionError as ex:
        logging.exception(f"caught exception, error={ex}")
        raise ex

