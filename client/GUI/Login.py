"""
name:
date:
description
"""
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
from client.window_order import fsm
from client.API.Login import Login


class LoginGui(tk.Frame):
    _RELX_ENTITY = 0.25
    _WITH_ENTITY = 0.7
    _HIGH_ALL = 0.07
    _WITH_LABLE = 0.15
    _RELX_LABLE = 0.05

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.place(relx=0.0, rely=0.0, relheight=1, relwidth=1)
        self.configure(width=455)

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

        self.lable_username_error = tk.Label(self)
        self.lable_username_error.place(relx=self._RELX_ENTITY, rely=0.141, relheight=self._HIGH_ALL
                                        , relwidth=self._WITH_ENTITY)
        self.lable_username_error.configure(foreground="#ff1f1f")

        self.entry_password = tk.Entry(self)
        self.entry_password.place(relx=self._RELX_ENTITY, rely=0.225, relheight=self._HIGH_ALL,
                                  relwidth=self._WITH_ENTITY)
        self.entry_password.configure(font="-family {Courier New} -size 12")

        self.lable_password_error = tk.Label(self)
        self.lable_password_error.place(relx=self._RELX_ENTITY, rely=0.31, relheight=self._HIGH_ALL * 2
                                        , relwidth=self._WITH_ENTITY)
        self.lable_password_error.configure(foreground="#ff1f1f")

        self.Button1 = tk.Button(self)
        self.Button1.place(relx=0.5, rely=0.845, height=24, width=87)
        self.Button1.configure(command=self.run)
        self.Button1.configure(text='''Log in''')

        self.Button1 = tk.Button(self)
        self.Button1.place(relx=0.7, rely=0.845, height=24, width=87)
        self.Button1.configure(command=self.to_register)
        self.Button1.configure(text='''Register''')

        self.bind('<Key-Return>', self.run)

    def run(self, *args):
        print 'runnn'
        ret = Login.handle(self.entry_username.get(), self.entry_password.get())
        if ret is not True:
            self.clean_errors()

            if type(ret) is dict:
                for error in ret.keys():
                    if error == 'username':
                        self.username_error(ret[error])
                    elif error == 'password':
                        self.password_error(ret[error])
            self.mainloop()
        else:
            self.clean_errors()
            self.quit()

    def to_register(self):
        fsm.to_register()
        self.quit()

    def username_error(self, error):
        self.lable_username_error.config(text=error)

    def password_error(self, error):
        error = error.replace('\r\n', '\n')
        print repr(error)
        self.lable_password_error.config(text=error)

    def clean_errors(self):
        self.lable_username_error.config(text=' ')
        self.lable_password_error.config(text=' ')