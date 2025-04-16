import tkinter as tk

class kalkulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator")

        self.angka = tk.StringVar()
        self.operasi = ""
        self.history = []

        layar = tk.Entry(root, textvariable=self.angka, font=('Helvetica', 16), justify='right', bd=10)
        layar.grid(row=0, column=0, columnspan=4)

        tombol = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C', 'x²', '√', 'H'
        ]

        row_val = 1
        col_val = 0
        for button in tombol:
            tk.Button(root, text=button, padx=20, pady=20, font=('Helvetica', 14), command=lambda b=button: self.tekan_tombol(b)).grid(row=row_val, column=col_val, sticky='nsew')
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
        for i in range(row_val):
            root.grid_rowconfigure(i, weight=1)

        self.history_frame = tk.Frame(root, bd=10, relief='sunken')
        self.history_frame.grid(row=row_val, column=0, columnspan=4, sticky='nsew')
        self.history_label = tk.Label(self.history_frame, text="History", anchor='w', justify='left', font=('Helvetica', 12))
        self.history_label.pack(fill='both', expand=True)

    def tekan_tombol(self, tombol):
        if tombol == '=':
            self.hitung_hasil()
        elif tombol == 'C':
            self.angka.set('')
        elif tombol == 'x²':
            try:
                current_value = float(self.angka.get())
                self.angka.set(current_value ** 2)
                self.tambah_history(f"{current_value}^2 = {hasil}")
                self.angka.set(hasil)
            except Exception as e:
                self.angka.set("Error")
        elif tombol == '√':
            try:
                current_value = float(self.angka.get())
                if current_value < 0:
                    self.angka.set("Error")
                else:
                    hasil = current_value ** 0.5
                    self.tambah_history(f"√{current_value} = {hasil}")
                    self.angka.set(hasil)
            except Exception as e:
                self.angka.set("Error")
        elif tombol == 'H':
            self.tampilkan_history()
        else:
            current_value = self.angka.get()
            new_value = current_value + tombol
            self.angka.set(new_value)

    def hitung_hasil(self):
        try:
            ekspresi = self.angka.get()
            hasil = eval(ekspresi)
            self.tambah_history(f"{ekspresi} = {hasil}")
            self.angka.set(hasil)
        except Exception as e:
            self.angka.set("Error")

    def tambah_history(self, item):
        self.history.append(item)
        if len(self.history) > 10:
            self.history.pop(0)
        self.tampilkan_history()

    def tampilkan_history(self):
        history_text ="\n".join(self.history)
        self.history_label.config(text=history_text)
    
if __name__== "__main__":
    root = tk.Tk()
    app = kalkulator(root)
    root.mainloop()
