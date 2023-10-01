#!/bin/bash

# Function to check if the Kafka topic exists
topic_exists() {
    kafka-topics --zookeeper zookeeper:2181 --list | grep -q "logs"
}

# Wait for the Kafka topic to exist (retry every second)
while ! topic_exists; do
    echo "Waiting for Kafka topic 'logs' to be created..."
    sleep 1
done

# Start the Kafka producer
python -u app.py