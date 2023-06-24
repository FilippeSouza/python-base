#! /usr/bin/env python3
"""Hello World Multi Linguas

Dependendo da lingua configurada no ambiente o programa exibe a mensagem  correspondente.

Como usar:

TEnha a varial LANG  devidamente configurada ex:
	export LANG=pt_Br

Execução

	python3 hello.py
	ou
	./hello.py
"""
__version__= "0.0.1"
__author__ = "Filippe de Souza"
__license__ = "Unlicense"

#Dunder (identificador para a palavra __ (underline)__

import os

#current_language  = "it_IT"
current_language = os.getenv("LANG", "en_US")[:5]

msg =  "Hello, World!"

if current_language  == "pt_BR":
	msg = "Ola, mundo!"
elif current_language == "it_IT":
	msg = "Ciao, Mondo!"
elif current_language == "es_SP":
	msg = "Hola, Munod!"
elif current_language == "fr_FR":
	msg = "Bonjour Monde"

print(msg)



