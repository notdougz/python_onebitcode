"""Escreva um programa em Python que gera um número 
aleatório para que o usuário tente acertar o número. 

Algumas sugestões para o programa:

Utilizar um laço de repetição para que o programa execute
até que o usuário informe um número referente a opção para sair do programa.
Utilizar o módulo random para gerar valores 
aleatórios dentro de um intervalo. Ex: 1 a 10.
Lê o número que o usuário digitar via input e 
comparar se é o mesmo número que o programa sorteou."""

import random

sair = False

while not sair:
    try:
        numero_usuario = int(input("Qual número estou pensando de 1 a 10?\n"))
        numero_maquina = random.randint(1, 10)

        if numero_usuario == numero_maquina:
            print("Você acertou!")
            sair = True
        else:
            print(f"Você errou! O número era {numero_maquina}. Tente novamente!")
    except ValueError:
        print("Por favor, insira um número válido.")