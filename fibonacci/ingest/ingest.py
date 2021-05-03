import datetime

from models import Session, Fibonacci, FibonacciHistory
from rabbitmq import FibonacciConsumer

consumer = FibonacciConsumer(
        host='localhost',
        port='5672',
        username='fibonacci',
        password='fibonacci'
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
    consumer.consume_fibonacci_messages(queue='fibonacci', on_consume=add_fibonacci_to_db)