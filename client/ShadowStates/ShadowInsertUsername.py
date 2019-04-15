"""
name:
date:
description
"""

from client.GUI.SeeAll import SeeAllGui
from .state import State
import uiautomation as automation
import win32api, win32gui
import keyboard
from client.window_order import shadow_fsm


class ShadowInserUsername(State):
    USERNAME = 'bleyer23'
    PASSWORD = 'qazwsx12'


    @classmethod
    def on_press(cls, *args):
        print 'shadow insert username'
        try:
            url = cls.get_url()
        except:
            shadow_fsm.no_url()
            return
        window_handle = win32gui.GetForegroundWindow()
        result = win32api.SendMessage(window_handle, 0x0050, 0, 67699721)
        if not result == 0:
            shadow_fsm.no_url()
            return
        keyboard.write(cls.USERNAME)
        shadow_fsm.username_inserted()

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

    @classmethod
    def pass_data(cls):
        return {'username': cls.USERNAME, 'password': cls.PASSWORD}
