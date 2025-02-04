import pika
import json
from typing import Dict


class RabbitmqPublisher():

    def __init__(self):
        self.__host = "localhost"
        self.__port = 5672
        self.__username = "guest"
        self.__password = "guest"
        self.__exchange = "data_exchange"
        self.__routing_key = ""
        self.__channel = self.__create_channel()
    

    def __create_channel(self):
        connection_parameters = pika.ConnectionParameters(
            host=self.__host,
            port=self.__port,
            credentials=pika.PlainCredentials(
                username=self.__username,
                password=self.__password
            )
        )
        channel = pika.BlockingConnection(connection_parameters).channel()

        return channel
    

    def publish_message(self, body: Dict):
        self.__channel.basic_publish(
            exchange=self.__exchange,
            routing_key=self.__routing_key,
            body=json.dumps(body),
            properties=pika.BasicProperties(
                # modo de entrega com persistência dos dados
                delivery_mode=2
            )
        )
        

rabbitmq_publisher_obj = RabbitmqPublisher()
rabbitmq_publisher_obj.publish_message({"message": "enviando mensagem para a fila"})
