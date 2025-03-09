# Solicita ao usuário que insira seu nome
name = input("Qual seu nome? \n")

# Modos de abertura de arquivo:
# r - leitura
# w - escrita
# a - append (adicionar ao final do arquivo)

# Abre o arquivo "names.txt" no modo append ("a") para adicionar o nome ao final do arquivo
with open("names.txt", "a") as file:
    # Escreve o nome no arquivo, seguido de uma quebra de linha
    file.write(f"{name}\n")