# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 20:55:28 2022

@author: Juan
"""

from Crypto.Cipher import ChaCha20, AES
from Crypto.Hash import SHA384, SHA512, SHA3_384, SHA3_512
from Crypto.Util.Padding import pad

"""
Utilizamos las implementaciones criptográficas de la
librería pycryptodome y retornamos el resultado en 
hexadecimal
"""

#CHACHA20
def chacha20(key,vector):
    print('CHACHA20')
    cipher = ChaCha20.new(key=key)
    ciphertext = cipher.encrypt(vector)
    return ciphertext.hex()
    
#AES-EBC
def aes_ebc(key,vector):
    print('AES-EBC')
    cipher=AES.new(key,AES.MODE_ECB)
    ciphertext= cipher.encrypt(pad(vector,16))
    return ciphertext.hex()

#AES-CBC
def aes_cbc(key,vector):
    print('AES-CBC')
    cipher=AES.new(key,AES.MODE_CBC)
    ciphertext= cipher.encrypt(pad(vector,16))
    return ciphertext.hex()

#SHA-384
def sha_384(vector):
    print('SHA-384')
    cipher=SHA384.new()
    cipher.update(vector)
    return cipher.hexdigest()

#SHA-512
def sha_512(vector):
    print('SHA-512')
    cipher=SHA512.new()
    cipher.update(vector)
    return cipher.hexdigest()

#SHA3-384
def sha3_384(vector):
    print('SHA3-384')
    cipher=SHA3_384.new()
    cipher.update(vector)
    return cipher.hexdigest()
        
#SHA3-512
def sha3_512(vector):
    print('SHA3-512')
    cipher=SHA3_512.new()
    cipher.update(vector)
    return cipher.hexdigest()

