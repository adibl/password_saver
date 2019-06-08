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


class LoginGui(UsernamePasswordGui):

    def __init__(self, parent):
        super(LoginGui, self).__init__(parent)

        self.Button1 = tk.Button(self)
        self.Button1.place(relx=0.4, rely=0.845, relheight=self._HIGH_ALL, relwidth=0.2)
        self.Button1.configure(command=self.run)
        self.Button1.configure(text='''Log in''')

        self.Button2 = tk.Button(self)
        self.Button2.place(relx=0.7, rely=0.845, relheight=self._HIGH_ALL, relwidth=0.2)
        self.Button2.configure(command=self.to_register)
        self.Button2.configure(text='''Register''')

        self.Button3 = tk.Button(self)
        self.Button3.place(relx=0.1, rely=0.845, relheight=self._HIGH_ALL, relwidth=0.2)
        self.Button3.configure(command=self.to_forgot_password)
        self.Button3.configure(text='''forget password''')

        self.bind("<Escape>", self.run)
