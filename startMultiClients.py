import subprocess
import os

print('Ingrese cuantos clientes quiere que reciban el archivo')
n_clientes = int(input())

absolute_path = os.path.dirname(__file__)
relative_path_server = "udpserver.py"
relative_path_client = "udpclient.py"

path_server = os.path.join(absolute_path, relative_path_server)
path_client = os.path.join(absolute_path, relative_path_client)

for i in range(n_clientes): 
    subprocess.Popen(['python', path_client, buf, str(i), str(n_clientes)])




