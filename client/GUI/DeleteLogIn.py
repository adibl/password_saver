"""
name:
date:
description
"""
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
from .Gui import Gui
from .UsernamePasswordGui import UsernamePasswordGui


class DeleteLoginGui(UsernamePasswordGui):

    def __init__(self, parent):
        super(DeleteLoginGui, self).__init__(parent)

        self.Button1 = tk.Button(self)
        self.Button1.place(relx=0.4, rely=0.845, relheight=self._HIGH_ALL, relwidth=0.2)
        self.Button1.configure(command=self.run)
        self.Button1.configure(text='''delete account''')