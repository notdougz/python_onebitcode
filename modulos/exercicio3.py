"""Escreva um programa em Python para verificar se uma string 
contém apenas um determinado conjunto de caracteres 
(neste caso, a-z, A-Z e 0-9)."""

import re


frase = input(str("Insira uma frase: "))

#O ^ indica o inicio da frase o + indica que pode ter mais de uma ocorrencia de números alfanumericos e o espaço dentro do[ ] indica que a frase pode conter espaços
padrao = r'^[a-zA-Z0-9 ]+$'

if re.match(padrao, frase):
    print("Frase no padrão!")
else:
    print("Frase fora do padrão")

"""
import re
def check_character(string):
    rule = re.compile(r'[^a-zA-Z0-9]')
    string = rule.search(string)
    return not bool(string)

print(check_character("ABCDEFabcdef123450")) 
print(check_character("*&%@#!}{"))

Método ensinado no curso
"""