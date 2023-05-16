import asyncio
import ssl
import pathlib
import websockets

# Puerto en el que el servidor WebSocket estará escuchando
puerto = 9000

# Rutas a los archivos de certificado y clave privada
ruta_certificado = pathlib.Path('./certificado.pem')
ruta_clave_privada = pathlib.Path('./clave_privada.pem')

# Cargar los archivos de certificado y clave privada
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain(ruta_certificado, ruta_clave_privada)

# Función que se ejecuta cuando se recibe un mensaje del cliente
async def on_message(websocket, path):
    message = await websocket.recv()
    print("Mensaje recibido del cliente:", message)
    
    # Enviar respuesta al cliente
    await websocket.send("¡Hola desde el servidor!")

# Crear un servidor WebSocket seguro
start_server = websockets.serve(on_message, "0.0.0.0", puerto, ssl=ssl_context)

# Iniciar el servidor
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
