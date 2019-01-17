"""
name:
date:
description
"""
import sys
sys.path.insert(0, "D:/adi/Documents/password_saver/code/JWT")  # FIXME: make this unesesery

import pytest
import JWT

@pytest.mark.parametrize("userID,result", [
    ('aaaa', True),
    ('asdfsdfsd', True),
])
def test_create(userID, result):
    assert JWT.validate(*JWT.create(userID)) == result
