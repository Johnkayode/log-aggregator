
from kafka import KafkaConsumer

kafka_topic = "logs"
kafka_consumer = KafkaConsumer(kafka_topic, bootstrap_servers='kafka:9092', api_version=(0, 10, 1))


for message in kafka_consumer:
    if message.value is not None:
        # Process the received message
        print(f'Received message: {message.value.decode("utf-8")}')


kafka_consumer.close()