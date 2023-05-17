import asyncio
import websockets
from cryptography.fernet import Fernet

# Clave de cifrado utilizada en el servidor
clave = b'ClaveDeCifradoDelServidorAquí'

async def cliente():
    async with websockets.connect("ws://<dirección_del_servidor>:8765") as websocket:
        while True:
            # Enviar datos al servidor
            mensaje = input("Ingrese un mensaje: ")
            datos_cifrados = Fernet(clave).encrypt(mensaje.encode())
            await websocket.send(datos_cifrados)
            
            # Recibir respuesta del servidor
            respuesta_cifrada = await websocket.recv()
            respuesta = Fernet(clave).decrypt(respuesta_cifrada)
            print(f"Respuesta del servidor: {respuesta.decode()}")

asyncio.get_event_loop().run_until_complete(cliente())
