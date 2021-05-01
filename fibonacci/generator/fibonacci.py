'''
Calculating fibonacci numbers
'''
import time
import sys

import fibonacci_strategy

from config import RECURSION_LIMIT

sys.setrecursionlimit(RECURSION_LIMIT)

class Fibonacci:

    def __init__(self, n: int, strategy=fibonacci_strategy.FibonacciRecursive()):
        '''
        Object which can calculate fibonacci result for given n
        or generate a fibonacci sequence from 0 to n with delay between
        next numbers

        :param n: fibonacci sequence term
        :type n: int
        '''
        self.__n = n
        self.strategy = strategy

    @property
    def n(self):
        return self.__n

    @n.setter
    def n(self, value):
        if not isinstance(value, int):
            raise TypeError('Fibonacci number must be integer')
        elif value < 0:
            raise ValueError('Fibonacci number must be > 0')
        
        return value

    def __repr__(self):
        return f'<{self.__class__.__name__} ({self.n})>'
    
    def calculate(self):
        '''Recursive function generating fibonacci result

        :return: Fibonacci result for given number
        :rtype: int
        '''
        return self.strategy.fibonacci_result(self.n)

    def sequence_generator(self, delay=1):
        '''
        Generates next fibonacci numbers

        :param delay: delay between yielding next numbers, defaults to 1
        :type delay: int, optional
        :yield: fibonacci sequence number
        :rtype: int
        '''
        for n in range(self.n + 1):
            yield self.strategy.fibonacci_result(n)
            time.sleep(delay)

class EndlessFibonacci:

    def __init__(self, strategy=fibonacci_strategy.FibonacciRecursive()):
        self.strategy = strategy
    
    def __repr__(self):
        return f'<{self.__class__.__name__}>'

    def sequence_generator(self, delay=1):
        '''
        Generates infinite fibonacci sequence

        :param delay: [description], defaults to 1
        :type delay: int, optional
        :yield: [description]
        :rtype: [type]
        '''
        n = 0
        while True:
            result = self.strategy.fibonacci_result(n)
            n += 1
            yield  result
            time.sleep(delay)



if __name__ == '__main__':
    '''
    CLI Interface
    '''
    from argparse import ArgumentParser

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