"""
name:
date:
description
"""
from jwcrypto import jwk


def main():
    key = jwk.JWK(generate='oct', size=256)
    key2 = jwk.JWK(generate='RSA', size=2048)
    data = key.export()
    with open('public_signing.pem', 'wb') as f:
        f.write(data)

    data = key2.export_public()
    with open('public_encrypte_public.pem', 'wb') as f:
        f.write(data)

    data = key2.export_private()
    with open('public_encrypte_private.pem', 'wb') as f:
        f.write(data)


if __name__ == '__main__':
    main()
