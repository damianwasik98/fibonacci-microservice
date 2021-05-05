import datetime
import os

from dotenv import load_dotenv

from models import Session, Fibonacci, FibonacciHistory
from rabbitmq import FibonacciConsumer

load_dotenv('.env')

consumer = FibonacciConsumer(
        host=os.environ.get('RABBITMQ_HOST', 'localhost'),
        port=os.environ.get('RABBITMQ_PORT', '5672'),
        username=os.environ.get('RABBITMQ_USER', 'fibonacci'),
        password=os.environ.get('RABBITMQ_PASS', 'fibonacci')
    )


def add_fibonacci_to_db(fibonacci_dict):

    number = str(fibonacci_dict['number'])
    fibonacci_number = str(fibonacci_dict['fibonacci_number'])

    fibonacci = Fibonacci(number=number, fibonacci_number=fibonacci_number)
    history = FibonacciHistory(date=datetime.datetime.now(), number=number)

    session.add(fibonacci)
    session.add(history)
    session.commit()

with Session() as session:
    consumer.consume_fibonacci_messages(
        queue=os.environ.get('RABBITMQ_QUEUE', 'fibonacci'),
        on_consume=add_fibonacci_to_db
    )