'''
RabbitMQ manipulation
'''
import json

import pika

class FibonacciMessage:

    def __init__(self, number: int, fibonacci_number: int):
        '''
        Creates message structure with specific format. Used in FibonacciProducer
        to send this message to queue

        :param number: number from which fibonacci number has been generated
        :type number: int
        :param fibonacci_number: fibonacci result number
        :type fibonacci_number: int
        '''
        self.number = number
        self.fibonacci_number = fibonacci_number

    def __repr__(self):
        return f'<{self.__class__.__name__}({self.number}:{self.fibonacci_number}>)'

    def to_dict(self):
        return {
            'number': self.number,
            'fibonacci_number': self.fibonacci_number
        }

    def to_json(self):
        return json.dumps(self.to_dict())

class FibonacciProducer:
    
    def __init__(self, host, port, username, password):
        '''
        Manipulates RabbitMQ instance. You can publish fibonacci
        number and result to queue. 
        
        To do it you shoul create channel, call publish_fib_number_to_queue
        and close channel

        It has a context manager, so you can use it simpler way using with keyword

        :param host: RabbitMQ instance host
        :type host: str
        :param port: RabbitMQ instance port
        :type port: int
        :param username: RabbitMQ instance username
        :type username: str
        :param password: RabbitMQ instance password
        :type password: str
        '''
        self.host = host
        self.port = port
        self.username = username
        self.password = password

        self._client = self._connect_to_rabbitmq()

    def __repr__(self):
        return f'{self.__class__.__name__} ({self._client})'

    def _connect_to_rabbitmq(self) -> pika.BlockingConnection:
        '''
        Connects to RabbitMQ instance

        :return: connection with RabbitMQ
        :rtype: pika.BlockingConnection
        '''
        credentials = pika.credentials.PlainCredentials(username=self.username, password=self.password)
        connection_params = pika.ConnectionParameters(host=self.host, port=self.port,credentials=credentials)
        return pika.BlockingConnection(parameters=connection_params)

    def create_channel(self):
        '''
        Creates channel to communicate with RabbitMQ
        '''
        self._channel = self._client.channel()
    
    def close_channel(self):
        '''
        After manipulating RabbitMQ channel should be closed
        '''
        self._channel.close()

    def __enter__(self):
        self.create_channel()
        return self
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.close_channel()

    def publish_fib_number_to_queue(self, queue: str, number: int, fibonacci_number: int):
        '''
        Publishes fibonacci number and result to queue in specific structure

        :param queue: queue name in which message will appear
        :type queue: str
        :param number: number from which fibonacci number has been generated
        :type number: int
        :param fibonacci_number: fibonacci result number
        :type fibonacci_number: int
        '''
        routing_key = 'fibonacci'
        self._channel.queue_declare(queue=queue)
        self._channel.exchange_declare(exchange=queue, durable=True)
        self._channel.queue_bind(queue=queue, exchange=queue, routing_key=routing_key)

        fibonacci_message = FibonacciMessage(number=number, fibonacci_number=fibonacci_number)

        self._channel.basic_publish(
            exchange=queue,
            routing_key=routing_key,
            body=fibonacci_message.to_json(),
            properties=pika.BasicProperties(delivery_mode=2) # make message persistent, even if server restarts
        )
