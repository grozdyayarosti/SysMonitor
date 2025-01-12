import tkinter as tk
from tkinter import messagebox


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Калькулятор индекса массы тела (ИМТ)')
        self.geometry('400x300')
        self.resizable(width=False, height=False)

        self.init_frame()

        self.height_label = None
        self.init_height_label()
        self.weight_label = None
        self.init_weight_label()

        self.height_tf = None
        self.init_height_tf()
        self.weight_tf = None
        self.init_weight_tf()

        self.init_button()

    def init_frame(self):
        self.frame = tk.Frame(
            self,
            padx=10,
            pady=10
        )
        self.frame.pack(expand=True)

    def init_height_label(self):
        self.height_label = tk.Label(
            self.frame,
            text="Введите свой рост (в см)  "
        )
        self.height_label.grid(row=3, column=1)

    def init_weight_label(self):
        self.weight_label = tk.Label(
            self.frame,
            text="Введите свой вес (в кг)  ",
        )
        self.weight_label.grid(row=4, column=1)

    def init_height_tf(self):
        self.height_tf = tk.Entry(self.frame)
        self.height_tf.grid(row=3, column=2, pady=5)

    def init_weight_tf(self):
        self.weight_tf = tk.Entry(self.frame)
        self.weight_tf.grid(row=4, column=2, pady=5)

    def init_button(self):
        cal_btn = tk.Button(
            self.frame,
            text='Рассчитать ИМТ',
            command=self.calculate_bmi
        )
        cal_btn.grid(row=5, column=2)

    def calculate_bmi(self):
        kg = int(self.weight_tf.get())
        m = int(self.height_tf.get()) / 100
        bmi = kg / (m * m)
        bmi = round(bmi, 1)

        if bmi < 18.5:
            messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует недостаточному весу')
        elif (bmi > 18.5) and (bmi < 24.9):
            messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует нормальному весу')
        elif (bmi > 24.9) and (bmi < 29.9):
            messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует избыточному весу')
        else:
            messagebox.showinfo('bmi-pythonguides', f'ИМТ = {bmi} соответствует ожирению')


app = MainWindow()
app.mainloop()