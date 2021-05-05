import json

import pika

class FibonacciMessage:

    def __init__(self, message):
        self.message = message

    def convert_to_dict(self):
        return json.loads(self.message)

class FibonacciConsumer:
    
    def __init__(self, host, port, username, password):
        '''
        Manipulates RabbitMQ instance. You can consume fibonacci
        sequence from queue. 

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

    def _connect_to_rabbitmq(self):
        '''
        Connects to RabbitMQ instance

        :return: connection with RabbitMQ
        :rtype: pika.BlockingConnection
        '''
        credentials = pika.credentials.PlainCredentials(username=self.username, password=self.password)
        connection_params = pika.ConnectionParameters(host=self.host, port=self.port,credentials=credentials)
        return pika.BlockingConnection(parameters=connection_params)

    def _create_channel(self):
        '''
        Creates channel to communicate with RabbitMQ
        '''
        self._channel = self._client.channel()
    

    def consume_fibonacci_messages(self, queue: str, on_consume):
        '''
        Starts consuming messages from fibonacci queue

        :param queue: name of queue with fibonacci messages
        :type queue: str
        :param on_consume: callback function with gets fibonacci dictionary as an arg
        :type on_consume: callable
        '''
        self._create_channel()
        self._channel.queue_declare(queue=queue)
        
        def callback(ch, method, properties, body):
            fibonacci_message = FibonacciMessage(message=body)
            fibonacci_dict = fibonacci_message.convert_to_dict()
            on_consume(fibonacci_dict)
            self._channel.basic_ack(delivery_tag=method.delivery_tag)
        
        self._channel.basic_qos(prefetch_count=10)
        self._channel.basic_consume(queue=queue, on_message_callback=callback)

        self._channel.start_consuming()
