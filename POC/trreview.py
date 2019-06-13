"""
name:
date:
description
"""
import tkinter as tk
import ttk
root = tk.Tk()
table = ttk.Treeview(root, columns=('A', ), style="mystyle.Treeview", selectmode='browse')
table.place(relx=0, rely=0, relheight=1, relwidth=1)

table.heading("#0", text="program name")
table.column("#0", width=100)

table.heading("A", text="username")
table.column("A", width=100)

root.mainloop()