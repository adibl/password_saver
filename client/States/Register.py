"""
name:
date:
description
"""
from client.window_order import fsm
from client.GUI.Register import RegisterGui
from client.API.Register import Register
from .state import State

class RegisterState(RegisterGui, State):

    def clean(self):
        self.clean_errors()

    def run_after(self):
        return self.entry_username.get(), self.entry_password.get()

    def run_befor(self):
        self.clean_errors()


    def get_data(self, data):
        print data

    def run(self, *args):
        print 'runnn'
        ret = Register.handle(self.entry_username.get(), self.entry_password.get(), self.Spinbox_question.get(),
                              self.entry_aswer.get())
        if ret is not True:
            self.clean_errors()
            if type(ret) is dict:
                for error in ret.keys():
                    if error == 'username':
                        self.username_error(ret[error])
                    elif error == 'password':
                        self.password_error(ret[error])
                    elif error == 'question':
                        print ret[error]
                        self.question_error(ret[error])
            self.mainloop()
            self.quit()
        else:
            self.clean_errors()
            fsm.registered()
            self.quit()



    def username_error(self, error):
        self.lable_username_error.config(text=error)

    def password_error(self, error):
        error = error.replace('\r\n', '\n')
        print repr(error)
        self.lable_password_error.config(text=error)

    def question_error(self, error):
        self.lable_question_error.config(text=error)

    def clean_errors(self):
        self.lable_username_error.config(text=' ')
        self.lable_password_error.config(text=' ')
        self.lable_answer_error.config(text=' ')
        self.lable_question_error.config(text=' ')