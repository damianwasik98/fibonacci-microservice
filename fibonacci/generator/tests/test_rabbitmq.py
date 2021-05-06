import pytest

from rabbitmq import FibonacciMessage


@pytest.fixture
def fibonacci_message():
    message = {
        'number': 0,
        'fibonacci_number': 0
    }

    return FibonacciMessage(**message)

def test_init(fibonacci_message):
    assert fibonacci_message.number == 0
    assert fibonacci_message.fibonacci_number == 0

def test_to_dict(fibonacci_message):
    assert fibonacci_message.to_dict() == {
        'number': 0,
        'fibonacci_number': 0
    }

def test_to_json(fibonacci_message):
    assert fibonacci_message.to_json() == '{"number": 0, "fibonacci_number": 0}'