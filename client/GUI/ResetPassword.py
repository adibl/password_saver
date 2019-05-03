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


class ResetPasswordGui(Gui):
    _RELX_ENTITY = 0.25
    _WITH_ENTITY = 0.7
    _HIGH_ALL = 0.07
    _WITH_LABLE = 0.15
    _RELX_LABLE = 0.05

    def __init__(self, parent):
        super(ResetPasswordGui, self).__init__(parent)
        self.place(relx=0.0, rely=0.0, relheight=1, relwidth=1)
        self.configure(width=455)

        self.Label1 = tk.Label(self)
        self.Label1.place(relx=self._RELX_LABLE, rely=0.056, relheight=self._HIGH_ALL, relwidth=self._WITH_LABLE)
        self.Label1.configure(font="-family {Segoe UI} -size 12")
        self.Label1.configure(anchor='w')
        self.Label1.configure(text='''qestion''')

        self.label_question = tk.Label(self)
        self.label_question.place(relx=self._RELX_ENTITY, rely=0.056, relheight=self._HIGH_ALL,
                                  relwidth=self._WITH_ENTITY)
        self.label_question.configure(font="-family {Courier New} -size 12")
        self.label_question.configure(anchor='w')
        self.label_question.configure(text="")

        self.Label2 = tk.Label(self)
        self.Label2.place(relx=self._RELX_LABLE, rely=0.056 +self._HIGH_ALL, relheight=self._HIGH_ALL, relwidth=self._WITH_LABLE)
        self.Label2.configure(anchor='w')
        self.Label2.configure(font="-family {Segoe UI} -size 12")
        self.Label2.configure(text='''answer''')

        self.entry_answer = tk.Entry(self)
        self.entry_answer.place(relx=self._RELX_ENTITY, rely=0.056 +self._HIGH_ALL, relheight=self._HIGH_ALL,
                                relwidth=self._WITH_ENTITY)
        self.entry_answer.configure(font="-family {Courier New} -size 12")

        self.label_answer_error = tk.Label(self)
        self.label_answer_error.place(relx=self._RELX_ENTITY, rely=0.056 +self._HIGH_ALL*2, relheight=self._HIGH_ALL
                                       , relwidth=self._WITH_ENTITY)
        self.label_answer_error.configure(foreground="#ff1f1f")

        self.Label1 = tk.Label(self)
        self.Label1.place(relx=self._RELX_LABLE, rely=0.056 +self._HIGH_ALL*5, relheight=self._HIGH_ALL, relwidth=self._WITH_LABLE)
        self.Label1.configure(font="-family {Segoe UI} -size 12")
        self.Label1.configure(anchor='w')
        self.Label1.configure(text='''new username''')

        self.entry_username = tk.Entry(self)
        self.entry_username.place(relx=self._RELX_ENTITY, rely=0.056 +self._HIGH_ALL*5, relheight=self._HIGH_ALL,
                                  relwidth=self._WITH_ENTITY)
        self.entry_username.configure(font="-family {Courier New} -size 12")

        self.label_username_error = tk.Label(self)
        self.label_username_error.place(relx=self._RELX_ENTITY, rely=0.056 + self._HIGH_ALL*6, relheight=self._HIGH_ALL
                                      , relwidth=self._WITH_ENTITY)
        self.label_username_error.configure(foreground="#ff1f1f")

        self.Label2 = tk.Label(self)
        self.Label2.place(relx=self._RELX_LABLE, rely=0.056 +self._HIGH_ALL*7, relheight=self._HIGH_ALL, relwidth=self._WITH_LABLE)
        self.Label2.configure(anchor='w')
        self.Label2.configure(font="-family {Segoe UI} -size 12")
        self.Label2.configure(text='''new password''')

        self.entry_password = tk.Entry(self)
        self.entry_password.place(relx=self._RELX_ENTITY, rely=0.056 +self._HIGH_ALL*7, relheight=self._HIGH_ALL,
                                  relwidth=self._WITH_ENTITY)
        self.entry_password.configure(font="-family {Courier New} -size 12")

        self.label_password_error = tk.Label(self)
        self.label_password_error.place(relx=self._RELX_ENTITY, rely=0.056 + self._HIGH_ALL * 8,
                                        relheight=self._HIGH_ALL
                                        , relwidth=self._WITH_ENTITY)
        self.label_password_error.configure(foreground="#ff1f1f")


        self.label_general_error = tk.Label(self)
        self.label_general_error.place(relx=self._RELX_ENTITY, rely=0.056 +self._HIGH_ALL*9, relheight=self._HIGH_ALL * 2
                                       , relwidth=self._WITH_ENTITY)
        self.label_general_error.configure(foreground="#ff1f1f")



        self.Button1 = tk.Button(self)
        self.Button1.place(relx=0.4, rely=0.845, relheight=self._HIGH_ALL, relwidth=0.2)
        self.Button1.configure(command=self.run)
        self.Button1.configure(text='''reset password''')