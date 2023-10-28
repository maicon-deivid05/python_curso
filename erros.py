#!/usr/bin/env python3

import os
import sys

# EAFP - Easy to ASK Forgivenes than permission
#(É mais facil pedir perdao do que permissao)

try:
    names = open("names.txt").readlines()
    # FileNotFoundError
except FileNotFoundError as e: 
    print(f"{str(e)}")
    sys.exit(1)
else:
    print("Sucesso!!!")
finally:
    print("execute isso sempre")

try:
    print(names[2])
except:
    print("[Error] Missing name in the list")
    sys.exit(1)