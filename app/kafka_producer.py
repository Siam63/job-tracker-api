import json
import os
from dotenv import load_dotenv
from kafka import KafkaProducer

load_dotenv()

KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
KAFKA_DOCUMENT_TOPIC = os.getenv("KAFKA_DOCUMENT_TOPIC", "document-uploaded")


def create_kafka_producer():
    return KafkaProducer(
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        value_serializer=lambda value: json.dumps(value).encode("utf-8")
    )


def publish_document_uploaded_event(event: dict):
    producer = create_kafka_producer()
    producer.send(KAFKA_DOCUMENT_TOPIC, event)
    producer.flush()
    producer.close()