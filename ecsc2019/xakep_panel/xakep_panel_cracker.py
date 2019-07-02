#!/usr/bin/python

import hashlib
from Crypto.Cipher import AES
import base64

sha256_key = "c0fc5be956e3c5500366fd46ee179d00955ae403787164d6c4ab4e07431d2520".decode("hex")
md5_iv = "a5c44099256a1f3432b5c6acda700096".decode("hex")

enc = base64.b64decode("TT321MTlmflN18OEIve08jzWBKMq7XGJukuRBv45g18=")

aes = AES.new(sha256_key, AES.MODE_CBC, md5_iv)
print aes.decrypt(enc)
