"""
name:
date:
description
"""
from jwcrypto import jwt, jwe, jwk
import time
from jwcrypto.common import json_decode

with open('public_signing.pem', 'rb') as f: #FIXME: take files from other directory
    KEY = json_decode(f.read())
with open('public_encrypte_public.pem', 'rb') as f:
    ENC_KEY = json_decode(f.read())
def create(userID, timeout=25):
    """
    bild JWT token from user cradentials
    :param str userID: the user identifier
    :param str signing_key: the signing key
    :param str encrypte_key: the encription key
    :param int timeout: timeout of the JWT in minutes. default is 25
    :return:
    """
    header = {'alg': 'HS256', 'typ': "JWT"}
    body ={}
    body['iss'] = userID
    body['iat'] = int(time.time())
    body['exp'] = body['iat'] + timeout * 60

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
    encrypted_signed_token = E.serialize()
    return encrypted_signed_token