"""
name:
date:
description
"""

import Tkinter as tk

from client.API.ResetPassword import ForgotPassword
from client.GUI.GetSequrityQuestion import GetSecurityQuestionGui
from client.window_order import fsm
from .state import State


class GetSecurityQuestionState(GetSecurityQuestionGui, State):
    def run(self, *args):
        self.question = None
        self.username = None
        print 'runnn'
        username = self.entry_username.get()
        is_ok, ret = ForgotPassword.GET(username)
        print ret
        if is_ok is not True:
            if type(ret) is dict:
                for error in ret.keys():
                    if error == 'general':
                        self.general_error(ret[error])
                    if error == 'username':
                        self.general_error(ret[error])
                self.wait_until_end()
            elif type(ret) is str:
                fsm.got_question()
                self.question = ret
                self.username = username
                self.end()
            else:
                self.general_error('general error')
                self.wait_until_end()
        else:
            if type(ret) is str or type(ret) is unicode:
                fsm.got_question()
                self.question = ret
                self.username = username
                self.end()
            else:
                self.general_error('general error')
                self.wait_until_end()

    def to_register(self):
        fsm.to_register()
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

    def clean(self):
        self.clean_errors()

    def run_after(self):
        return {'username': self.username, 'question': self.question}
