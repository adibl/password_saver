"""
name:
date:
description
"""

import time

import win32api
import win32gui
from pynput import keyboard
from pynput.keyboard import Key, Controller


def on_press(key):
    if key == Key.insert:
        window_handle = win32gui.GetForegroundWindow()
        result = win32api.SendMessage(window_handle, 0x0050, 0, 67699721)
        keyboard = Controller()
        keyboard.type('bleyer23@gmail.com')
        time.sleep(0.1)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(0.1)
        keyboard.type('qazwsx12')


def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False


# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
