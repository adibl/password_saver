"""
name:
date:
description
"""

from client.API.ManageRecord import Record
from client.GUI.EditGui import EditGui
from client.window_order import fsm
from .state import State


class EditState(EditGui, State):
    def run_before(self, *args):
        data = Record.GET(self.url)
        if 'username' in data.keys() and 'password' in data.keys():
            self.insert_username_and_pass(data['username'], data['password'])

    def run(self):
        print 'runned'
        ret = Record.PATCH(self.url, username=self.entry_username.get(), password=self.entry_password.get())
        if ret:
            fsm.trigger('return')
            self.end()
        else:
            print ret
            raise ValueError

    def get_data(self, data):
        self.url = data[0]
