#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('deploy', 'admin')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', credentials))
channel = connection.channel()

channel.exchange_declare(exchange='test', exchange_type='direct')

channel.queue_declare(queue='test', arguments={'x-message-ttl' : 3600000})

channel.basic_publish(exchange='test', routing_key='test', body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()