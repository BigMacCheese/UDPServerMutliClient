import subprocess
import os

print('Defina el tamaño de los mensajes en que se deben fragmentar los archivos. Los fragmentos deben ser menores o iguales a 63 kB (escriba el valor en kB)')
buf = input()

print('Ingrese el tamaño del archivo que se desea enviar: 100 MB  o 250 MB (solo escriba el numero)')
size = input()

print('Ingrese cuantos clientes quiere que reciban el archivo')
n_clientes = int(input())

absolute_path = os.path.dirname(__file__)
relative_path_server = "udpserver.py"
relative_path_client = "udpclient.py"

path_server = os.path.join(absolute_path, relative_path_server)
path_client = os.path.join(absolute_path, relative_path_client)

server_process = subprocess.Popen(['python', path_server, buf, size])

for i in range(n_clientes): 
    subprocess.Popen(['python', path_client, buf, str(i), str(n_clientes)])




