"""
name:
date:
description
"""
from client.GUI.DeleteLogIn import DeleteLoginGui
from client.API.Delete import Delete
from .state import State
from client.window_order import fsm


class DeleteUser(DeleteLoginGui, State):
    is_runed = False

    def run(self, *args):
        print 'runnn'
        username = self.entry_username.get()
        password = self.entry_password.get()
        responce = Delete.DELETE(username, password)
        print responce
        if not responce is True:
            self.label_general_error.configure(text=responce['general'])
            self.wait_until_end()
        fsm.sucsees()
        self.end()

    def run_before(self):
        super(DeleteUser, self).run_before()

    def to_register(self):
        return NotImplemented