"""
name:
date:
description
"""
import tkinter as tk

class GenerateGui(tk.Tk):
    _RELX_ENTITY = 0.25
    _WITH_ENTITY = 0.7
    _HIGH_ALL = 0.07
    _WITH_LABLE = 0.15
    _RELX_LABLE = 0.05
    _AFTER_ENTITY_RELX = _RELX_ENTITY + _WITH_ENTITY

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("500x500")

        self.Label1 = tk.Label(self)
        self.Label1.place(relx=self._RELX_LABLE, rely=0.056, relheight=self._HIGH_ALL, relwidth=self._WITH_LABLE)
        self.Label1.configure(font="-family {Segoe UI} -size 12")
        self.Label1.configure(anchor='w')
        self.Label1.configure(text='''Username''')

        self.entry_username = tk.Entry(self)
        self.entry_username.place(relx=self._RELX_ENTITY, rely=0.056, relheight=self._HIGH_ALL,
                                  relwidth=self._WITH_ENTITY)
        self.entry_username.configure(font="-family {Courier New} -size 12")

        self.Label2 = tk.Label(self)
        self.Label2.place(relx=self._RELX_LABLE, rely=0.225, relheight=self._HIGH_ALL, relwidth=self._WITH_LABLE)
        self.Label2.configure(anchor='w')
        self.Label2.configure(font="-family {Segoe UI} -size 12")
        self.Label2.configure(text='''Password''')

        self.entry_password = tk.Entry(self)
        self.entry_password.place(relx=self._RELX_ENTITY, rely=0.225, relheight=self._HIGH_ALL,
                                  relwidth=self._WITH_ENTITY)
        self.entry_password.configure(font="-family {Courier New} -size 12")

        self.Button1 = tk.Button(self)
        self.Button1.place(relx=0.4, rely=0.845, relheight=self._HIGH_ALL, relwidth=0.2)
        self.Button1.configure(command=self.quit)
        self.Button1.configure(text='''Finish''')

        self.label_general_error = tk.Label(self)
        self.label_general_error.place(relx=self._RELX_ENTITY, rely=0.31, relheight=self._HIGH_ALL * 2
                                        , relwidth=self._WITH_ENTITY)
        self.label_general_error.configure(foreground="#ff1f1f")

        self.Button1 = tk.Button(self)
        self.Button1.place(relx=self._AFTER_ENTITY_RELX, rely=0.225, relheight=self._HIGH_ALL, relwidth=0.2)
        self.Button1.configure(command=self.auto_generate)
        self.Button1.configure(text='''Auto Generate Password''')


    def auto_generate(self):
        self.entry_password.insert(0, self.generate_strong_password())


    def generate_strong_password(self):
        return 'Qazwsx12#' #TODO: