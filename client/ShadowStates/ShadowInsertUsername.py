#!/usr/bin/env python
# -*- coding: utf-8 -*-

import keyboard
import uiautomation as automation
import win32api
import win32gui

from client.API.ManageRecord import Record
from client.window_order import shadow_fsm
from client.ShadowStates.state import State
import re


class ShadowInserUsername(State):
    USERNAME = 'bleyer23'
    PASSWORD = 'qazwsx12'

    @classmethod
    def on_press(cls, *args):
        print 'shadow insert username'
        try:
            url = cls.get_url()
        except:
            print 'no url'
            shadow_fsm.no_url()
            return
        window_handle = win32gui.GetForegroundWindow()
        result = win32api.SendMessage(window_handle, 0x0050, 0, 67699721)
        if not result == 0:
            shadow_fsm.no_url()
            return
        ret = Record.GET(url)
        if 'username' in ret.keys() and 'password' in ret.keys():
            keyboard.write(ret['username'])
            cls.PASSWORD = ret['password']
            shadow_fsm.username_inserted()
        else:
            shadow_fsm.no_url()


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
        address_control = automation.FindControl(control, find_search_bar)
        url = address_control.CurrentValue()
        URL_RE = re.compile('^https?://([\w|.]*)/')
        return URL_RE.search(url).group(1)

    @classmethod
    def pass_data(cls):
        return {'username': cls.USERNAME, 'password': cls.PASSWORD}


def find_search_bar(c, d):
    if isinstance(c, automation.EditControl):
        if u"שורת חיפוש וכתובות אתרים" in unicode(c.Name) or u"Address and search bar" in unicode(c.Name):
            return True
    return False
