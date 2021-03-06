"""
name:
date:
description
"""
import os
import time

from jwcrypto import jwt, jwe, jwk
from jwcrypto.common import json_decode

with open(os.path.join(os.path.dirname(__file__), 'public_signing.pem'),
          'rb') as f:  # TODO: take files from other directory
    KEY = json_decode(f.read())
with open(os.path.join(os.path.dirname(__file__), 'public_encrypte_public.pem'), 'rb') as f:
    ENC_KEY = json_decode(f.read())


def create(userID, timeout=25):
    """
    bild JWT token from user cradentials
    :param str userID: the user identifier
    :param int timeout: timeout of the JWT in minutes. default is 25
    :return:
    """
    header = {'alg': 'HS256', 'typ': "JWT"}
    body = {'iss': userID, 'iat': int(time.time())}
    body['exp'] = int(body['iat'] + timeout * 60)

    # generate JWT
    T = jwt.JWT(header, body)
    # sign the JWT with a private key
    T.make_signed_token(jwk.JWK(**KEY))
    # serialize it
    signed_token = T.serialize(compact=True)
    # JWE algorithm in the header
    eprot = {
        'alg': "RSA-OAEP",
        'enc': "A128CBC-HS256",
        "typ": "JWE"
    }
    E = jwe.JWE(plaintext=signed_token, protected=eprot, recipient=jwk.JWK(**ENC_KEY))
    # encrypt with a public key
    # serialize it
    encrypted_signed_token = E.serialize(compact=True)
    return encrypted_signed_token
