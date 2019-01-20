"""
name:
date:
description
"""
from server.Autentication.JWT import create
import re

def create_JWT(*kg, **kv):
    print kg
    print kv
    return "Bearer " + create('aaaa', 1)

if __name__ == '__main__':
    with open("test_API.tavern.yaml", 'r') as f:

        s = f.read()
        re.sub('Bearer (.*)$', create_JWT(), s)
    with open("test_API.tavern.yaml", 'w') as f:
        f.write(s)