# Enunciado:

# Lendo n linhas de um arquivo

# Escreva um programa Python para ler as primeiras n linhas de um arquivo.

# O nome do arquivo e a quantidade de linhas devem ser passadas via parâmetro na função.

# Importa a função islice do módulo itertools para auxiliar na leitura parcial do arquivo
from itertools import islice

# Função para ler as primeiras 'nlines' linhas de um arquivo
def file_read_from_line(fname, nlines):
    """
    Lê e imprime as primeiras 'nlines' linhas de um arquivo.

    Parâmetros:
    fname (str): Caminho do arquivo a ser lido.
    nlines (int): Número de linhas a serem lidas e exibidas.
    """
    with open(fname, encoding="utf-8") as file:  # Abre o arquivo com codificação UTF-8
        for line in islice(file, nlines):  # Lê apenas as 'n' primeiras linhas
            print(line, end="")  # Exibe a linha sem adicionar uma nova quebra de linha extra

# Chamada da função para ler as 2 primeiras linhas do arquivo "texto.txt"
file_read_from_line("manipulando_arquivos/dados/texto.txt", 2)
