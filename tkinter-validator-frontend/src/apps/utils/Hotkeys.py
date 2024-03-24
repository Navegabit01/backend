import customtkinter as ctk
from tkinter import messagebox


hotkey_2_default = "Control + Shift + x"
new_hk = []


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
        print(self.miconfig.get_hotkey1())

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


class HotkeyValidator:
    def __init__(self):
        self.lst = []

    def set_lst(self, lst):
        self.lst = lst

    def get_lst(self):
        return self.lst

    def max_three_elements_in_list(self):
        self.lst = self.lst[::-1][0:3][::-1]

    def exist_ctrl(self):
        return True if "Control_L" or "Control_R" in self.lst else False

    def exist_shift(self):
        return True if "Shift_L" or "Shift_R" in self.lst else False

    def shift_after_ctrl(self):
        ctrl_pos = 0
        shift_pos = 0
        if self.exist_ctrl() and self.exist_shift():
            for pos, elm in enumerate(self.lst):
                if self.is_ctrl(elm):
                    ctrl_pos = pos
                elif self.is_shift(elm):
                    shift_pos = pos
            return shift_pos > ctrl_pos
        return False

    def is_a_function_key(self, key):
        return key in ["F" + str(x) for x in range(1, 13)]

    def is_ctrl(self, elm):
        return True if elm == "Control_L" or elm == "Control_R" else False

    def is_shift(self, elm):
        return True if elm == "Shift_L" or elm == "Shift_R" else False

    def is_alt(self, elm):
        return True if elm == "Alt_L" or elm == "Alt_R" else False

    def number_or_char_and_not_functions_keys(self, key):
        return not self.is_a_function_key(key) and key.isalnum()

    # Rules
    def between_two_and_three(self):
        return len(self.lst) >= 2 and len(self.lst) < 4

    # rules of three
    def ctr_shift_letter(self):
        if (
            len(self.lst) == 3
            and self.is_ctrl(self.lst[0])
            and self.is_shift(self.lst[1])
            and self.lst[2].isalpha()
        ):
            return True

    def ctr_alt_num(self):
        return (
            len(self.lst) == 3
            and self.is_ctrl(self.lst[0])
            and self.is_alt(self.lst[1])
            and self.lst[2].isdigit()
        )

    def alnum_shift_letter(self):
        return (
            len(self.lst) == 3
            and self.lst[0].isalnum()
            and self.is_shift(self.lst[1])
            and self.lst[2].isalpha()
        )

    def shift_letter_alnum(self):
        return (
            len(self.lst) == 3
            and self.is_shift(self.lst[1])
            and self.lst[2].isalpha()
            and self.lst[0].isalnum()
        )

    def alnum_ctrl_alnum(self):
        return (
            len(self.lst) == 3
            and self.lst[0].isalnum()
            and self.is_ctrl(self.lst[1])
            and self.lst[2].isalnum()
        )

    def alnum_alt_alnum(self):
        return (
            len(self.lst) == 3
            and self.lst[0].isalnum()
            and self.is_alt(self.lst[1])
            and self.lst[2].isalnum()
        )

    def three_alnum(self):
        return (
            len(self.lst) == 3 and self.all_elm_len_three() and self.all_are_alphanum()
        )

    def all_are_alphanum(self):
        for x in self.lst:
            if not x.isalpha():
                return False
        return True

    # end rule of three

    # Rules of two
    def ctrl_alnum(self):
        return (
            len(self.lst) == 2 and self.is_ctrl(self.lst[0]) and self.lst[1].isalnum()
        )

    def shift_alpha(self):
        return (
            len(self.lst) == 2 and self.is_shift(self.lst[0]) and self.lst[1].isalpha()
        )

    # end rule of two
    def valid_hotkey_secuence(self):
        if self.ctr_shift_letter():
            return True
        if self.ctr_alt_num():
            return True
        if self.alnum_shift_letter():
            return True
        if self.alnum_ctrl_alnum():
            return True
        if self.alnum_alt_alnum():
            return True
        if self.three_alnum():
            return True
        if self.all_are_alphanum():
            return True
        if self.ctrl_alnum():
            return True
        if self.shift_alpha():
            return True
        if self.shift_letter_alnum():
            return True
        return False

    def all_elm_len_three(self):
        for x in self.lst:
            if len(x) > 1:
                return False
        return True

    def remove_lower_case(self, schar):
        if self.is_alt(schar) or self.is_ctrl(schar) or self.is_shift(schar):
            return schar.split("_")[0]
        return schar

    def config_to_load(self, hotkey):
        res = []
        for x in hotkey:
            if x == "<" or x == ">":
                continue
            res.append(x)
        res = "".join(res)
        res = res.split("-")
        res = "  +  ".join(res)
        return res

    def is_a_function_key(self, key):
        return key in ["F" + str(i + 1) for i in range(12)]

    def create_hotkey_to_main(self):
        return "<" + "-".join(self.lst) + ">"

    def configure_key_press(self, key_lst):
        self.set_lst(key_lst)
        self.max_three_elements_in_list()
        return [self.remove_lower_case(x) for x in self.get_lst()]
