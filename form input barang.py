import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Fungsi untuk menambahkan data barang ke Treeview
def add_item():
    kode = entry_kode.get().strip()
    nama = entry_nama.get().strip()
    harga = entry_harga.get().strip()
    stock = entry_stock.get().strip()

    if not kode or not nama or not harga or not stock:
        messagebox.showerror("Error", "Semua field harus diisi!")
        return

    if not harga.isdigit() or not stock.isdigit():
        messagebox.showerror("Error", "Harga dan stock harus berupa angka!")
        return

    for row in tree.get_children():
        if tree.item(row, "values")[0] == kode:
            messagebox.showerror("Error", "Kode barang sudah ada!")
            return

    # Menambahkan data ke Treeview
    tree.insert("", "end", values=(kode, nama, harga, stock))
    clear_entries()

# Fungsi untuk menghapus data barang dari Treeview
def delete_item():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "Pilih data yang ingin dihapus!")
        return

    for item in selected_item:
        tree.delete(item)

# Fungsi untuk membersihkan field input
def clear_entries():
    entry_kode.delete(0, tk.END)
    entry_nama.delete(0, tk.END)
    entry_harga.delete(0, tk.END)
    entry_stock.delete(0, tk.END)

# Membuat GUI
root = tk.Tk()
root.title("Form Input Data Barang")
root.geometry("600x400")

# Frame untuk form input
frame_input = tk.Frame(root, padx=10, pady=10)
frame_input.pack(fill="x")

tk.Label(frame_input, text="Kode Barang:").grid(row=0, column=0, pady=5, sticky="w")
entry_kode = tk.Entry(frame_input)
entry_kode.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Nama Barang:").grid(row=1, column=0, pady=5, sticky="w")
entry_nama = tk.Entry(frame_input)
entry_nama.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Harga Barang:").grid(row=2, column=0, pady=5, sticky="w")
entry_harga = tk.Entry(frame_input)
entry_harga.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Stock Barang:").grid(row=3, column=0, pady=5, sticky="w")
entry_stock = tk.Entry(frame_input)
entry_stock.grid(row=3, column=1, padx=5, pady=5)

# Tombol untuk menambah dan menghapus
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

btn_add = tk.Button(frame_buttons, text="Tambah", command=add_item, width=15)
btn_add.grid(row=0, column=0, padx=5, pady=5)

btn_delete = tk.Button(frame_buttons, text="Hapus", command=delete_item, width=15)
btn_delete.grid(row=0, column=1, padx=5, pady=5)

# Treeview untuk menampilkan data barang
frame_tree = tk.Frame(root)
frame_tree.pack(pady=10)

columns = ("Kode", "Nama", "Harga", "Stock")
tree = ttk.Treeview(frame_tree, columns=columns, show="headings", height=10)
tree.heading("Kode", text="Kode Barang")
tree.heading("Nama", text="Nama Barang")
tree.heading("Harga", text="Harga Barang")
tree.heading("Stock", text="Stock Barang")

for col in columns:
    tree.column(col, anchor="w", width=120)

tree.pack(side="left", fill="both", expand=True)

# Scrollbar untuk Treeview
scrollbar = ttk.Scrollbar(frame_tree, orient="vertical", command=tree.yview)
scrollbar.pack(side="right", fill="y")
tree.configure(yscrollcommand=scrollbar.set)

# Menjalankan aplikasi
root.mainloop()
