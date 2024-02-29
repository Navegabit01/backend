import customtkinter
import asyncio
from asyncio import *
import uuid
from payment_view import *
from src.apps.interfaces.interface import AmbitApp
import requests


hay_conexion = False
uid = str(uuid.uuid1()).split("-")[-1]
data = {
    "uid": uid,
    "is_user": False,
    "server_response": None,
    "hay_conexion": False,
    "first-time-message": "Bienvenido que desea hacer",
    "test-user-message": "Se ha registrado para 15 dias de uso en la version de prueba.",
    "premiun-user-message": "Se ha registrado para 60 dias de uso en la version premiun de la aplicacion.",
    "label-title": "System-Tk-Validator",
    "btn-test": "Probar aplicacion",
    "btn-buy": "Comprar aplicacion",
    "url": "http://localhost:8000/userprofile/",  # Cambiar la url local de las consultas, por la real de despliegue
}


async def fetch_status(url: str) -> dict:
    return await asyncio.to_thread(requests.get, url, None)


async def main():
    try:
        global data
        server_data: Task[dict] = asyncio.create_task(
            fetch_status(data["url"] + "?uid=" + uid)
        )
        mydata = await server_data
        data["server_response"] = mydata
        data["hay_conexion"] = True
    except:
        pass


asyncio.run(main=main())


if not data["hay_conexion"] or data["server_response"].status_code == 403:
    root = customtkinter.CTk()
    root.geometry("500x350")
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    PaymentView(root, data)
else:
    if data["server_response"].status_code == 404:
        requests.post(data["url"], data={"uid": data["uid"]})
    root = AmbitApp()

root.mainloop()
