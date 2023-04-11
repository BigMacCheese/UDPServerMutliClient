import socket
import time
import select
from datetime import datetime
import os
import sys

buffer_size = int(sys.argv[1]) * 1024
id_cliente = sys.argv[2]
n_clientes = sys.argv[3]

iphost = '127.0.0.1'
port = 20001
tiempo_transferencia = 0
timeout = 5

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

cliente = 'Cliente 1'
cliente_bytes = cliente.encode('utf-8')

UDPClientSocket.sendto(cliente_bytes, (iphost, port))

tiempo_inicio = time.time()
data_name, addr = UDPClientSocket.recvfrom(buffer_size)

if data_name:
    file_name_bytes = data_name.strip()
    file_name = file_name_bytes.decode('utf-8')

    file_size = int(file_name[:9])

    print('File name: ', file_name)

    relative_path = "ArchivosRecibidos\Cliente{}-Prueba{}.txt".format(id_cliente, n_clientes)
    absolute_path = os.path.dirname(__file__)
    full_path = os.path.join(absolute_path, relative_path)

    now = datetime.now()
    log_name = now.strftime("Cliente{}-%Y-%m-%d-%H-%M-%S-log.txt").format(id_cliente)
    log_relative_path = "Logs\{}".format(log_name)
    log_path = os.path.join(absolute_path, log_relative_path)

    exito = ''

    f = open(full_path, 'wb')

    while True:
        ready = select.select([UDPClientSocket], [], [], timeout)
        if ready[0]:
            data, addr = UDPClientSocket.recvfrom(buffer_size)
            f.write(data)
        else:
            tiempo_fin = time.time()
            tiempo_transferencia = tiempo_fin - tiempo_inicio - 5
            print("La conexion con el servidor termino")

            real_file_size = os.path.getsize(full_path)
            if file_size == real_file_size:
                exito = "Si"
            else:
                exito = "No"
            break

    print('La transferencia de archivos se demoro: ', tiempo_transferencia)
    log = open(log_path, 'w')
    log.write("Id Cliente: " + str(id_cliente) + ", Nombre archivo: " + file_name +  ", Tiempo de transferencia: " + str(tiempo_transferencia) + ", Exito de transferencia: " + exito)
    log.close()
else:
    print("Error: No se recibio ningun paquete del servidor.")