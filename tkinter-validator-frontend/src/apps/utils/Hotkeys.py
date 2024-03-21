import customtkinter as ctk


class Hotkey1(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Hotkey no_1")
        self.geometry("350x120")
        self.resizable(False, False)
        self.label = ctk.CTkLabel(
            self,
            text="Introduzca el atajo de teclado deseado:\n\n" + "Ctrl + Shift + l",
        )
        self.label.grid(row=1, column=0, padx=70, pady=10, sticky="w")

        self.aceptar = ctk.CTkButton(self, text="Aceptar", width=50)
        self.aceptar.grid(row=2, column=0, padx=100, pady=10, sticky="w")

        self.cerrar = ctk.CTkButton(
            self, text="Cerrar", width=50, command=self.close_window
        )
        self.cerrar.grid(row=2, column=0, padx=200, pady=10, sticky="w")

        self.bind("<Key>", self.on_key_press)

    def close_window(self):
        self.destroy()

    def on_key_press(self, event):
        print(event)

        self.label.configure(
            text=f"Introduzca el atajo de teclado deseado: \n\n{event.keysym}"
        )


class Hotkey2(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Hotkey no_2")
        self.geometry("350x120")
        self.resizable(False, False)

        self.label = ctk.CTkLabel(
            self,
            text="Introduzca el atajo de teclado deseado:\n\n" + "Ctrl + Shift + l",
        )
        self.label.grid(row=1, column=0, padx=70, pady=10, sticky="w")

        self.aceptar = ctk.CTkButton(self, text="Aceptar", width=50)
        self.aceptar.grid(row=2, column=0, padx=100, pady=10, sticky="w")

        self.cerrar = ctk.CTkButton(
            self, text="Cerrar", width=50, command=self.close_window
        )
        self.cerrar.grid(row=2, column=0, padx=200, pady=10, sticky="w")

        self.bind("<Key>", self.on_key_press)

    def close_window(self):
        self.destroy()

    def on_key_press(self, event):
        print(event)
        self.label.configure(text=f"Tecla presionada:  \n{event.keysym}")
