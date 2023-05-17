import asyncio
import websockets
from cryptography.fernet import Fernet

# Generar una clave de cifrado
clave = Fernet.generate_key()
fernet = Fernet(clave)

async def servidor(websocket, ruta):
    while True:
        # Recibir datos del cliente
        datos_cifrados = await websocket.recv()
        
        # Desencriptar los datos
        datos = fernet.decrypt(datos_cifrados)
        mensaje = datos.decode()
        print(f"Mensaje recibido: {mensaje}")
        
        # Responder al cliente
        respuesta = "Mensaje recibido correctamente"
        respuesta_cifrada = fernet.encrypt(respuesta.encode())
        await websocket.send(respuesta_cifrada)

start_server = websockets.serve(servidor, "0.0.0.0", 8765)

print("Servidor en ejecución...")

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()