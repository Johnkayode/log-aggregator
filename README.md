# log-aggregator
Log aggregation pipeline with Kafka and ELK stack

## Data Pipeline Architecture
![Data pipeline](https://github.com/Johnkayode/log-aggregator/blob/main/docs/architecture.png)

## Kibana Dashboard
Log data visualization.
![Kibana dashboard](https://github.com/Johnkayode/log-aggregator/blob/main/docs/kibana.png)

## Run Project
- Run `docker run --build` to build and run the containers
- Open `localhost:5601` to view the Kibana dashboard
- Create data views for the logs.

Note: You might need to increase your Docker memory allocation to 4GB to run all containers efficiently.
