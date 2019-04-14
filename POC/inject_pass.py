"""
name:
date:
description
"""

from pynput import keyboard
from pynput.keyboard import Key, Controller
import time

def on_press(key):
    if key == Key.insert:
        import win32api
        win32api.LoadKeyboardLayout('00000409', 1)  # to switch to english
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