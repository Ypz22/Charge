"""
Turbo Hash Breaker 1.0

Turbo Hash Breaker is a complete password recovery tool for multiple hash types. It uses a wordlist full of passwords and then tries to crack a given hash with each of the passwords in the wordlist. In the first version, it supports the following hash types:
    
        MD5
        SHA1
        SHA256
        SHA3
        BLAKE2

The program is written in Python and uses the hashlib library to generate the hashes. The program is divided into two files: main.py and hasher.py. The main.py file contains the main program, while the hasher.py file contains the Hasher class, which is responsible for generating the hashes.

It use threads and the powerfull of parallelism to speed up the process of cracking the hashes.
"""

import argparse
import sys
from hasher import Hasher
import os
import time
from multiprocessing import Process

start_time = time.perf_counter()

def commonHashBreaker(hash_value, hash_type, dictionary_path):
    # Validar si el tipo de hash es 'md5'
    if hash_type != "md5":
        print("Error: Solo se soporta el tipo de hash MD5.")
        sys.exit(1)

    # Leer el diccionario uno por uno y comparar con el hash
    with open(dictionary_path, "r") as archivo:
        for password in archivo:
            password = password.strip()
            hasher = Hasher(password)

            # Calcular el hash MD5
            current_hash = hasher.hash_md5()

            # Comparar el hash
            if current_hash == hash_value:
                print(f"Contraseña encontrada: {password}")
                end_time = time.perf_counter()
                print(f"Tiempo de ejecución: {end_time - start_time} segundos")