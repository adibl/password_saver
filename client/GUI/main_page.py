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

from client.GUI.Register import RegisterGui
from Login import LoginGui
FSM_TO_CLASS = {'register' : RegisterGui, 'login': LoginGui}

class SeaofBTCapp(tk.Tk):
    PAGES = (RegisterGui, LoginGui)

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        '''This class configures and populates the toplevel window.
                   top is the toplevel containing window.'''
        self.geometry("500x500")
        self.title("New Toplevel")

        self.frames = {}

        for F in self.PAGES:
            frame = F(self)

            self.frames[F] = frame
            frame.place(relx=0.0, rely=0.0, relheight=1, relwidth=1)
        self.show_frame()

    def show_frame(self):
        frame = self.frames[FSM_TO_CLASS[fsm.current]]
        frame.tkraise()

if __name__ == '__main__':
    root = SeaofBTCapp()
    root.mainloop()
    while not fsm.is_finished():
        root.show_frame()
        root.mainloop()


