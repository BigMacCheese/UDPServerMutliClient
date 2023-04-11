# UDPServerMutliClient

0. Cambiar el iphost tanto de udpserver.py y del udpclient.py a la ip de la maquina que va hostear el servidor.

1. Ejecutar el udpserver.py en una linea de comandos las cuales debe recibir como parametros el tamaño de los datagramas que se van a enviar (entre 1 y 63) y el tamaño del archivo que se quiere enviar (100 o 250)

ejemplo: udpserver.py 32 100

2. Ejecutar el archivo startMultiClients.py en una consola de python la cual va necesitar el tamaño de los datagramas que se van a enviar (el mismo numero ingresado en el servidor) y el numero de clientes que quieren recibir los documentos (max 25).

3. Todos los archivos recibidos y los logs van a estar en sus respectivas carpetas
