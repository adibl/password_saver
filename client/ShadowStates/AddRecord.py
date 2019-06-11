"""
name:
date:
description
"""
from client.GUI.GenerateGui import GenerateGui
from client.API.AddRecord import Passwords
from client.API.ManageRecord import Record
from client.window_order import shadow_fsm
from .ShadowInsertUsername import ShadowInserUsername
from .state import State
import tkMessageBox
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

class AddRecord(State):
    URL = None

    @classmethod
    def on_press(cls):
        """
        run the satae

        :return:
        """
        print 'start add record'
        try:
            cls.URL = ShadowInserUsername.get_url()
        except:
            shadow_fsm.no_url()
            return
        data = Record.GET(cls.URL)
        gui = GenerateGui()
        is_exzist = False
        if all(x in data for x in ['username', 'password']):
            gui.insert_username_and_pass(data['username'], data['password'])
            is_exzist = True
        gui.mainloop()
        if is_exzist:
            username, password = gui.get_data()
            return_value = Record.PATCH(cls.URL, username=username, password=password)
        else:
            return_value = Passwords.handle(cls.URL, *gui.get_data())
        while return_value is not True:
            gui.handle_errors(return_value)
            gui.mainloop()
            if is_exzist:
                username, password = gui.get_data()
                return_value = Record.PATCH(cls.URL, username=username, password=password)
            else:
                return_value = Passwords.handle(cls.URL, *gui.get_data())
        gui.destroy()
        shadow_fsm.to_key_logger()
