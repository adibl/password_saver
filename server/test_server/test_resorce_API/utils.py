"""
name:
date:
description
"""
from server.Autentication.JWT import create, validate
import re

def create_JWT():
    jwt =create('aaaaaaaaaaaaaaaaaaaaaaaa', 100)
    return "Bearer " + str(jwt)

if __name__ == '__main__':
    with open("test_validation.tavern.yaml", 'r') as f:
        s = f.read()
    s = re.sub('Bearer (.*)$', create_JWT(), s, flags=re.M)
    with open("test_validation.tavern.yaml", 'w+') as f:
        f.write(s)