"""
name:
date:
description
"""
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk


class Gui(tk.Frame, object):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.variable = tk.BooleanVar(value=False, name='quit var')

    def wait_until_end(self):
        self.wait_variable(name=self.variable)

    def end(self):
        self.variable.set(True)
