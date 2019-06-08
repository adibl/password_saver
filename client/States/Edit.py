"""
name:
date:
description
"""

from client.API.ManageRecord import Record
from client.GUI.EditGui import EditGui
from client.window_order import fsm
from .state import State
from  tkinter import messagebox


class EditState(EditGui, State):
    def run_before(self, *args):
        data = Record.GET(self.url)
        if 'username' in data.keys() and 'password' in data.keys():
            self.insert_username_and_pass(data['username'], data['password'])
        elif data['general'] == 404:
            messagebox.showwarning('Error', "program don't exist")
            fsm.trigger('return')
        else:
            messagebox.showerror('Error', 'unknown error')

    def run(self):
        print 'runned'
        ret = Record.PATCH(self.url, username=self.entry_username.get(), password=self.entry_password.get())
        if ret:
            fsm.trigger('return')
            self.end()
        elif ret['general'] == 404:
            messagebox.showwarning('Error', "program don't exist")
            fsm.trigger('return')
        else:
            messagebox.showerror('Error', 'unknown error')

    def get_data(self, data):
        if 'url' in data:
            self.url = data['url']

    def delete(self):
        ret = Record.DELETE(self.url)
        if ret:
            fsm.trigger('return')
            self.end()
        else:
            messagebox.showerror('Error', 'unknown error')
