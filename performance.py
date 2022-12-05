# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 19:43:47 2022

@author: Juan
"""

import timeit
import json 
import tracemalloc

"""
Obtiene el tiempo que toma ejecutar una función recibida
Obtiene la memoria en bytes utilizada por el proceso

Argumentos: 
    function: funcion criptográfica a utilizar 
    key: llave para cifrar
    vector: texto en claro a cifrar
    
Retorna json:
    time: tiempo en segundos utilizado
    current_memory: memoria actual utilizada
    peak_memory: pico de memoria utilizado
    result: resultado del proceso de encriptado
"""    

def measure(function,vector,key=None):
    start_time= timeit.default_timer()
    
    tracemalloc.start()
    if(key is None):
        result=function(vector)    
    else:
        result=function(key,vector)
    
    end_time= timeit.default_timer()
    
    data = {'time': end_time-start_time,
            'current_memory':tracemalloc.get_traced_memory()[0],
            'peak_memory': tracemalloc.get_traced_memory()[1], 
            'result':result}
    
    tracemalloc.stop()
    return json.dumps(data)