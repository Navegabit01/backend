import asyncio
import os
import requests
import uuid
import hashlib
import dotenv
from payment_view import PaymentView
from src.apps.interfaces.interface import AmbitApp
from customtkinter import CTk, set_appearance_mode, set_default_color_theme

dotenv.load_dotenv()


class AppValidatorService:
    def __init__(self):
        self.url = os.getenv("APP_VALIDATOR_URL")
        if not self.url:
            print(self.url)
            raise ValueError("APP_VALIDATOR_URL environment variable not set")
        self.data = {
            "url": self.url,
            "uid": self.generate_unique_code(),
            "is_user": False,
            "server_response": None,
            "hay_conexion": False,
            "first-time-message": "Bienvenido que desea hacer",
            "test-user-message": "Se ha registrado para 15 dias de uso en la "
                                 "version de prueba.",
            "premiun-user-message": "Se ha registrado para 60 dias de uso en "
                                    "la version premiun de la aplicacion.",
            "label-title": "System-Tk-Validator",
            "btn-test": "Probar aplicacion",
            "btn-buy": "Comprar aplicacion",
        }

    @staticmethod
    def generate_unique_code():
        mac = uuid.getnode()
        mac_address = (':'.
                       join(['{:02x}'.format((mac >> i) & 0xff)
                             for i in range(0, 8 * 6)]))
        hash_digest = hashlib.sha256(mac_address.encode()).hexdigest()
        return hash_digest

    @staticmethod
    async def fetch_status(url_input: str) -> dict:
        return await asyncio.to_thread(requests.get, url_input, None)

    async def main(self):
        try:
            mydata = await self.fetch_status(
                self.data["url"] + "?uid=" + self.data["uid"])
            self.data["server_response"] = mydata
            self.data["hay_conexion"] = True
        except Exception as error:
            print("Oops! Something went wrong." + str(error))

    async def validate_application(self):
        await self.main()
        if (not self.data["hay_conexion"] or
                self.data["server_response"].status_code == 403):
            root = CTk()
            root.geometry("500x350")
            set_appearance_mode("dark")
            set_default_color_theme("dark-blue")
            PaymentView(root, self.data)
        elif self.data["server_response"].status_code == 404:
            requests.post(self.data["url"], data={"uid": self.data["uid"]})
            root = AmbitApp()
            root.mainloop()


async def schedule_validation(service: AppValidatorService):
    while True:
        await service.validate_application()
        await asyncio.sleep(3600)  # Sleep for 1 hour (3600 seconds)


if __name__ == "__main__":
    validator = AppValidatorService()
    asyncio.run(schedule_validation(validator))
