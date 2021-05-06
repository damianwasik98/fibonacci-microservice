# generator

### Configuration

You must create `.env` file in this directory and fill in with your custom variables or copy from `.env.example`

Variables explanation:
- `RABBITMQ_HOST` - RabbitMQ instance host to connect with
- `RABBITMQ_PORT` - RabbitMQ instance port to connect with
- `RABBITMQ_USER` - RabbitMQ instance username to connect with
- `RABBITMQ_PASS` - RabbitMQ instance password to connect with
- `RABBITMQ_QUEUE` - RabbitMQ queue name where fib numbers will be produced

### Script description

Script produces next numbers of Fibonacci's sequence and produces to RabbitMQ queue. It uses strategy pattern, you can choose to calculate recursively or iteratively. 
It has CLI interface, so it is configurable during run.
How to run the script you can see in Dockerfile.

```
❯ python generator.py -h                            
usage: Fibonacci sequence generator [-h] [-n N] [-d DELAY] [-s {recursive,iterative}] [-env ENV_FILE]

optional arguments:
  -h, --help            show this help message and exit
  -n N                  Generate sequence and finish on this number. If None, endless generation
  -d DELAY, --delay DELAY
                        Predefined delay between generated numbers
  -s {recursive,iterative}, --strategy {recursive,iterative}
                        Strategy used to calculate fib numbers
  -env ENV_FILE, --env-file ENV_FILE
                        env file name with rabbitmq connection params, if not provided script tries to connect to localhost rabbitmq with default settings
```

### Tests

To run tests, type from this directory
```
python -m pytest tests
```
