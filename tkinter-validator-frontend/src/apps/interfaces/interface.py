from src.apps.utils.translate import Translations2, Translate
from src.apps.utils.Hotkeys import Hotkey1, Hotkey2
from src.apps.utils.Hotkeys import HotkeyValidator as HV
from tkinter import messagebox
import customtkinter as ctk
import os
import json
from PIL import ImageTk


"""
 - Creo los hotkey si no existen 
 - los guardo en el archivo de configuracion
 - Los cargo para abrr

"""


class Configuration:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Configuration, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.initial_language = "English"
        self.in_out_selector_pos = 0
        self.options = 0
        self.checkbox_continue_check_var = ctk.StringVar(value="off")
        self.configuration = {}
        self.hotkey1 = "<Control-x>"
        self.hotkey2 = "<Control-Shift-X>"
        self.lang = "English"
        self.ambitapp = None

    def set_ambitapp(self, ambit):
        self.ambitapp = ambit

    def set_current_lang(self, lang):
        self.lang = lang

    def get_current_lang(self):
        return self.lang

    def set_hotkey1(self, hotkey):
        self.hotkey1 = hotkey

    def get_hotkey1(self):
        return self.hotkey1

    def set_hotkey2(self, hotkey):
        self.hotkey2 = hotkey

    def get_hotkey2(self):
        return self.hotkey2

    def load_config(self):
        try:
            with open("config.json", "r") as file:
                data = json.loads(file.read())
                self.initial_language = data["lang"]
                self.in_out_selector_pos = data["in_out_selector_pos"]
                self.options = data["opts"]
                self.hotkey1 = data["hotkey1"]
                self.hotkey2 = data["hotkey2"]
        except:
            self.save_config()

    def save_config(self):
        self.configuration = {
            "lang": self.initial_language,
            "in_out_selector_pos": self.in_out_selector_pos,
            "opts": self.options,
            "hotkey1": self.hotkey1,
            "hotkey2": self.hotkey2,
        }

        jsondata = json.dumps(self.configuration, indent=1)
        with open("config.json", "w") as file:
            file.write(jsondata)


class AmbitApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.lang = Translations2()
        self.config = Configuration()
        self.config.load_config()
        self.lang.set_current_language(self.config.initial_language)
        self.config.set_ambitapp(self)
        self.hv = HV()
        self.geometry("800x450")
        self.icon_path = os.getcwd() + "/src/assets/icon.png"
        self.geometry("800x450")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.title(self.lang.get_value("title"))
        # Cargar los iconos
        self.iconphoto(True, ImageTk.PhotoImage(file="./src/assets/icon.png"))
        self.eye_open_icon = ImageTk.PhotoImage(file="./src/assets/eye-open.png")
        self.eye_closed_icon = ImageTk.PhotoImage(file="./src/assets/eye-close.png")
        self.configure(bg="#ADD8E6")

        # Etiqueta de registro
        self.registration_label = ctk.CTkLabel(self)
        self.registration_label.grid(row=1, column=0, columnspan=2, padx=20, sticky="w")

        # Selector de lenguage
        self.language_selector = ctk.CTkOptionMenu(
            self, values=["Español", "English"], command=self.change_language
        )
        self.language_selector.grid(row=2, column=0, padx=20, sticky="w")

        # Campo de insercion de la API
        self.api_key_entry = ctk.CTkEntry(self, show="*", width=400)
        self.api_key_entry.grid(row=3, column=0, padx=20, pady=20, sticky="w")

        # Boton de visualizacion  de la llave
        self.toggle_btn = ctk.CTkButton(
            self,
            text="",
            width=30,
            image=self.eye_open_icon,
            command=self.toggle_api_visibility,
        )
        self.toggle_btn.grid(row=3, column=1, padx=0, pady=0, sticky="W")

        # Campo de insercion de extensiones
        self.file_extensions_entry = ctk.CTkEntry(
            self, placeholder_text_color="red", width=15
        )
        self.file_extensions_entry.insert(
            0, ".doc, .txt, .py, .php, .html, .cs, .exe, .css"
        )
        self.file_extensions_entry.grid(row=9, column=0, padx=20, pady=10, sticky="we")

        # Hotkey 1
        self.hotkey_label1 = ctk.CTkLabel(self)
        self.hotkey_label1.grid(row=10, column=0, padx=20, sticky="w")

        self.hotkey_button1 = ctk.CTkButton(
            self, text=self.lang.get_value("set_hotkey_1"), command=self.call_hotkey1
        )
        self.hotkey_button1.grid(row=10, column=1, padx=10, pady=10, sticky="w")
        ###

        # Hotkey 2
        self.hotkey_label2 = ctk.CTkLabel(self)
        self.hotkey_label2.grid(row=11, column=0, padx=20, sticky="w")
        self.hotkey_button2 = ctk.CTkButton(
            self, text=self.lang.get_value("set_hotkey_2"), command=self.call_hotkey2
        )
        self.hotkey_button2.grid(row=11, column=1, padx=10, pady=10, sticky="w")

        # Selector de activacion
        switch_var = ctk.StringVar(value="on")
        self.activation_switch = ctk.CTkSwitch(
            self, variable=switch_var, onvalue="on", offvalue="off"
        )
        self.activation_switch.grid(row=13, column=0, padx=20, pady=10, sticky="w")

        # Etiqueta de contacto
        self.contact_info_label = ctk.CTkLabel(self)
        self.contact_info_label.grid(
            row=35, column=0, padx=20, pady=30, sticky="w", columnspan=3
        )

        # Boton de guardado configuracion
        self.save_config = ctk.CTkButton(
            self, text="", width=30, command=self.save_user_config
        )
        self.save_config.grid(row=34, column=1, padx=0, pady=0, sticky="W")

        # Configuracion de los hotkeys
        self.hotkey_window = None
        self.hotkey_window_2 = None

        # Configuracion temporal
        self.options = self.lang.get_value("in_out_selector")
        self.options_pos = 0

        # Data
        temp = self.lang.get_value("in_out_selector")[self.config.in_out_selector_pos]
        self.opciones_var1 = ctk.StringVar(value=temp)
        self.option_menu = ctk.CTkOptionMenu(
            self,
            values=self.options,
            variable=self.opciones_var1,
            command=self.save_text_in_out_selector,
        )
        # Data

        # self.optionmenu.set("Seleccione la deseada." if self.nooption else "Hola")
        self.option_menu.grid(row=32, column=0, padx=10, pady=(10, 0), sticky="w")

        self.bind(self.config.get_hotkey1(), self.optionmenu_callback)
        self.bind(self.config.get_hotkey2(), self.action_over_activation_button)

        self.update_texts()

    def save_text_in_out_selector(self, event):
        for pos, i in enumerate(self.lang.get_value("in_out_selector")):
            if i == event:
                self.config.in_out_selector_pos = pos
                break

    def call_hotkey1(self):
        toplv = self.hotkey_window
        if toplv is None or not toplv.winfo_exists():
            self.hotkey_window = Hotkey1(self)
            self.hotkey_window.set_singlenton(self.config)
            return
        self.hotkey_window.focus()

    def call_hotkey2(self):
        toplv = self.hotkey_window_2
        if toplv is None or not toplv.winfo_exists():
            self.hotkey_window_2 = Hotkey2(self)
            self.hotkey_window_2.set_singlenton(self.config)
            return
        self.hotkey_window_2.focus()

    def save_user_config(self):
        self.config.initial_language = self.lang.current_language
        self.config.save_config()

    def action_over_activation_button(self, choice):
        self.activation_switch.toggle()

    def optionmenu_callback(self, choice):
        if self.options_pos == 4:
            self.options_pos = -1
        self.options_pos += 1
        self.option_menu.set(self.options[self.options_pos])
        # Fin del bloque de configuracion temporal

    def show_message_function(self):
        self.show_message = True

    def toggle_api_visibility(self):
        if self.api_key_entry.cget("show") == "":
            self.api_key_entry.configure(show="*")
            self.toggle_btn.configure(image=self.eye_closed_icon)
        else:
            self.api_key_entry.configure(show="")
            self.toggle_btn.configure(image=self.eye_open_icon)

    def init_config(self):
        pass

    def change_language(self, language):
        self.lang.current_language = language
        self.update_texts()

    def update_texts(self):
        self.title(self.lang.get_value("title"))
        self.option_menu.configure(values=self.lang.get_value("in_out_selector"))
        self.save_config.configure(text=self.lang.get_value("save_config"))
        self.api_key_entry.configure(placeholder_text=self.lang.get_value("apy_key"))
        self.activation_switch.configure(text=self.lang.get_value("activate_app"))
        # self.checkbox_continue.configure(text=self.lang.get_value("checkbox_continue"))
        self.registration_label.configure(
            text=self.lang.get_value("registration_label")
        )
        self.contact_info_label.configure(text=self.lang.get_value("contact_info"))
        self.file_extensions_entry.configure(
            placeholder_text=self.lang.get_value("apy_key")
        )
        self.language_selector.set(self.lang.current_language)

        self.hotkey_label1.configure(
            text=self.lang.get_value("hotkey_1_default")
            + self.hv.config_to_load(self.config.hotkey1)
        )

        self.hotkey_label2.configure(
            text=self.lang.get_value("hotkey_2_default")
            + self.hv.config_to_load(self.config.hotkey2)
        )


class Hotkey1(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Hotkey no_1")
        self.geometry("350x120")
        self.resizable(False, False)
        self.singlenton = None
        self.hv = HV()
        self.hotkey_default = None
        self.current_hotkey = []
        self.label = ctk.CTkLabel(
            self,
        )
        self.label.grid(row=1, column=0, padx=70, pady=10, sticky="w")

        self.aceptar = ctk.CTkButton(
            self, text="Aceptar", width=50, command=self.save_hotkey_conf
        )
        self.aceptar.grid(row=2, column=0, padx=100, pady=10, sticky="w")

        self.cerrar = ctk.CTkButton(
            self, text="Cerrar", width=50, command=self.close_window
        )
        self.cerrar.grid(row=2, column=0, padx=200, pady=10, sticky="w")

        self.bind("<Key>", self.on_key_press)

    def set_singlenton(self, singlenton):
        self.singlenton = singlenton
        self.hotkey_default = self.hv.config_to_load(singlenton.get_hotkey1())
        self.label.configure(
            text="Introduzca el atajo de teclado deseado:\n\n" + self.hotkey_default
        )

    def save_hotkey_conf(self):
        if not self.hv.valid_hotkey_secuence():
            messagebox.showerror(
                "Combinacion incorrecta", "La combinacion de teclas no es correcta."
            )
            self.label.configure(
                text=f"Introduzca el atajo de teclado deseado: \n\n{self.hotkey_default}"
            )
        else:
            self.singlenton.set_hotkey1(self.hv.create_hotkey_to_main())
            self.singlenton.ambitapp.update_texts()
            self.close_window()

    def close_window(self):
        self.destroy()

    def on_key_press(self, evt):
        res = ""
        self.current_hotkey.append(evt.keysym)
        self.current_hotkey = self.hv.configure_key_press(self.current_hotkey)
        if len(self.current_hotkey) > 1:
            res = "   +   ".join(self.current_hotkey)
        elif len(self.current_hotkey) == 1:
            res = self.current_hotkey[0]
        self.label.configure(
            text=f"Introduzca el atajo de teclado deseado: \n\n{res if len(res) >= 1 else self.hotkey_default}"
        )


class Hotkey2(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Hotkey no_2")
        self.geometry("350x120")
        self.resizable(False, False)
        self.hv = HV()
        self.singlenton = None
        self.hotkey_default = None
        self.current_hotkey = []
        self.label = ctk.CTkLabel(
            self,
        )
        self.label.grid(row=1, column=0, padx=70, pady=10, sticky="w")

        self.aceptar = ctk.CTkButton(
            self, text="Aceptar", width=50, command=self.save_hotkey_conf
        )
        self.aceptar.grid(row=2, column=0, padx=100, pady=10, sticky="w")

        self.cerrar = ctk.CTkButton(
            self, text="Cerrar", width=50, command=self.close_window
        )
        self.cerrar.grid(row=2, column=0, padx=200, pady=10, sticky="w")

        self.bind("<Key>", self.on_key_press)

    def set_singlenton(self, singlenton):
        self.singlenton = singlenton
        self.hotkey_default = self.hv.config_to_load(singlenton.get_hotkey2())
        self.label.configure(
            text="Introduzca el atajo de teclado deseado:\n\n" + self.hotkey_default
        )

    def save_hotkey_conf(self):
        if not self.hv.valid_hotkey_secuence():
            messagebox.showerror(
                "Combinacion incorrecta", "La combinacion de teclas no es correcta."
            )
            self.label.configure(
                text=f"Introduzca el atajo de teclado deseado: \n\n{self.hotkey_default}"
            )
        else:
            self.singlenton.set_hotkey2(self.hv.create_hotkey_to_main())
            self.singlenton.ambitapp.update_texts()
            self.close_window()

    def close_window(self):
        self.destroy()

    def on_key_press(self, evt):
        res = ""
        self.current_hotkey.append(evt.keysym)
        self.current_hotkey = self.hv.configure_key_press(self.current_hotkey)
        if len(self.current_hotkey) > 1:
            res = "   +   ".join(self.current_hotkey)
        elif len(self.current_hotkey) == 1:
            res = self.current_hotkey[0]
        self.label.configure(
            text=f"Introduzca el atajo de teclado deseado: \n\n{res if len(res) >= 1 else self.hotkey_default}"
        )
