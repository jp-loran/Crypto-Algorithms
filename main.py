# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 19:44:59 2022

@author: Juan
"""

from Crypto.Random import get_random_bytes
import crypto_algorithms as crypto
import performance as pf
import json

#TEST VECTOR
key = get_random_bytes(32) #256 bits  
plaintext = b'Attack at dawn'

result=json.loads(pf.measure(crypto.chacha20, plaintext, key))
print(result)