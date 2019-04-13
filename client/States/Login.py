"""
name:
date:
description
"""
from client.window_order import fsm
from client.GUI.Login import LoginGui
from client.API.Login import Login
from .state import State


class LoginState(LoginGui, State):
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

    def clean(self):
        pass

    def get_data(self, data):
        self.entry_username.insert(0, data[0])
        self.entry_password.insert(0, data[1])

    def run_after(self):
        return None