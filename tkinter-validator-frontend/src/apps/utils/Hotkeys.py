import customtkinter as ctk
from tkinter import messagebox

hotkey_2_default = "Control + Shift + x"
functional = ["F" + str(i + 1) for i in range(12)]
new_hk = []


# Informational alert
# messagebox.showinfo("Title", "This is an informational alert.")

# # Warning alert
# messagebox.showwarning("Warning", "This is a warning alert.")

# # Error alert
# messagebox.showerror("Error", "This is an error alert.")

# Tab
# BackSpace
# Alt_R
# Alt_L


def max_three_elements_in_list(lst):
    return lst[::-1][0:3][::-1]


def exist_ctrl(lst):
    return True if "Control_L" or "Control_R" in lst else False


def exist_shift(lst):
    return True if "Shift_L" or "Shift_R" in lst else False


def shift_after_ctrl(lst):
    ctrl_pos = 0
    shift_pos = 0
    if exist_ctrl(lst) and exist_shift(lst):
        for pos, elm in enumerate(lst):
            if is_ctrl(elm):
                ctrl_pos = pos
            elif is_shift(elm):
                shift_pos = pos
        return shift_pos > ctrl_pos
    return False


def is_a_function_key(key):
    return key in ["F" + str(x) for x in range(1, 13)]


def is_ctrl(elm):
    return True if elm == "Control_L" or elm == "Control_R" else False


def is_shift(elm):
    return True if elm == "Shift_L" or elm == "Shift_R" else False


def is_alt(elm):
    return True if elm == "Alt_L" or elm == "Alt_R" else False


def number_or_char_and_not_functions_keys(key):
    return not is_a_function_key(key) and key.isalnum()


# Rules
def between_two_and_three(lst):
    return len(lst) >= 2 and len(lst) < 4


# rules of three
def ctr_shift_letter(lst):
    return len(lst) == 3 and is_ctrl(lst[0]) and is_shift(lst[1]) and lst[2].isalpha()


def ctr_alt_num(lst):
    return len(lst) == 3 and is_ctrl(lst[0]) and is_alt(lst[1]) and lst[2].isdigit()


def alnum_shift_letter(lst):
    return len(lst) == 3 and lst[0].isalnum() and is_shift(lst[1]) and lst[2].isalpha()


def shift_letter_alnum(lst):
    return len(lst) == 3 and is_shift(lst[1]) and lst[2].isalpha() and lst[0].isalnum()


def alnum_ctrl_alnum(lst):
    return len(lst) == 3 and lst[0].isalnum() and is_ctrl(lst[1]) and lst[2].isalnum()


def alnum_alt_alnum(lst):
    return len(lst) == 3 and lst[0].isalnum() and is_alt(lst[1]) and lst[2].isalnum()


def three_alnum(lst):
    return len(lst) == 3 and all_elm_len_three(lst) and all_are_alphanum(lst)


def all_are_alphanum(lst):
    for x in lst:
        if not x.isalpha():
            return False
    return True


# end rule of three


# Rules of two
def ctrl_alnum(lst):
    return len(lst) == 2 and is_ctrl(lst[0]) and lst[1].isalnum()


def shift_alpha(lst):
    return len(lst) == 2 and is_shift(lst[0]) and lst[1].isalpha()


# end rule of two


# Clean Ok Hotkey
def create_hotkey(lst):
    new_list = []
    for x in lst:
        if is_ctrl(x) or is_alt(x) or is_shift(x):
            temp = x.split("_")[0]
            new_hk.append(temp)
        else:
            new_list.append(x)
    return "   +   ".join(new_list)


def valid_hotkey_secuence(lst):
    if ctr_shift_letter(lst):
        return True
    if ctr_alt_num(lst):
        return True
    if alnum_shift_letter(lst):
        return True
    if alnum_ctrl_alnum(lst):
        return True
    if alnum_alt_alnum(lst):
        return True
    if three_alnum(lst):
        return True
    if all_are_alphanum(lst):
        return True
    if ctrl_alnum(lst):
        return True
    if shift_alpha(lst):
        return True
    if shift_letter_alnum(lst):
        return True
    return False


def all_elm_len_three(lst):
    for x in lst:
        if len(x) > 1:
            return False
    return True


class Hotkey1(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Hotkey no_1")
        self.geometry("350x120")
        self.resizable(False, False)
        self.hotkey_1_default = "Control + Shift + x"
        self.label = ctk.CTkLabel(
            self,
            text="Introduzca el atajo de teclado deseado:\n\n" + "Ctrl + Shift + l",
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

    def save_hotkey_conf(self):
        global new_hk
        if not valid_hotkey_secuence(new_hk):
            messagebox.showerror(
                "Combinacion incorrecta", "La combinacion de teclas no es correcta."
            )
            self.label.configure(
                text=f"Introduzca el atajo de teclado deseado: \n\n{self.hotkey_1_default}"
            )
        else:
            self.destroy()

    def close_window(self):
        self.destroy()

    def on_key_press(self, evt):
        global new_hk
        new_hk.append(evt.keysym)
        new_hk = max_three_elements_in_list(new_hk)
        res = ""
        if len(new_hk) > 1:
            res = "   +   ".join(new_hk)
        elif len(new_hk) == 1:
            res = new_hk[0]
        self.label.configure(
            text=f"Introduzca el atajo de teclado deseado: \n\n{res if len(res) >= 1 else self.hotkey_1_default}"
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
        self.label.configure(text=f"Tecla presionada:  \n{event.keysym}")
