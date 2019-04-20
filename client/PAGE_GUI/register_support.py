#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.22
#  in conjunction with Tcl version 8.6
#    Apr 12, 2019 12:16:00 PM +0300  platform: Windows NT

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True


def set_Tk_var():
    global entity_username
    entity_username = tk.StringVar()
    global entitiy_password
    entitiy_password = tk.StringVar()
    global spinbox_question
    spinbox_question = tk.StringVar()
    global entity_answer
    entity_answer = tk.StringVar()


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


if __name__ == '__main__':
    import register

    register.vp_start_gui()
