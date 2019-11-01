import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

password_provided = 'kanyer_hova'
password = password_provided.encode()

salt = b'\x0cQT\xae\x0b\xa1k\xe4&^c\xf8\x93V\xd6\xb8'
kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
                 length=32,
                 salt=salt,
                 iterations=100000,
                 backend=default_backend()
                 )
key = base64.urlsafe_b64encode(kdf.derive(password))

file = open('na.key', 'wb')
file.write(key)
file.close()

print(key)
