#!/usr/bin/env python
import pika, time
#docker run -d --name rabitmq -p 5672:5672 rabbitmq:3
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
counter = 0
while True:
    channel.basic_publish(exchange='',
                        routing_key='hello',
                        body= f"Message: {str(counter)}")
    print(f" [x] Sent Message: {str(counter)}")
    counter += 1
    time.sleep(0.5)
connection.close()

