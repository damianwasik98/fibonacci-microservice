'''
Fibonacci Generator CLI Interface
'''
import os
from argparse import ArgumentParser

from dotenv import load_dotenv

from fibonacci import Fibonacci, EndlessFibonacci, fibonacci_strategy
from rabbitmq import FibonacciProducer

strategy_mapping = {
    'recursive': fibonacci_strategy.FibonacciRecursive(),
    'iterative': fibonacci_strategy.FibonacciIterative()
}

arg_parser = ArgumentParser('Fibonacci sequence generator')
arg_parser.add_argument('-n', type=int)
arg_parser.add_argument('-d', '--delay', default=1, type=float)
arg_parser.add_argument('-s', '--strategy', default='recursive', choices=strategy_mapping.keys())
arg_parser.add_argument('-env', '--env-file')
cli_args = arg_parser.parse_args()

if cli_args.env_file:
    load_dotenv(cli_args.env_file)

with FibonacciProducer(
    host=os.environ.get('RABBITMQ_HOST', 'localhost'),
    port=os.environ.get('RABBITMQ_PORT', 5672),
    username=os.environ.get('RABBITMQ_USER', 'guest'),
    password=os.environ.get('RABBITMQ_PASS', 'guest')
) as producer:

    if cli_args.n is None:
        fibonacci = EndlessFibonacci(strategy=strategy_mapping[cli_args.strategy])
    else:
        fibonacci = Fibonacci(n=cli_args.n, strategy=strategy_mapping[cli_args.strategy])

    print(f'Starting {fibonacci} with strategy: {strategy_mapping[cli_args.strategy]}')
    for result in fibonacci.sequence_generator(delay=cli_args.delay):
        print(result)
        producer.publish_fib_number_to_queue(
            queue=os.environ.get('RABBITMQ_QUEUE', 'fibonacci'),
            number=result[0],
            fibonacci_number=result[1]
        )