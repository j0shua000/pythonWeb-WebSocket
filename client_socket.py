import socket
import netifaces

# Configura la dirección IP y el puerto del servidor
SERVER_IP = '192.168.1.100'
SERVER_PORT = 8000

# Crea un socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta el socket al servidor IP y puerto
client_socket.connect((SERVER_IP, SERVER_PORT))
print(f'Conectado al servidor {SERVER_IP}:{SERVER_PORT}')

# Obtiene la dirección MAC del cliente
mac_address = netifaces.ifaddresses('wlan0')[netifaces.AF_LINK][0]['addr']
print(f'Dirección MAC del cliente: {mac_address}')

# Envía la dirección MAC al servidor
client_socket.send(mac_address.encode())
print('Dirección MAC enviada al servidor')

# Cierra el socket
client_socket.close()