"""
name:
date:
description
"""
import Tkinter as tk

from client.API.ResetPassword import ForgotPassword
from client.GUI.ResetPassword import ResetPasswordGui
from client.window_order import fsm
from .state import State


class ResetPasswordState(ResetPasswordGui, State):
    def run(self, *args):

        ret = ForgotPassword.PATCH(self.username, self.entry_answer.get(),self.entry_username.get(), self.entry_password.get())
        if ret is True:
            fsm.finish()
            self.end()
        else:
            self.handle_errors(ret)

    def to_register(self):
        fsm.to_register()
        self.end()

    def general_error(self, error):
        error = error.replace('\r\n', '\n')
        self.label_general_error.config(text=error)

    def clean_errors(self):
        self.label_general_error.config(text=' ')

    def get_data(self, data):
        self.question=data['question']
        self.username = data['username']
        self.label_question.config(text=self.question)

    def clean(self):
        self.clean_errors()

    def handle_errors(self, data):
        if 'username' in data:
            self.label_username_error.configure(text=data['username'])
        if 'answer' in data:
            self.label_answer_error.configure(text=data['answer'])
        if 'password' in data:
            error = data['password'].replace('\r\n', '\n')
            self.label_password_error.configure(text=error)
        if 'general' in data:
            self.label_general_error.configure(text=data['general'])

    def run_after(self):
        data = self.entry_username.get()
        if data == '':
            data = self.username
        return {'username': data, 'password': self.entry_password.get()}