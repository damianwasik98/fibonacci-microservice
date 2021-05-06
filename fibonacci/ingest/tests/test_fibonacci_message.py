import pytest

from rabbitmq import FibonacciMessage

@pytest.fixture
def rabbitmq_message():
    return '{"number": 1, "fibonacci_number": 1}'

def test_convert_to_dict(rabbitmq_message):

    fibonacci_message = FibonacciMessage(rabbitmq_message)
    assert isinstance(fibonacci_message.convert_to_dict(), dict)
    assert fibonacci_message.convert_to_dict() == {"number": 1, "fibonacci_number": 1}