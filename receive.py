import pika
import logging
import time
logging.basicConfig()


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',connection_attempts=5, retry_delay=1))
channel = connection.channel()


string = open("hash_list.txt", "r") ## c kök klasöründe ki dosyamızı okuduk 'read' kipinde.
read = string.readlines() ##     pythonda satır satır dosya okuma kodu.

a_tag = str(read)
b_tag = a_tag.split(", ")
i=0

string2 = open("hash_list_text.txt", "r") ## c kök klasöründe ki dosyamızı okuduk 'read' kipinde.
read2 = string2.readlines() ##     pythonda satır satır dosya okuma kodu.

a_text = str(read2)
b_text = a_text.split(",")

#while (i<=len(b_tag)):

   # channel.queue_declare(queue=str(b_tag[i]))


    #def callback(ch, method, properties, body):
      #  print(" [x] Received -- Properties %r " %body)

    #channel.basic_consume(queue=str(b_tag[i]), on_message_callback=callback, auto_ack=True)

    #channel.queue_declare(queue=str(b_text[i]))

    #def callback(ch, method, properties, body):
     #   print(" [x] Received -- Properties %r " %body)

   # channel.basic_consume(queue=str(b_text[i]), on_message_callback=callback, auto_ack=True)

   # i = i+1

    #if (i ==115):
     #   break#

while i<10000:
    channel.queue_declare(queue=str(i))

    def callback(ch, method, properties, body):
        print(" [x] Received -- Properties %r " %body)

    channel.basic_consume(queue=str(i), on_message_callback=callback, auto_ack=True)
    i= i+1



#channel.queue_declare(queue='hello')

#channel.queue_declare(queue='selamlar')



#channel.basic_consume(
   # queue='hello', on_message_callback=callback, auto_ack=True)
#channel.basic_consume(
 #   queue='selamlar', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()