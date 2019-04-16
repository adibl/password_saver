"""
name:
date:
description
"""
from .state import State
import uiautomation as automation
from .GenerateGui import GenerateGui
from client.window_order import shadow_fsm
from client.API.AddRecord import Passwords
import base64

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
            cls.URL = cls.get_url()
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



    @staticmethod
    def get_url():
        control = automation.GetFocusedControl()
        controlList = []
        while control:
            controlList.insert(0, control)
            control = control.GetParentControl()
        if len(controlList) == 1:
            control = controlList[0]
        else:
            control = controlList[1]
        address_control = automation.FindControl(control, lambda c, d: isinstance(c,
                                                                                  automation.EditControl) and "Address and search bar" in c.Name)
        return address_control.CurrentValue()