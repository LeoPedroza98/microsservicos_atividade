import pika

from atividade import Atividade
from config import settings

EXCHANGE_NAME = "FTGO"

SERVICE_NAME = "atividade"

# Event Types
ATIVIDADE_CREATED = "atividadeCreated"
ATIVIDADE_SUBMITED = "atividadeSubmited"


def connect():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=settings.rabbitmq_host)
    )
    channel = connection.channel()
    channel.exchange_declare(exchange=EXCHANGE_NAME, exchange_type="topic")

    return connection, channel


CONNECTION, CHANNEL = connect()


def emit_atividade_created(atividade : Atividade):
    CHANNEL.basic_publish(
        exchange=EXCHANGE_NAME,
        routing_key=f'{SERVICE_NAME}.{ATIVIDADE_CREATED}',
        body=atividade.json()
    )


def emit_atividade_submited(atividade: Atividade):
    CHANNEL.basic_publish(
        exchange=EXCHANGE_NAME,
        routing_key=f'{SERVICE_NAME}.{ATIVIDADE_SUBMITED}',
        body=atividade.json()
    )