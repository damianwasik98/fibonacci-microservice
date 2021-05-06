# fibonacci

In this directory you must create `.env` file. It contains RabbitMQ and PostgreSQL connection parameters, which will be used by other services (also in `.env` files).

This `.env` file is loaded in `docker-compose.yml`
There is `.env.example` file you can use, or define your own parameters if you want.

Explanation of variables:

- `RABBITMQ_PORT` - this will expose port of RabbitMQ instance used by generator and ingest to connect
- `RABBITMQ_USER` - this will create custom username in RabbitMQ instance
- `RABBITMQ_PASS` - this will create custom password in RabbitMQ instance
- `POSTGRES_PORT` - this will expose port of PostgreSQL db used by ingest and api
- `POSTGRES_DB` - this will create custom name of database
- `POSTGRES_USER` - this will create custom database password
- `POSTGRES_PASS` - this will create custom database password
