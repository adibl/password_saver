"""
name:
date:
description
"""
import tkinter as tk
#from client.API.Register import Register
from client.window_order import fsm


try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

from client.States.Register import RegisterState
from client.States.Login import LoginState
from client.States.SeeAll import SeeAllState
FSM_TO_CLASS = {'register' : RegisterState, 'login': LoginState, 'see_all': SeeAllState}




class TopLevel(tk.Tk):
    PAGES = (RegisterState, LoginState, SeeAllState)

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        '''This class configures and populates the toplevel window.
                   top is the toplevel containing window.'''
        self.geometry("500x500")
        self.title("New Toplevel")

        self.frames = {}
        self.last_frame = None

        for F in self.PAGES:
            frame = F(self)

            self.frames[F] = frame
            frame.place(relx=0.0, rely=0.0, relheight=1, relwidth=1)
        self.show_frame()

    def show_frame(self, data=''):
        frame = self.frames[FSM_TO_CLASS[fsm.current]]
        if self.last_frame is not None:
            data = self.last_frame.run_after()
            if data is not None:
                frame.get_data(data)
        frame.tkraise()
        frame.run_before()
        self.last_frame = frame

    def get_data(self):
        ret = self.last_frame.run_after()
        self.last_frame.clean()
        return ret

if __name__ == '__main__':
    root = TopLevel()
    root.mainloop()
    while not fsm.is_finished():
        data = root.get_data()
        root.show_frame(data)
        root.mainloop()


