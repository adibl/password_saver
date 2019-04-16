#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep
import uiautomation as automation

def print_name(c,d):
    if isinstance(c, automation.EditControl):
        if u"שורת חיפוש וכתובות אתרים" in unicode(c.Name) or u"Address and search bar" in unicode(c.Name):
            return True
    return False


if __name__ == '__main__':
    sleep(3)
    control = automation.GetFocusedControl()
    print control
    controlList = []
    while control:
        controlList.insert(0, control)
        control = control.GetParentControl()
    if len(controlList) == 1:
        control = controlList[0]
    else:
        control = controlList[1]
    print control
    address_control = automation.FindControl(control, print_name)
    print address_control.CurrentValue()



