import socket 
import time
import os
from datetime import datetime
import sys
from _thread import *
import threading

iphost = '127.0.0.1'
port = 20001
file_name = ''
relative_path = ''
tiempo_transferencia = 0
thread_count = 0

buffer_size = int(sys.argv[1])*1024
archive_size = str(sys.argv[2])

if archive_size == '100':
    relative_path = "100000000B.txt"
    file_name = '100000000B'
    print('Enviando el archivo de 100 MB ...')

elif archive_size == '250': 
    relative_path = "250000000B.txt"
    file_name = '250000000B'
    
    print('Enviando el archivo de 250 MB ...')

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

absolute_path = os.path.dirname(__file__)
print(absolute_path)
now = datetime.now()
log_name = now.strftime("Servidor-%Y-%m-%d-%H-%M-%S-log.txt")
log_relative_path = "Logs\{}".format(log_name)
log_path = os.path.join(absolute_path, log_relative_path)

try:
    UDPServerSocket.bind((iphost, port))
except socket.error as e:
    print(str(e))

print('El servidor esta recibiendo conexiones...')

log_lock = threading.Lock()

def multi_thread_client(addr, id_cliente):

    file_name_bytes = file_name.encode('utf-8')
    tiempo_inicio = time.time()
    UDPServerSocket.sendto(file_name_bytes, addr)

    full_path = os.path.join(absolute_path, relative_path)

    f = open(full_path, "rb")
    data = f.read(buffer_size)

    while(data):

        if UDPServerSocket.sendto(data, addr):
            data = f.read(buffer_size)
            time.sleep(0.02)

    tiempo_fin = time.time()
    tiempo_transferencia = tiempo_fin - tiempo_inicio

    log_lock.acquire()

    log = open(log_path, 'a')
    log.write("Id Cliente: " + str(id_cliente) + ", Nombre archivo enviado: " + file_name + ", Tamaño del archivo: " + archive_size + "MB, Tiempo de transferencia: " + str(tiempo_transferencia))
    log.write("\n")
    log.close()

    log_lock.release()

    f.close()
    

while True:
    
    data, addr = UDPServerSocket.recvfrom(buffer_size)
    data_strip = data.strip()
    cliente = data_strip.decode('utf-8')

    print('Conectado: ' + cliente)
    
    thread_count += 1
    start_new_thread(multi_thread_client, (addr, thread_count))
    print('# thread: ' + str(thread_count))




          










    

        
        





