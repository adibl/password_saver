"""
name:
date:
description
"""
from .state import State
import uiautomation as automation
from .GenerateGui import GenerateGui

class AddRecord(State):
    URL = None

    @classmethod
    def on_press(cls):
        """
        run the satae

        :return:
        """
        print 'start add record'
        cls.URL = cls.get_url()
        gui = GenerateGui()
        gui.mainloop()



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