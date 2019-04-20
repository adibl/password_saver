"""
name:
date:
description
"""
import keyboard

from client.ShadowStates.state import State
from client.window_order import shadow_fsm


class KeyLoggerState(State):
    KEY = 'insert'

    @classmethod
    def on_press(cls):
        keyboard.add_hotkey('insert', shadow_fsm.insert)
        keyboard.add_hotkey('ctrl+alt+insert', shadow_fsm.home)
        keyboard.read_hotkey(suppress=False)
        keyboard.unhook_all_hotkeys()
