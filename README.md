# fibonacci-microservice

Recruitment task. You can read description [here](https://github.com/damianwasik98/fibonacci-microservice/blob/main/docs/project_requirements.md).

## Instalation and run

### 1. Configuration

Project contains three independent services:

- generator
- ingest
- api

Each service is in seperate folder [here](https://github.com/damianwasik98/fibonacci-microservice/tree/main/fibonacci)

To connect services containers with RabbitMQ and PostgreSQL you fill in configuration in `.env` files. Each service has README how to fill in `.env` file and example file `.env.example` in its directory.
Also there is one `.env` file used in docker-compose to configure rabbitmq and postgresql (also there is `.env.example`).

So to configure it:
1. Clone the code
2. Create `.env` file in fibonacci directory and fill in with values like in [`.env.example`](https://github.com/damianwasik98/fibonacci-microservice/blob/main/fibonacci/.env.example)
3. Create `.env` file in api, generator and ingest directories and fill in with values like in `.env.example` files

### 2. Run

All services are defined in [`docker-compose.yml`](https://github.com/damianwasik98/fibonacci-microservice/blob/main/fibonacci/docker-compose.yml) file, so to run it you simply type

```
cd fibonacci
docker-compose up
```

### 3. Monitoring

After running these commands, all services should be downloaded and installed. To check if its working you can check if RabbitMQ Web GUI is alive or if api documentation is available through browser.


>**Important** ❗️ 
It will take a while untill RabbitMQ and PostgreSQL will be up and running, so at first generator, ingest and api seems to fail, but services restart because of trying to connect to not fully loaded RabbitMQ or PostgreSQL.


If your `.env` files are identical with `.env.example` files, you should access RabbitMQ and API by typing urls:
- `localhost:15672 (username: fibonacci, password: fibonacci)` - RabbitMQ Server
- `localhost:8000/docs` - Fibonacci API Swagger Docs
