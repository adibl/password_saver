"""
name:
date:
description
"""

import Tkinter as tk

from client.API.Login import Login
from client.GUI.Login import LoginGui
from client.window_order import fsm
from .state import State


class LoginState(LoginGui, State):
    def run(self, *args):
        print 'runnn'
        ret = Login.handle(self.entry_username.get(), self.entry_password.get())
        print ret
        if ret is not True:
            if type(ret) is dict:
                for error in ret.keys():
                    if error == 'general':
                        self.general_error(ret[error])
            self.wait_until_end()
        else:
            fsm.logedin()
            self.clean_errors()
            self.end()

    def to_register(self):
        fsm.to_register()
        self.end()

    def to_forgot_password(self):
        fsm.to_forgot_password()
        self.end()

    def general_error(self, error):
        error = error.replace('\r\n', '\n')
        self.label_general_error.config(text=error)

    def clean_errors(self):
        self.label_general_error.config(text=' ')

    def get_data(self, data):
        if 'username' in data:
            self.entry_username.delete(0, tk.END)
            self.entry_username.insert(0, data['username'])
        if 'password' in data:
            self.entry_password.delete(0, tk.END)
            self.entry_password.insert(0, data['password'])

    def clean(self):
        self.clean_errors()

    def pass_data(self):
        return {'username': self.entry_username.get(), 'password': self.entry_password.get()}
