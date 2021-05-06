# ingest

### Configuration

You must create `.env` file in this directory and fill in with your custom variables or copy from `.env.example`

Variables explanation:
- `RABBITMQ_HOST` = RabbitMQ instance host to connect with
- `RABBITMQ_PORT` = RabbitMQ instance port to connect with
- `RABBITMQ_USER` = RabbitMQ instance username
- `RABBITMQ_PASS` = RabbitMQ instance password
- `RABBITMQ_QUEUE` = RabbitMQ queue to get fibonacci numbers from
- `POSTGRES_HOST` = PostgreSQL instance host to connect with
- `POSTGRES_PORT` = PostgreSQL instance port to connect with
- `POSTGRES_DB` = PostgreSQL database name
- `POSTGRES_USER` = PostgreSQL database username
- `POSTGRES_PASS` = PostgreSQL database passwor

### Script description

Script consumes Fibonacci's sequence numbers from RabbitMQ and saves into PostgreSQL database.
How to run the script you can see in Dockerfile.
