import customtkinter
import datetime
from tkinter import *
import time
import requests
import asyncio
from requests import *
from asyncio import *
import uuid
from payment_view import *

from time import time

usuario_existente = "ghg"
usuario_no_existente = "111"
hay_conexion = False
uid = str(uuid.uuid1()).split("-")[-1]
data = {
    "uid":uid,
    "is_user": False,
    "server_response":None,
    'hay_conexion':False,
    "first-time-message": "Bienvenido que desea hacer",
    "test-user-message": "Se ha registrado para 15 dias de uso en la version de prueba.",
    "premiun-user-message": "Se ha registrado para 60 dias de uso en la version premiun de la aplicacion.",
    "label-title": "System-Tk-Validator",
    "btn-test": "Probar aplicacion",
    "btn-buy": "Comprar aplicacion",
    "url": "http://localhost:8000/userprofile/",  # Cambiar la url local de las consultas, por la real de despliegue
}

root = customtkinter.CTk()
root.geometry("500x350")

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

async def fetch_status(url: str) -> dict:
    return await asyncio.to_thread(requests.get, url, None)
    # response: Response = await asyncio.to_thread(requests.get, url, None)
    # return response

async def main():
    try:
        global data
        server_data: Task[dict] = asyncio.create_task(
            fetch_status(data["url"] +"?uid="+ uid)
        )
        data['server_response'] =  await server_data
        data['hay_conexion'] = True
    except:
        pass

asyncio.run(main=main())

# Falta la llamada recursiva 
# para validar cada 1h.

PaymentView(root,data)

root.mainloop()