"""
name:
date:
description
"""
from client.ShadowStates.state import State
import keyboard
from client.window_order import shadow_fsm
import time

class KeyLoggerState(State):
    KEY = 'insert'

    @classmethod
    def on_press(cls):
        keyboard.add_hotkey('insert', shadow_fsm.insert)
        keyboard.add_hotkey('home', shadow_fsm.home)
        keyboard.read_hotkey(suppress=False)
        keyboard.unhook_all_hotkeys()

