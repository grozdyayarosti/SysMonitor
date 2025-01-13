import tkinter as tk
from tkinter import messagebox
import os

from system_calculation import SystemCalculation


# import SystemCalculation


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Системный монитор')
        self.geometry('800x600')
        self.resizable(width=False, height=False)

        self.init_frame()

        self.cpu_label = None
        self.init_cpu_value_label()

        self.ram_label = None
        self.init_ram_value_label()

        self.rom_label = None
        self.init_rom_value_label()

        # self.init_button()

    def init_frame(self):
        self.frame = tk.Frame(
            self,
            padx=10,
            pady=10
        )
        self.frame.pack(expand=True)

    def init_cpu_value_label(self):
        cpu_value = SystemCalculation().get_cpu()
        self.cpu_label = tk.Label(
            self.frame,
            text=f"CPU: {cpu_value}"
        )
        self.cpu_label.grid(row=3, column=1)

    def init_ram_value_label(self):
        ram_value = SystemCalculation().get_ram()
        self.ram_label = tk.Label(
            self.frame,
            text=f"RAM: {ram_value}"
        )
        self.ram_label.grid(row=4, column=1)

    def init_rom_value_label(self):
        rom_value = SystemCalculation().get_rom()
        self.ram_label = tk.Label(
            self.frame,
            text=f"ROM: {rom_value}"
        )
        self.ram_label.grid(row=5, column=1)

    # def init_button(self):
    #     cal_btn = tk.Button(
    #         self.frame,
    #         text='Рассчитать ИМТ',
    #         # command=
    #     )
    #     cal_btn.grid(row=5, column=2)

app = MainWindow()
app.mainloop()