import tkinter as tk
from tkinter import messagebox

class Node:
    def __init__(self, value):
        self.value = value  # Menyimpan nilai digit
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return

        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if not current.left:
                current.left = new_node
                return
            else:
                queue.append(current.left)

            if not current.right:
                current.right = new_node
                return
            else:
                queue.append(current.right)

    def preorder_traversal(self, node, result):
        if node:
            result.append(node.value)
            self.preorder_traversal(node.left, result)
            self.preorder_traversal(node.right, result)

    def inorder_traversal(self, node, result):
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.value)
            self.inorder_traversal(node.right, result)

    def postorder_traversal(self, node, result):
        if node:
            self.postorder_traversal(node.left, result)
            self.postorder_traversal(node.right, result)
            result.append(node.value)

    def count_odd_digits(self, node):
        if not node:
            return 0
        count = 1 if int(node.value) % 2 != 0 else 0
        count += self.count_odd_digits(node.left)
        count += self.count_odd_digits(node.right)
        return count

def insert_npm():
    npm = entry_npm.get()
    if not npm.isdigit():
        messagebox.showerror("Error", "NPM harus berupa angka.")
        return

    global bt
    bt = BinaryTree()
    for digit in npm:
        bt.insert(digit)

    # Update hasil traversal secara otomatis setelah NPM dimasukkan
    update_traversal()

    # Gambar pohon biner
    draw_tree()

def update_traversal():
    if not bt or not bt.root:
        return

    global result

    # Preorder
    result = []
    bt.preorder_traversal(bt.root, result)
    preorder_result.set("".join(result))

    # Inorder
    result = []
    bt.inorder_traversal(bt.root, result)
    inorder_result.set("".join(result))

    # Postorder
    result = []
    bt.postorder_traversal(bt.root, result)
    postorder_result.set("".join(result))

def count_odd():
    if not bt or not bt.root:
        messagebox.showerror("Error", "Masukkan NPM terlebih dahulu.")
        return

    odd_count = bt.count_odd_digits(bt.root)
    odd_count_result.set(str(odd_count))

def draw_tree():
    canvas.delete("all")
    if bt and bt.root:
        draw_node(bt.root, 400, 50, 200)

def draw_node(node, x, y, x_offset):
    if node:
        # Gambar node (lingkaran dengan isi nilai)
        canvas.create_oval(x-20, y-20, x+20, y+20, fill="lightblue")
        canvas.create_text(x, y, text=node.value, font=("Arial", 12, "bold"))

        if node.left:
            canvas.create_line(x, y+20, x-x_offset, y+100, arrow=tk.LAST)
            draw_node(node.left, x-x_offset, y+100, x_offset//2)

        if node.right:
            canvas.create_line(x, y+20, x+x_offset, y+100, arrow=tk.LAST)
            draw_node(node.right, x+x_offset, y+100, x_offset//2)

# GUI Setup
root = tk.Tk()
root.title("Binary Tree NPM")

# Input NPM
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

label_npm = tk.Label(frame_input, text="Masukkan NPM:")
label_npm.pack(side=tk.LEFT, padx=5)

entry_npm = tk.Entry(frame_input)
entry_npm.pack(side=tk.LEFT, padx=5)

button_insert = tk.Button(frame_input, text="Masukkan", command=insert_npm)
button_insert.pack(side=tk.LEFT, padx=5)

# Traversal Results
frame_traversal = tk.Frame(root)
frame_traversal.pack(pady=10)

preorder_result = tk.StringVar()
inorder_result = tk.StringVar()
postorder_result = tk.StringVar()

label_preorder = tk.Label(frame_traversal, text="Preorder: ")
label_preorder.grid(row=0, column=0, sticky=tk.W)
entry_preorder = tk.Entry(frame_traversal, textvariable=preorder_result, state="readonly")
entry_preorder.grid(row=0, column=1)

label_inorder = tk.Label(frame_traversal, text="Inorder: ")
label_inorder.grid(row=1, column=0, sticky=tk.W)
entry_inorder = tk.Entry(frame_traversal, textvariable=inorder_result, state="readonly")
entry_inorder.grid(row=1, column=1)

label_postorder = tk.Label(frame_traversal, text="Postorder: ")
label_postorder.grid(row=2, column=0, sticky=tk.W)
entry_postorder = tk.Entry(frame_traversal, textvariable=postorder_result, state="readonly")
entry_postorder.grid(row=2, column=1)

# Odd Digit Count
frame_odd = tk.Frame(root)
frame_odd.pack(pady=10)

odd_count_result = tk.StringVar()

label_odd = tk.Label(frame_odd, text="Jumlah Digit Ganjil: ")
label_odd.pack(side=tk.LEFT, padx=5)
entry_odd = tk.Entry(frame_odd, textvariable=odd_count_result, state="readonly")
entry_odd.pack(side=tk.LEFT, padx=5)

button_count_odd = tk.Button(frame_odd, text="Hitung Digit Ganjil", command=count_odd)
button_count_odd.pack(side=tk.LEFT, padx=5)

# Canvas for Tree Visualization
canvas = tk.Canvas(root, width=800, height=400, bg="white")
canvas.pack(pady=20)

# Run the application
root.mainloop()
