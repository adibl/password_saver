"""
name:
date:
description
"""
from jwcrypto import jwt, jwe
import time

def create(userID, sing_key, encrypte_key, timeout=25):
    """
    bild JWT token from user cradentials
    :param str userID:
    :return:
    """
    header = {}
    header['alg'] = 'HS256'
    header['typ'] = "JWT"
    body ={}
    body['iss'] = userID
    body['iat'] = int(time.time())
    body['exp'] = body['iat'] + timeout * 60

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
    return encrypted_signed_token