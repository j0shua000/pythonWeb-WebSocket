import websocket
import ssl

# URL del servidor WebSocket seguro en la Raspberry Pi
url = "wss://direccion_ip_raspberry:puerto"

# Crear una conexión WebSocket segura
ws = websocket.WebSocket(sslopt={"cert_reqs": ssl.CERT_NONE})

# Conectar al servidor
ws.connect(url)

# Enviar datos al servidor
ws.send("¡Hola desde el cliente!")

# Recibir datos del servidor
response = ws.recv()
print("Respuesta del servidor:", response)

# Cerrar la conexión
ws.close()