from websocket_server import WebsocketServer
import ssl

# Puerto en el que el servidor WebSocket estará escuchando
puerto = 5353

# Función que se ejecuta cuando se recibe un mensaje del cliente
def on_message(client, server, message):
    print("Mensaje recibido del cliente:", message)
    
    # Enviar respuesta al cliente
    server.send_message(client, "¡Hola desde el servidor!")

# Ruta al certificado y la clave privada
cert_file = "./certificado.pem"
key_file = "./clave_privada.pem"

# Crear un servidor WebSocket seguro
server = WebsocketServer(puerto, host='0.0.0.0', ssl={
    'certfile': 'cert_file',
    'keyfile': 'key_file'
})

# Asociar la función on_message al evento "message"
server.set_fn_message_received(on_message)

# Iniciar el servidor
server.run_forever()
