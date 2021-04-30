### Description

Make an attempt to create a tiny microservice setup generating numbers of Fibonacci sequence.
This setup has to consist of 3 services:

1. **Generator** - responsible for generating Fibonacci numbers with a predefined delay and pushing these onto rabbitmq queue

2. **Ingest** - which will consume numbers and store them in the relational db of your choice

3. **Api** - RestAPI, which will return numbers of that sequence

All of the services and databases should be configured and linked via docker-compose.yaml file.
### Must have:

Use of asyncio
Typings

### Nice to have:

Unit tests

Please provide a README file describing how to run the services and other caveats.

#### Tech stack:
- Python 3.7
- RabbitMQ
- Docker, Docker-compose
- Relational db (postgresql, mysql, sqlite, whateves)
