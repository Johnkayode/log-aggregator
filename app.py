import logging
import time


logger = logging.getLogger('my_logger')


while True:
    logger.info('This is a log message sent to Kafka.')
    time.sleep(120)