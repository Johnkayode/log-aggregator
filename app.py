import logging
import time
from uuid import uuid4
from kafka import KafkaProducer


kafka_topic = "logs"
kafka_producer = KafkaProducer(bootstrap_servers='kafka:9092', api_version=(0, 10, 1))

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class KafkaHandler(logging.Handler):
    def emit(self, record):
        log_message = self.format(record)
       
        kafka_producer.send(kafka_topic, value=log_message.encode('utf-8'))
        kafka_producer.flush()
        print(log_message)


kafka_handler = KafkaHandler()
kafka_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
kafka_handler.setFormatter(formatter)

logger.addHandler(kafka_handler)

while True:
    txId = uuid4()
    logger.info(f'Application processed transaction: {txId}')
    time.sleep(120) # every 2 mins
