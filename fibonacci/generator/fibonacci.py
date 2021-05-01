'''
Calculating fibonacci numbers
'''
import time
from functools import lru_cache

LRU_CACHE_MAXSIZE = 1000

@lru_cache(maxsize=LRU_CACHE_MAXSIZE)
def fibonacci_result(n: int):
    '''
    Simple recursive function calculating fibonacci result

    :param n: fibonacci sequence term
    :type n: int
    :return: value of fibonacci sequence term
    :rtype: int
    '''
    if n <= 1:
        return n
    else:
        return fibonacci_result(n - 1) + fibonacci_result(n - 2)


class Fibonacci:

    def __init__(self, n: int):
        '''
        Object which can calculate fibonacci result for given n
        or generate a fibonacci sequence from 0 to n with delay between
        next numbers

        :param n: fibonacci sequence term
        :type n: int
        '''
        self.__n = n

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
    
    def calculate(self):
        '''Recursive function generating fibonacci result

        :return: Fibonacci result for given number
        :rtype: int
        '''
        return fibonacci_result(self.n)

    def sequence_generator(self, delay=1):
        '''
        Generates next fibonacci numbers

        :param delay: delay between yielding next numbers, defaults to 1
        :type delay: int, optional
        :yield: fibonacci sequence number
        :rtype: int
        '''
        for n in range(self.n + 1):
            yield fibonacci_result(n)
            time.sleep(delay)

class EndlessFibonacci:

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
            result = fibonacci_result(n)
            n += 1
            yield  result
            time.sleep(delay)



if __name__ == '__main__':
    '''
    CLI Interface
    '''
    from argparse import ArgumentParser

    arg_parser = ArgumentParser('Fibonacci sequence generator')
    arg_parser.add_argument('-n', type=int)
    arg_parser.add_argument('--lru-cache-maxsize', default=1000, type=int)
    arg_parser.add_argument('--delay', default=1, type=int)

    cli_args = arg_parser.parse_args()

    LRU_CACHE_MAXSIZE = cli_args.lru_cache_maxsize

    if cli_args.n is None:
        fibonacci = EndlessFibonacci()
        for number in fibonacci.sequence_generator(delay=cli_args.delay):
            print(number)
    else:
        fibonacci = Fibonacci(cli_args.n)
        result = fibonacci.calculate()
        print(f'Result for {cli_args.n}')
        print(result)
        print(f'Fibonacci sequence for {cli_args.n}')
        for number in fibonacci.sequence_generator(delay=cli_args.delay):
            print(number)