"""
name:
date:
description
"""
import sys
import time
sys.path.insert(0, "D:/adi/Documents/password_saver/code/JWT")  # FIXME: make this unesesery
from jwcrypto import jwk, jws

import pytest
from server.Autentication.JWT import validate, create

@pytest.mark.parametrize("userID,result", [
    ('aaaa', True),
    ('asdfsdfsd', True),
])
def test_create(userID, result):
    key = jwk.JWK(generate='oct', size=256)
    key2 = jwk.JWK(generate='RSA', size=1024)
    assert validate(create('sdfsdf', key, key2), key, key2) is not False


@pytest.mark.parametrize("userID, timeout,result", [
    ('aaaa', 5, True),
    ('asdfsdfsd', 3, True),
    ('asdfsdfsd', 11, False),
])
def test_validate_timeout(userID, timeout,result):
    key = jwk.JWK(generate='oct', size=256)
    key2 = jwk.JWK(generate='RSA', size=1024)
    token = create('sdfsdf', key, key2, timeout=timeout/60)
    time.sleep(10)
    assert validate(token, key, key2) is not False


def test_no_exp():
    key = jwk.JWK(generate='oct', size=256)
    key2 = jwk.JWK(generate='RSA', size=1024)
    userID = 'aaaa'
    #JWT.create.create()
    sing_key = key
    encrypte_key = key2
    timeout = 25
    from jwcrypto import jwt, jwe
    header = {}
    header['alg'] = 'HS256'
    header['typ'] = "JWT"
    body = {}
    body['iss'] = userID
    body['iat'] = int(time.time())
    #         body['exp'] = body['iat'] + timeout * 60

    # generate JWT
    T = jwt.JWT(header, body)
    # sign the JWT with a private key
    T.make_signed_token(sing_key)
    # serialize it
    signed_token = T.serialize(compact=True)

    # JWE algorithm in the header
    eprot = {
        'alg': "RSA-OAEP",
        'enc': "A128CBC-HS256"
    }
    E = jwe.JWE(signed_token, eprot)
    # encrypt with a public key
    E.add_recipient(encrypte_key)  #
    # serialize it
    encrypted_signed_token = E.serialize(compact=True)
    assert validate(encrypted_signed_token, key, key2) is False


