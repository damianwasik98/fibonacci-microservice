import pytest

from fibonacci import Fibonacci, EndlessFibonacci
from fibonacci_strategy import FibonacciRecursive, FibonacciIterative

@pytest.fixture
def fibonacci_iterative():
    return Fibonacci(
        n=10,
        strategy=FibonacciIterative()
    )

@pytest.fixture
def fibonacci_recursive():
    return Fibonacci(
        n=10,
        strategy=FibonacciRecursive()
    )

def test_fibonacci(fibonacci_iterative, fibonacci_recursive):
    assert fibonacci_iterative.n == 10
    assert fibonacci_recursive.n == 10
    
    assert isinstance(fibonacci_iterative.strategy, FibonacciIterative)
    assert isinstance(fibonacci_recursive.strategy, FibonacciRecursive)

@pytest.mark.parametrize('n, should_raise, expected_exception', [
    (1, False, None),
    (-10, True, ValueError),
    ('123', True, TypeError),
    (11.33, True, TypeError),
    (True, True, TypeError),
    ((1, 2), True, TypeError),
    ([1, 2], True, TypeError)
])
def test_n(fibonacci_iterative, fibonacci_recursive, n, should_raise, expected_exception):
    if should_raise:
        with pytest.raises(expected_exception):
            fibonacci_iterative.n = n
        with pytest.raises(expected_exception):
            fibonacci_recursive.n = n
    else:
        fibonacci_iterative.n = n
        fibonacci_recursive.n = n
        assert fibonacci_iterative.n == n
        assert fibonacci_recursive.n == n


@pytest.fixture
def endless_fibonacci_iterative():
    return EndlessFibonacci(
        strategy=FibonacciIterative()
    )

@pytest.fixture
def endless_fibonacci_recursive():
    return EndlessFibonacci(
        strategy=FibonacciRecursive()
    )

def test_endless_fibonacci(endless_fibonacci_iterative, endless_fibonacci_recursive):
    assert isinstance(endless_fibonacci_iterative.strategy, FibonacciIterative)
    assert isinstance(endless_fibonacci_recursive.strategy, FibonacciRecursive)