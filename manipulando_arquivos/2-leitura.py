# Modos de abertura de arquivo:
# r - leitura
# w - escrita
# a - append (adicionar ao final do arquivo)

# Abre o arquivo de texto contendo os nomes no modo leitura ("r")
with open("manipulando_arquivos/dados/names.txt", "r", encoding="utf-8") as file:
    # Itera sobre cada linha do arquivo
    for line in file:
        # Remove espaços em branco no final da linha (incluindo a quebra de linha) e exibe uma mensagem personalizada
        print(f"Olá, {line.rstrip()}")