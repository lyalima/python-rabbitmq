# Exemplo de integração entre Python e RabbitMQ.

Para executar o RabbitMQ use: docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management.

Para instalar as dependências do código use: pip install -r requirements.txt

Para executar o publisher use: python publisher.py

Para executar o consumer use: python consumer.py
