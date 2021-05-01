from functools import lru_cache
from abc import ABC, abstractmethod

LRU_CACHE_MAXSIZE = None

class FibonacciStrategy(ABC):

    @abstractmethod
    def fibonacci_result(self):
        pass


class FibonacciRecursive(FibonacciStrategy):

    @staticmethod
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
        
        return FibonacciRecursive.fibonacci_result(n - 1) + FibonacciRecursive.fibonacci_result(n - 2)


class FibonacciIterative(FibonacciStrategy):
    pass

    @staticmethod
    @lru_cache(maxsize=LRU_CACHE_MAXSIZE)
    def fibonacci_result(n: int):
        pass