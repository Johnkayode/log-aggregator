import json
import logging
import time
from uuid import uuid4
from random import randint
from kafka import KafkaProducer


kafka_topic = "logs"
kafka_producer = KafkaProducer(bootstrap_servers='kafka:9092', api_version=(0, 10, 1))

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        super(JsonFormatter, self).format(record)
        log_data = {
            'timestamp': self.formatTime(record, self.datefmt),
            'name': record.name,
            'level': record.levelname,
            'file': record.filename,
            'message': record.getMessage(),
        }
        return json.dumps(log_data)


class KafkaHandler(logging.Handler):
    def emit(self, record):
        log_message = self.format(record)
       
        kafka_producer.send(kafka_topic, value=log_message.encode('utf-8'))
        kafka_producer.flush()
        print(log_message)


kafka_handler = KafkaHandler()
kafka_handler.setLevel(logging.INFO)
formatter = JsonFormatter()
kafka_handler.setFormatter(formatter)

logger.addHandler(kafka_handler)

while True:
    randomNum = randint(0,15)
    txId = uuid4()
    if(randomNum<=4):
        logger.info(f'Application processed transaction: {txId}')
    elif (randomNum>5 and randomNum<=8):
        logger.warning(f'Transaction: {txId} is already being processed.')
    elif (randomNum>8 and randomNum<=12):
        logger.error(f'Application tried to process transaction: {txId} more than once.')
    else:
        logger.critical(f'Transaction processing service down.')
    time.sleep(120) # every 2 mins
