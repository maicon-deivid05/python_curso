#! /home/gitpod/.pyenv/shims/tutorial-env python3
"""Hello World Multi Linguas.

Dependendo da ligua configurada no ambiente  o programa exibe a mensagem 
correspondente.

Como usar:

Tenha a variável LANG devidamente configutada ex:

    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
    
"""
__version__ ="0.1.3"
__author__ ="Maicon"
__license__ ="Unlicense"

import os
import sys


arguments = {
    "lang": None,
    "count": 1,
}
for arg in sys.argv [1:]:
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:   
        print(f"invalid Option `{key}`")
        sys.exit()
    arguments[key] = value
 

current_language = arguments["lang"]
if current_language is None:
    if "LANG" is os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language:")

current_language = current_language[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Muno!",
    "fr_FR": "Bonjour, Monde!",
}

print(msg[current_language] * int(arguments["count"]))  
