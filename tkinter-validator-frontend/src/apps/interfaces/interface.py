from src.apps.utils.translate import Translations2, Translate
import customtkinter as ctk
import os
import json
from PIL import Image, ImageTk
import PIL


class Configuration:
    def __init__(self):
        self.initial_language = "English"
        self.in_out_selector_pos = 0
        self.options = 0
        self.checkbox_continue_check_var = ctk.StringVar(value="off")
        self.configuration = {}

    def load_config(self):
        try:
            with open("config.json", "r") as file:
                data = json.loads(file.read())
                self.initial_language = data["lang"]
                self.in_out_selector_pos = data["selector_pos"]
                self.options = data["opts"]
        except:
            self.save_config()

    def save_config(self):
        self.configuration = {
            "lang": self.initial_language,
            "selector_pos": self.in_out_selector_pos,
            "opts": self.options,
        }
        jsondata = json.dumps(self.configuration)
        with open("config.json", "w") as file:
            file.write(jsondata)


class AmbitApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.lang = Translations2()
        self.config = Configuration()
        self.config.load_config()
        self.lang.set_current_language(self.config.initial_language)

        self.geometry("800x600")
        self.icon_path = os.getcwd() + "/src/assets/icon.png"
        self.geometry("800x600")
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
            self, text="", width=30, image=self.eye_closed_icon
        )  # command=self.toggle_api_visibility)
        self.toggle_btn.grid(row=3, column=1, padx=0, pady=0, sticky="W")

        # Campo de insercion de extensiones
        self.file_extensions_entry = ctk.CTkEntry(
            self, placeholder_text_color="red", width=15
        )
        self.file_extensions_entry.insert(
            0, ".doc, .txt, .py, .php, .html, .cs, .exe, .css"
        )
        self.file_extensions_entry.grid(row=9, column=0, padx=20, pady=10, sticky="we")

        self.setup_hotkey_section(
            row=10, column=0, hotkey_default=self.lang.get_value("hotkey_1_default")
        )
        self.setup_hotkey_section(
            row=11, column=0, hotkey_default=self.lang.get_value("hotkey_2_default")
        )

        # Selector de activacion
        switch_var = ctk.StringVar(value="on")
        self.activation_switch = ctk.CTkSwitch(
            self, variable=switch_var, onvalue="on", offvalue="off"
        )
        self.activation_switch.grid(row=13, column=0, padx=20, pady=10, sticky="w")

        # CheckBox de modo continuo
        self.checkbox_continue = ctk.CTkCheckBox(
            self,
            text=self.lang.get_value("checkbox_continue"),
            variable=self.config.checkbox_continue_check_var,
            onvalue="on",
            offvalue="off",
        )
        self.checkbox_continue.grid(row=33, column=0, padx=10, pady=0, sticky="W")

        # Etiqueta de contacto
        self.contact_info_label = ctk.CTkLabel(self)
        self.contact_info_label.grid(
            row=35, column=0, padx=20, pady=30, sticky="w", columnspan=3
        )

        # Boton de guardado configuracion
        self.save_config = ctk.CTkButton(
            self, text="", width=30, command=self.save_user_config
        )  # image=self.eye_closed_icon,# command=self.toggle_api_visibility)
        self.save_config.grid(row=34, column=1, padx=0, pady=0, sticky="W")

        # Configuracion de los hotkeys
        self.hotkey = None
        self.hotkey2 = None

    def call_hotkey1(self):
        toplv = self.hotkey
        if toplv is None or not toplv.winfo_exists():
            self.hotkey = Hotkey1(self)
            return
        self.hotkey.focus()

    def call_hotkey2(self):
        toplv = self.hotkey2
        if toplv is None or not toplv.winfo_exists():
            self.hotkey2 = Hotkey2(self)
            return
        self.hotkey.focus()

        # Fin de la configuracion de los hotkey

        # self.show_message = True
        # self.init_ui()
        self.update_texts()

        # Configuracion temporal
        self.current_hotkey1 = "<Control-x>"
        self.current_hotkey2 = "<Control-d>"
        self.options = self.lang.get_value("in_out_selector")
        self.options_pos = 0
        self.label = ctk.CTkLabel(
            self,
            text="Hasta que no funcione el selector de hotkey usare:\n El selector <Control-x> para tipo de entrada.\n El selector <Control-d> para activar la aplicacion 2\n",
            font=("Roboto", 12),
        )
        self.label.grid(row=31, column=0, padx=10, pady=(10, 0), sticky="w")

        temp = self.lang.get_value("in_out_selector")[self.config.in_out_selector_pos]
        self.opciones_var1 = ctk.StringVar(value=temp)
        self.option_menu = ctk.CTkOptionMenu(
            self,
            values=self.options,
            variable=self.opciones_var1,
        )

        # self.optionmenu.set("Seleccione la deseada." if self.nooption else "Hola")
        self.option_menu.grid(row=32, column=0, padx=10, pady=(10, 0), sticky="w")

        self.bind(self.current_hotkey1, self.optionmenu_callback)
        self.bind(self.current_hotkey2, self.action_over_activation_button)

    def save_user_config(self):
        self.config.initial_language = self.lang.current_language
        self.config.save_config()

    def action_over_activation_button(self, choice):
        self.activation_switch.toggle()

    def optionmenu_callback(self, choice):
        if self.options_pos == 3:
            self.options_pos = -1
        self.options_pos += 1
        self.option_menu.set(self.options[self.options_pos])
        # Fin del bloque de configuracion temporal

    def show_message_function(self):
        self.show_message = True

    def toggle_api_visibility(self):
        pass
        # if self.api_key_entry.cget('show') == '':
        #     self.api_key_entry.configure(show='*')
        #     self.toggle_btn.configure(image=self.eye_closed_icon)
        # else:
        #     self.api_key_entry.configure(show='')
        #     self.toggle_btn.configure(image=self.eye_open_icon)

    def init_config(self):
        pass
        # image = PIL.Image.open("./src/assets/background.webp")
        # background_image = ctk.CTkImage(image, size=(800, 600))

        # self.title_label = ctk.CTkLabel(self, font=("Roboto", 20), image=background_image)
        # self.title_label.place(x=0, y=0)

    def setup_hotkey_section(self, row, column, hotkey_default):
        hotkey_label = ctk.CTkLabel(self, text=hotkey_default)
        hotkey_label.grid(row=row, column=column, padx=20, sticky="w")
        hotkey_button_text = (
            self.lang.get_value("set_hotkey_1")
            if row == 10
            else self.lang.get_value("set_hotkey_2")
        )

        self.hotkey_button = ctk.CTkButton(
            self,
            text=hotkey_button_text,
            command=self.call_hotkey1 if row == 10 else self.call_hotkey2,
        )
        self.hotkey_button.grid(
            row=row, column=column + 1, padx=10, pady=10, sticky="w"
        )

    def change_language(self, language):
        self.lang.current_language = language
        self.update_texts()

    def update_texts(self):
        self.title(self.lang.get_value("title"))
        self.registration_label.configure(
            text=self.lang.get_value("registration_label")
        )
        self.activation_switch.configure(text=self.lang.get_value("activate_app"))
        self.contact_info_label.configure(text=self.lang.get_value("contact_info"))
        # self.hotkey_button.configure(text=self.lang.get_value("set_hotkey_1"))
        self.api_key_entry.configure(placeholder_text=self.lang.get_value("apy_key"))
        self.file_extensions_entry.configure(
            placeholder_text=self.lang.get_value("apy_key")
        )

        # self.option_menu.configure(values=self.lang.get_value('in_out_selector'))
        self.save_config.configure(text=self.lang.get_value("save_config"))
        self.checkbox_continue.configure(text=self.lang.get_value("checkbox_continue"))


# funcion pendiente a implementar para la escritura de los hotkey

# key_press1 = []
# # teclas_presionadas = []
# # hotkeys = {"hotkey1": "", "hotkey2": ""}


# def get_chain_of_code(code):
#     pass
#     if code == 17:
#         if len(key_press1) >= 1 and key_press1[0] != "Control":
#             key_press1 = []
#             key_press1.append("Control")

#         # if len(key_press1) == 2 and key_press1[0] == "Control":


# class App(ctk.CTk):
#     def __init__(self):
#         super().__init__()
#         self.geometry("500x400")

#         self.button_1 = ctk.CTkButton(self, text="Hotkey 1", command=self.call_hotkey1)
#         self.button_1.grid(row=9, column=0, padx=20, pady=10, sticky="we")
# self.button_1.pack(side="top", padx=20, pady=20)

# self.button_2 = ctk.CTkButton(self, text="Hotkey 2", command=self.call_hotkey2)
# self.button_2.pack(side="top", padx=20, pady=20)

# self.button_1 = ctk.CTkButton(self, text="Hotkey 1", command=self.call_hotkey1)
# self.button_1.pack(side="top", padx=20, pady=20)

# self.button_2 = ctk.CTkButton(self, text="Hotkey 2", command=self.call_hotkey2)
# self.button_2.pack(side="top", padx=20, pady=20)


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
        self.geometry("400x120")
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


#  Antigua interfaz

"""
import customtkinter
import os
import PIL
from tkinter import simpledialog
from PIL import Image, ImageTk
import customtkinter as ctk

from src.apps.utils.translate import Translations
from src.apps.ambit import AmBit
from src.apps.utils.translate import Translate

ctk.set_appearance_mode("Dark")  # "Light" o "Dark"
ctk.set_default_color_theme("blue")


class ConfigurationInterface(customtkinter.CTk):
    def __init__(self, ambit: AmBit):
        super().__init__()
        self.option_check_1 = None
        self.option_check_1 = None
        self.AmBit = ambit
        self.title("my app")
        self.geometry("400x180")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1), weight=1)
        lang = 'es'
        self.option_check_1 = customtkinter.CTkCheckBox(
            self, text=Translate.TEXT_TO_TEXT[lang])
        self.option_check_1.grid(
            row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        self.option_check_2 = customtkinter.CTkCheckBox(
            self, text="checkbox 2")
        self.option_check_2.grid(
            row=1, column=0, padx=10, pady=(10, 0), sticky="w")

        check_var = customtkinter.StringVar(value="on")
        checkbox = customtkinter.CTkCheckBox(
            self,
            text="CTkCheckBox",
            variable=check_var, onvalue="on",
            offvalue="off")

    def create_interface(self, lang='es'):
        pass

    def button_callback(self):
        print("button pressed")

class AmbitApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.current_language = "Español"
        self.icon_path = os.getcwd() + "/src/assets/icon.png"
        # Cargar los iconos
        self.iconphoto(
            True, ImageTk.PhotoImage(file='./src/assets/icon.png'))
        self.eye_open_icon = ImageTk.PhotoImage(
            file='./src/assets/eye-open.png')
        self.eye_closed_icon = ImageTk.PhotoImage(
            file='./src/assets/eye-close.png')
        self.configure(bg='#ADD8E6')

        self.show_message = True
        self.init_ui()
        self.update_texts()

    def show_message_function(self):
        self.show_message = True

    def toggle_api_visibility(self):
        if self.api_key_entry.cget('show') == '':
            self.api_key_entry.configure(show='*')
            self.toggle_btn.configure(image=self.eye_closed_icon)
        else:
            self.api_key_entry.configure(show='')
            self.toggle_btn.configure(image=self.eye_open_icon)

    def init_ui(self):
        #image = PIL.Image.open("./src/assets/background.webp")
        #background_image = ctk.CTkImage(image, size=(800, 600))

        #self.title_label = ctk.CTkLabel(self, font=("Roboto", 20), image=background_image)
        #self.title_label.place(x=0, y=0)

        self.registration_label = ctk.CTkLabel(self)
        self.registration_label.grid(
            row=1, column=0, columnspan=2, padx=20, sticky="w")

        self.language_selector = ctk.CTkOptionMenu(
            self, values=["Español", "English"], command=self.change_language)
        self.language_selector.grid(row=2, column=0, padx=20, sticky="w")

        self.api_key_entry = ctk.CTkEntry(
            self,
            show='*',
            width=400,
            placeholder_text=Translations['apy_key'][self.current_language])
        self.api_key_entry.grid(
            row=3, column=0, padx=20, pady=20, sticky="w")

        self.toggle_btn = ctk.CTkButton(
            self,
            text='',
            width=30,
            image=self.eye_closed_icon,
            command=self.toggle_api_visibility)

        self.toggle_btn.grid(row=3, column=1, padx=0, pady=0, sticky="W")

        self.file_extensions_entry = ctk.CTkEntry(self)
        self.file_extensions_entry.configure(
            placeholder_text=Translations["apy_key"][self.current_language],
            placeholder_text_color='red',
            width=15
        )
        self.file_extensions_entry.insert(
            0, ".doc, .txt, .py, .php, .html, .cs, .exe, .css")
        self.file_extensions_entry.grid(
            row=9, column=0, padx=20, pady=10, sticky="we")

        self.setup_hotkey_section(
            row=10, column=0,
            hotkey_default=Translations[
                "hotkey_1_default"][self.current_language])
        self.setup_hotkey_section(
            row=11, column=0,
            hotkey_default=Translations[
                "hotkey_2_default"][self.current_language])

        self.activation_switch = ctk.CTkSwitch(self)
        self.activation_switch.grid(
            row=13, column=0, padx=20, pady=10, sticky="w")

        self.contact_info_label = ctk.CTkLabel(self)
        self.contact_info_label.grid(
            row=14, column=0, padx=20, pady=10, sticky="w", columnspan=3)

    def setup_hotkey_section(self, row, column, hotkey_default):
        hotkey_label = ctk.CTkLabel(self, text=hotkey_default)
        hotkey_label.grid(row=row, column=column, padx=20, sticky="w")

        hotkey_button_text = Translations["set_hotkey_1"][
            self.current_language
        ] if row == 10 else Translations["set_hotkey_2"][self.current_language]

        self.hotkey_button = ctk.CTkButton(
            self, text=hotkey_button_text,
            command=lambda: self.set_hotkey(hotkey_label)
        )
        self.hotkey_button.grid(
            row=row, column=column + 1, padx=10, sticky="w")

    def set_hotkey(self, label_widget):
        hotkey = simpledialog.askstring(
            Translations["HotKey_title_text"][self.current_language],
            Translations["HotKey_text"][self.current_language]
        )
        if hotkey:
            label_widget.configure(text=hotkey)

    def change_language(self, language):
        self.current_language = language
        self.update_texts()

    def update_texts(self):
        self.title(Translations["title"][self.current_language])
        self.registration_label.configure(
            text=Translations["registration_label"][self.current_language])
        self.activation_switch.configure(
            text=Translations["activate_app"][self.current_language])
        self.contact_info_label.configure(
            text=Translations["contact_info"][self.current_language])
        self.hotkey_button.configure(
            text=Translations["set_hotkey_1"][self.current_language])
        self.api_key_entry.configure(
            placeholder_text=Translations['apy_key'][self.current_language])
"""
