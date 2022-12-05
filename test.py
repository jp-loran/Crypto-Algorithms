# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 22:56:33 2022

@author: Juan
"""

from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes
import timeit

#TEST VECTOR
key = get_random_bytes(32) #256 bits  
plaintext = b'Attack at dawn'


def chacha20(key,vector):
    print('CHACHA20')
    cipher = ChaCha20.new(key=key)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext.hex()
    

def get_time(function, key, vector):
    start= timeit.default_timer()
    result=function(key,vector)    
    print(result)
    end= timeit.default_timer()
    return end-start
    
print(get_time(chacha20,key,plaintext))