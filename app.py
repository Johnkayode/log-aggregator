import logging
import time
from kafka import KafkaProducer


kafka_topic = "logs"
kafka_producer = KafkaProducer(bootstrap_servers='localhost:9092')

logger = logging.getLogger('__name__')
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
    logger.info('This is a log message sent to Kafka.')
    time.sleep(120)
