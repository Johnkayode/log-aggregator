#!/bin/bash

KAFKA_TOPIC="logs"

KAFKA_BROKER="kafka:9092"

# Function to check if a Kafka topic exists using Python
function check_kafka_topic() {
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

function check_elasticsearch_availability() {
    elasticsearch_host="elasticsearch" 
    elasticsearch_port=9200  

    curl --head --silent "$elasticsearch_host:$elasticsearch_port" > /dev/null
    return $?
}

function wait_for_elasticsearch() {
    retries=0
    while [ $retries -lt 5 ]; do
        if check_elasticsearch_availability; then
            echo "Elasticsearch container running."
            return 0
        else
            echo "Elasticsearch container is not yet available. Retrying in 10 seconds..."
            sleep 10
            retries=$((retries + 1))
        fi
    done

    echo "Maximum retry attempts reached. Exiting..."
    exit 1
}



while ! check_kafka_topic; do
    echo "Waiting for Kafka topic '$KAFKA_TOPIC' to be created..."
    sleep 5 
done

wait_for_elasticsearch
# wait 10s for logstash to connect to elasticsearch
sleep 10
echo "Starting the application."
python -u app.py