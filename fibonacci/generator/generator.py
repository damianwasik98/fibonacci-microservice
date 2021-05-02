'''
Fibonacci Generator CLI Interface
'''
from argparse import ArgumentParser

from fibonacci import Fibonacci, EndlessFibonacci, fibonacci_strategy

strategy_mapping = {
    'recursive': fibonacci_strategy.FibonacciRecursive(),
    'iterative': fibonacci_strategy.FibonacciIterative()
}

arg_parser = ArgumentParser('Fibonacci sequence generator')
arg_parser.add_argument('-n', type=int)
arg_parser.add_argument('-d', '--delay', default=1, type=float)
arg_parser.add_argument('-s', '--strategy', default='recursive', choices=strategy_mapping.keys())

cli_args = arg_parser.parse_args()

if cli_args.n is None:
    fibonacci = EndlessFibonacci(strategy=strategy_mapping[cli_args.strategy])
    print(f'Starting {fibonacci} with strategy: {strategy_mapping[cli_args.strategy]}')
    for number in fibonacci.sequence_generator(delay=cli_args.delay):
        print(number)
else:
    fibonacci = Fibonacci(n=cli_args.n, strategy=strategy_mapping[cli_args.strategy])
    print(f'Starting {fibonacci} with strategy: {strategy_mapping[cli_args.strategy]}')
    result = fibonacci.calculate()
    print(f'Result for {cli_args.n}: {result}')
    print(f'Fibonacci sequence for {cli_args.n}')
    for number in fibonacci.sequence_generator(delay=cli_args.delay):
        print(number)