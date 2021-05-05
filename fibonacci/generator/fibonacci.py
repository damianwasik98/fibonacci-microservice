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
        :yield: tuple with number from fibonacci number has been generated and fibonacci result
        :rtype: tuple
        '''
        for n in range(self.n + 1):
            yield (n, self.strategy.fibonacci_result(n))
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
        :yield: tuple with number from fibonacci number has been generated and fibonacci result
        :rtype: tuple
        '''
        n = 0
        while True:
            result = self.strategy.fibonacci_result(n)
            n_from = n
            n += 1
            yield  (n_from, result)
            time.sleep(delay)
