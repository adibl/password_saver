"""
name:
date:
description
"""
from server.Autentication.JWT import create
import re

def create_JWT():
    return "Bearer " + create('aaaaaaaaaaaaaaaaaaaaaaaa', 10)

if __name__ == '__main__':
    with open("test_API.tavern.yaml", 'r') as f:
        s = f.read()
        print s
    s = re.sub('Bearer (.*)$', create_JWT(), s, flags=re.M)
    print s
    with open("test_API.tavern.yaml", 'w+') as f:
        f.write(s)