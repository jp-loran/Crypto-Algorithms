# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 20:55:28 2022

@author: Juan
"""


from Crypto.Cipher import ChaCha20, AES
from Crypto.Hash import SHA384, SHA512, SHA3_384, SHA3_512

from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

#TEST VECTOR
key = get_random_bytes(32) #256 bits  
plaintext = b'Attack at dawn'

#CHACHA20
print('CHACHA20')
cipher = ChaCha20.new(key=key)
ciphertext = cipher.encrypt(plaintext)
print(ciphertext.hex())

#AES-EBC
print('AES-EBC')
cipher=AES.new(key,AES.MODE_ECB)
ciphertext= cipher.encrypt(pad(plaintext,16))
print(ciphertext.hex())

#AES-CBC
print('AES-CBC')
cipher=AES.new(key,AES.MODE_CBC)
ciphertext= cipher.encrypt(pad(plaintext,16))
print(ciphertext.hex())

#SHA-384
print('SHA-384')
cipher=SHA384.new()
cipher.update(plaintext)
print(cipher.hexdigest())

#SHA-512
print('SHA-512')
cipher=SHA512.new()
cipher.update(plaintext)
print(cipher.hexdigest())


#SHA3-384
print('SHA3-384')
cipher=SHA3_384.new()
cipher.update(plaintext)
print(cipher.hexdigest())


#SHA3-512
print('SHA3-512')
cipher=SHA3_512.new()
cipher.update(plaintext)
print(cipher.hexdigest())
