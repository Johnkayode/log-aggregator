#!/bin/bash

KAFKA_TOPIC="logs"

KAFKA_BROKER="kafka:9092"

# Function to check if a Kafka topic exists using Python
check_kafka_topic() {
    python - <<EOF
from kafka.admin import KafkaAdminClient

def topic_exists(broker, topic):
    admin_client = KafkaAdminClient(bootstrap_servers=broker)
    return topic in admin_client.list_topics()

if topic_exists("$KAFKA_BROKER", "$KAFKA_TOPIC"):
    exit(0)
else:
    exit(1)
EOF
}

if check_kafka_topic; then
    echo "Starting the application."
    python -u app.py
else
    echo "Waiting for Kafka topic '$KAFKA_TOPIC'."
fi