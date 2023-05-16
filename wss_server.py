from websocket_server import WebsocketServer
import ssl

# Puerto en el que el servidor WebSocket estará escuchando
puerto = 9000

# Función que se ejecuta cuando se recibe un mensaje del cliente
def on_message(client, server, message):
    print("Mensaje recibido del cliente:", message)
    
    # Enviar respuesta al cliente
    server.send_message(client, "¡Hola desde el servidor!")

# Crear un servidor WebSocket seguro
server = WebsocketServer(puerto, host='0.0.0.0', ssl={
    'certfile': 'ruta_al_certificado',
    'keyfile': 'ruta_a_la_clave_privada'
})

# Asociar la función on_message al evento "message"
server.set_fn_message_received(on_message)

# Iniciar el servidor
server.run_forever()
