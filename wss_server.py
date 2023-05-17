import ssl
import websocket

def on_message(ws, message):
    # Manejar el mensaje recibido
    print("Mensaje recibido:", message)

# Configurar el contexto SSL
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
ssl_context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")  # Ruta al certificado y clave

# Crear una instancia de WebSocketServer
server = websocket.WebSocketServer(
    host='0.0.0.0',  # Dirección IP de la Raspberry Pi
    port=8765,  # Puerto para la conexión WebSocket
    ssl_context=ssl_context,
    certfile="cert.pem",  # Ruta al certificado
    keyfile="key.pem"  # Ruta a la clave privada
)
server.set_fn_message_received(on_message)
server.run_forever()