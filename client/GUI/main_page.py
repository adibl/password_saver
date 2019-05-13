"""
name:
date:
description
"""
# from client.API.Register import Register
from client.window_order import fsm

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

from client.States.Register import RegisterState
from client.States.Login import LoginState
from client.States.SeeAll import SeeAllState
from client.States.Edit import EditState
from client.States.DeleteUser import DeleteUser
from client.States.GetSecurityQuestion import GetSecurityQuestionState
from client.States.ResetPassword import ResetPasswordState

FSM_TO_CLASS = {'register': RegisterState, 'login': LoginState, 'see_all': SeeAllState, 'get_answer': ResetPasswordState,
                'edit': EditState, 'delete_user': DeleteUser, 'get_security_question': GetSecurityQuestionState}


class TopLevel(tk.Tk):
    PAGES = (FSM_TO_CLASS.values())

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        '''This class configures and populates the toplevel window.
                   top is the toplevel containing window.'''
        self.geometry("500x500")
        self.title("New Toplevel")
        self.bind("<Destroy>", self._destroy)

        self.frames = {}
        self.last_frame = None

        for F in self.PAGES:
            frame = F(self)

            self.frames[F] = frame
            frame.place(relx=0.0, rely=0.0, relheight=1, relwidth=1)

    def show_frame(self, data=''):
        self.frame = self.frames[FSM_TO_CLASS[fsm.current]]
        if self.last_frame is not None:
            data = self.last_frame.pass_data()
            self.last_frame.clean()
            if data is not None:
                self.frame.get_data(data)

        self.frame.tkraise()
        self.frame.run_before()
        self.frame.focus_set()
        self.last_frame = self.frame
        self.frame.wait_until_end()

    def get_data(self):
        ret = self.last_frame.pass_data()
        self.last_frame.clean()
        return ret

    def _destroy(self, *args):
        self.bind('<Destroy>', self._ignore)
        fsm.close()
        self.frame.end()

    def _ignore(self, e): pass

def run_fsm(root):
    root.show_frame()
    while not fsm.is_finished():
        print fsm.current
        data = root.get_data()
        root.show_frame(data)



if __name__ == '__main__':
    root = TopLevel()
    root.after(1, run_fsm, root)
    root.mainloop()
