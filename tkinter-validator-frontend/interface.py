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


class ConfigurationInterface:
    def __init__(self, ambit: AmBit):
        super().__init__()
        self.option_check_1 = None
        self.option_check_1 = None
        self.AmBit = ambit
        self.title("my app")
        self.geometry("400x180")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1), weight=1)
        lang = "es"
        self.option_check_1 = customtkinter.CTkCheckBox(
            self, text=Translate.TEXT_TO_TEXT[lang]
        )
        self.option_check_1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        self.option_check_2 = customtkinter.CTkCheckBox(self, text="checkbox 2")
        self.option_check_2.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")

        check_var = customtkinter.StringVar(value="on")
        checkbox = customtkinter.CTkCheckBox(
            self, text="CTkCheckBox", variable=check_var, onvalue="on", offvalue="off"
        )

    def create_interface(self, lang="es"):
        pass

    def button_callback(self):
        print("button pressed")


class AmbitApp:
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.current_language = "Español"
        self.icon_path = os.getcwd() + "/src/assets/icon.png"
        # Cargar los iconos
        self.iconphoto(True, ImageTk.PhotoImage(file="./src/assets/icon.png"))
        self.eye_open_icon = ImageTk.PhotoImage(file="./src/assets/eye-open.png")
        self.eye_closed_icon = ImageTk.PhotoImage(file="./src/assets/eye-close.png")
        self.configure(bg="#ADD8E6")

        self.show_message = True
        self.init_ui()
        self.update_texts()

    def show_message_function(self):
        self.show_message = True

    def toggle_api_visibility(self):
        if self.api_key_entry.cget("show") == "":
            self.api_key_entry.configure(show="*")
            self.toggle_btn.configure(image=self.eye_closed_icon)
        else:
            self.api_key_entry.configure(show="")
            self.toggle_btn.configure(image=self.eye_open_icon)

    def init_ui(self):
        image = PIL.Image.open("./src/assets/background.webp")
        background_image = ctk.CTkImage(image, size=(800, 600))

        self.title_label = ctk.CTkLabel(
            self, font=("Roboto", 20), image=background_image
        )
        self.title_label.place(x=0, y=0)

        self.registration_label = ctk.CTkLabel(self)
        self.registration_label.grid(row=1, column=0, columnspan=2, padx=20, sticky="w")

        self.language_selector = ctk.CTkOptionMenu(
            self, values=["Español", "English"], command=self.change_language
        )
        self.language_selector.grid(row=2, column=0, padx=20, sticky="w")

        self.api_key_entry = ctk.CTkEntry(
            self,
            show="*",
            width=400,
            placeholder_text=Translations["apy_key"][self.current_language],
        )
        self.api_key_entry.grid(row=3, column=0, padx=20, pady=20, sticky="w")

        self.toggle_btn = ctk.CTkButton(
            self,
            text="",
            width=30,
            image=self.eye_closed_icon,
            command=self.toggle_api_visibility,
        )

        self.toggle_btn.grid(row=3, column=1, padx=0, pady=0, sticky="W")

        self.file_extensions_entry = ctk.CTkEntry(self)
        self.file_extensions_entry.configure(
            placeholder_text=Translations["apy_key"][self.current_language],
            placeholder_text_color="red",
            width=15,
        )
        self.file_extensions_entry.insert(
            0, ".doc, .txt, .py, .php, .html, .cs, .exe, .css"
        )
        self.file_extensions_entry.grid(row=9, column=0, padx=20, pady=10, sticky="we")

        self.setup_hotkey_section(
            row=10,
            column=0,
            hotkey_default=Translations["hotkey_1_default"][self.current_language],
        )
        self.setup_hotkey_section(
            row=11,
            column=0,
            hotkey_default=Translations["hotkey_2_default"][self.current_language],
        )

        self.activation_switch = ctk.CTkSwitch(self)
        self.activation_switch.grid(row=13, column=0, padx=20, pady=10, sticky="w")

        self.contact_info_label = ctk.CTkLabel(self)
        self.contact_info_label.grid(
            row=14, column=0, padx=20, pady=10, sticky="w", columnspan=3
        )

    def setup_hotkey_section(self, row, column, hotkey_default):
        hotkey_label = ctk.CTkLabel(self, text=hotkey_default)
        hotkey_label.grid(row=row, column=column, padx=20, sticky="w")

        hotkey_button_text = (
            Translations["set_hotkey_1"][self.current_language]
            if row == 10
            else Translations["set_hotkey_2"][self.current_language]
        )

        self.hotkey_button = ctk.CTkButton(
            self, text=hotkey_button_text, command=lambda: self.set_hotkey(hotkey_label)
        )
        self.hotkey_button.grid(row=row, column=column + 1, padx=10, sticky="w")

    def set_hotkey(self, label_widget):
        hotkey = simpledialog.askstring(
            Translations["HotKey_title_text"][self.current_language],
            Translations["HotKey_text"][self.current_language],
        )
        if hotkey:
            label_widget.configure(text=hotkey)

    def change_language(self, language):
        self.current_language = language
        self.update_texts()

    def update_texts(self):
        self.title(Translations["title"][self.current_language])
        self.registration_label.configure(
            text=Translations["registration_label"][self.current_language]
        )
        self.activation_switch.configure(
            text=Translations["activate_app"][self.current_language]
        )
        self.contact_info_label.configure(
            text=Translations["contact_info"][self.current_language]
        )
        self.hotkey_button.configure(
            text=Translations["set_hotkey_1"][self.current_language]
        )
        self.api_key_entry.configure(
            placeholder_text=Translations["apy_key"][self.current_language]
        )
