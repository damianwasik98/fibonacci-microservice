from functools import lru_cache
from abc import ABC, abstractmethod

from config import LRU_CACHE_MAXSIZE

class FibonacciStrategy(ABC):

    def __repr__(self):
        return f'<{self.__class__.__name__}>'

    @abstractmethod
    def fibonacci_result(self):
        pass


class FibonacciRecursive(FibonacciStrategy):

    @staticmethod
    @lru_cache(maxsize=LRU_CACHE_MAXSIZE)
    def fibonacci_result(n: int) -> int:
        '''
        Simple recursive function calculating fibonacci result

        :param n: fibonacci sequence term
        :type n: int
        :return: value of fibonacci sequence term
        :rtype: int
        '''
        if n <= 1:
            return n
        
        return FibonacciRecursive.fibonacci_result(n - 1) + FibonacciRecursive.fibonacci_result(n - 2)


class FibonacciIterative(FibonacciStrategy):

    @staticmethod
    @lru_cache(maxsize=LRU_CACHE_MAXSIZE)
    def fibonacci_result(n: int) -> int:
        '''
        Simple iterative function calculating fibonacci result

        :param n: fibonacci sequence term
        :type n: int
        :return: value of fibonacci sequence term
        :rtype: int
        '''
        if n <= 1:
            return n

        two_before = 0
        one_before = 1
        fib_number = two_before + one_before

        i = 2
        while i < n:
            two_before = one_before
            one_before = fib_number
            fib_number = two_before + one_before
            
            i += 1
        return fib_number