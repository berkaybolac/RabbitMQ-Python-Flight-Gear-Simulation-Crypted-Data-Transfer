import pika
import sys
import xml.etree.ElementTree as ET
import mysql.connector
import socket
import time
# Here we define the UDP IP address as well as the port number that we have
# already defined in the client python script.
UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 4545

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# One difference is that we will have to bind our declared IP address
# and port number to our newly declared serverSock

serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
time.sleep(1)


tree = ET.parse('a.xml')
root = tree.getroot()

#print([elem.tag for elem in root.iter()])
#for child in root:x
        #print(child.tag)
listtag = []
listtext  =[]

for neighbor in root.getiterator():
    print(neighbor.text)
    if neighbor.text != '\n        ':
        if neighbor.text != '\n              ':
            if neighbor.text !='\n    ':
                if neighbor.text !='\n  ':
                    if neighbor.text!='\n          ':
                        if neighbor.text!='\n      ':
                            if neighbor.text!='\n            ':
                             listtag.append(neighbor.tag)
                             listtext.append(neighbor.text)


listhash = []
listhash_text = []

def hashtag():
    for i in listtag:
        listhash.append(hash(i))
    return listhash

def hashtext():
    for i in listtext:
        listhash_text.append(hash(i))
    return listhash_text

def fileonhash():
    orj_wr = open("hash_list.txt", "w") ## açılmış halini yeniden yazacağımız dosyamızı oluşturduk.
    orj_wr.writelines(str(hashtag()))
    orj_wr.close()

def fileonhash_text():
    orj_wr = open("hash_list_text.txt", "w") ## açılmış halini yeniden yazacağımız dosyamızı oluşturduk.
    orj_wr.writelines(str(hashtext()))
    orj_wr.close()

fileonhash_text()

fileonhash()


string = open("hash_list.txt", "r") ## c kök klasöründe ki dosyamızı okuduk 'read' kipinde.
read = string.readlines() ##     pythonda satır satır dosya okuma kodu.

string2 = open("hash_list_text.txt", "r") ## c kök klasöründe ki dosyamızı okuduk 'read' kipinde.
read2 = string2.readlines()

a_text = str(read2)
b_text = a_text.split(",")


a_tag = str(read)
b_tag = a_tag.split(", ")


i=0


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel=connection.channel()




while 1:

    data, addr = serverSock.recvfrom(1024)
    print("UCUS BILGILERI: ", data)
    channel.queue_declare(queue=str(i))

    channel.basic_publish(exchange='', routing_key=str(i), body=str(data))
    i=i+1

connection.close()

#while (i<=len(b_tag)):
 #   print(b_tag[i])
  #  print(b_text[i])

   # channel.queue_declare(queue=str(b_tag[i]))
    #channel.queue_declare(queue=str(b_text[i]))

    #channel.basic_publish(exchange='', routing_key=str(b_tag[i]), body=str(listtag[i]))
    #channel.basic_publish(exchange='', routing_key=str(b_text[i]), body=str(listtext[i]))

    #i = i+1

    #if (i ==115):
     #   break


#channel.queue_declare(queue='selamlar')


#channel.basic_publish(exchange='', routing_key='selamlar', body='selamlar ucus bilgileri asagidadir')



#print(" [x] Sent 'Hello World!'")
#print(" [x] Sent 'selamlar ucus bilgileri asagidadir'")

