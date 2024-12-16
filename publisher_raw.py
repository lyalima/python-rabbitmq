import pika


connection_parameters = pika.ConnectionParameters(
    host="localhost",
    port=5672,
    credentials=pika.PlainCredentials(
        username="guest",
        password="guest"
    )
)

channel = pika.BlockingConnection(connection_parameters).channel()
channel.basic_publish(
    exchange="data_exchange",
    routing_key="",
    body="enviando uma mensagem para a fila",
    properties=pika.BasicProperties(
        # modo de entrega com persistência dos dados
        delivery_mode=2
    )
)