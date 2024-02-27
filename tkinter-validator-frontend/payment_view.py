from src.apps.interfaces.interface import AmbitApp
import customtkinter as CTK
import webbrowser

url = "http://localhost:8000/"


class PaymentView:
    def __init__(self, root, data) -> None:
        self.data = data
        self.frame = CTK.CTkFrame(master=root)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)
        self.label = CTK.CTkLabel(
            master=self.frame, text=data["label-title"], font=("Roboto", 24)
        )
        self.label.pack(pady=20, padx=10)
        if not data["hay_conexion"]:
            self.not_conexion = CTK.CTkLabel(
                master=self.frame,
                text="No es posible conectarse al servicio.\n revise su conexion a internet o contacte con el \n administrador del servicio.",
                font=("Roboto", 12),
            )
            self.not_conexion.pack(pady=30, padx=10)
        elif data["server_response"].status_code == 403:
            self.label2 = CTK.CTkLabel(
                master=self.frame,
                text="Su cuenta ha vencido \n seleccione la opcion de compra para usar la aplicacion.",
                font=("Roboto", 12),
            )
            self.label2.pack(pady=30, padx=10)
            self.button1 = CTK.CTkButton(
                master=self.frame,
                text="Comprar aplicación",
                command=lambda: webbrowser.open(url),
            )
            self.button1.pack(pady=12, padx=10)
