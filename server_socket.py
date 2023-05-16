import socket

# Configura la dirección IP y el puerto del servidor
SERVER_IP = '192.168.0.9'
SERVER_PORT = 69

# Crea un socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlaza el socket al servidor IP y puerto
server_socket.bind((SERVER_IP, SERVER_PORT))

# Espera una conexión entrante
server_socket.listen(1)
print('Esperando conexiones entrantes...')

# Acepta la conexión entrante y obtiene el socket y la dirección del cliente
(client_socket, client_address) = server_socket.accept()
print(f'Conexión entrante desde {client_address}')

# Recibe la dirección MAC enviada desde el cliente
mac_address = client_socket.recv(1024).decode()
print(f'Dirección MAC recibida: {mac_address}')

# Cierra el socket y el servidor
client_socket.close()
server_socket.close()