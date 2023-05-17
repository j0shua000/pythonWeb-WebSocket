import ssl
import websocket

def on_message(ws, message):
    # Manejar el mensaje recibido
    print("Mensaje recibido:", message)

# Configurar el contexto SSL
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
ssl_context.verify_mode = ssl.CERT_NONE

# Crear una instancia de WebSocketApp
ws = websocket.WebSocketApp(
    "wss://<dirección_IP_de_la_Raspberry_Pi>:8765",  # Dirección IP y puerto de la Raspberry Pi
    on_message=on_message,
    ssl_context=ssl_context
)

ws.run_forever()
