"""
name:
date:
description
"""
from .state import State
from GUI.GenerateGui import GenerateGui
from client.window_order import shadow_fsm
from client.API.AddRecord import Passwords
from .ShadowInsertUsername import ShadowInserUsername

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
        gui = GenerateGui()

        return_value = None
        while return_value is not True:
            gui.mainloop()
            return_value = Passwords.handle(cls.URL, *gui.get_data())
            gui.handle_errors(return_value)
        gui.destroy()
        shadow_fsm.to_key_logger()
