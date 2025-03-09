# Lista vazia para armazenar os nomes
names = []

# Abre o arquivo de texto contendo os nomes
with open("manipulando_arquivos/dados/names.txt", "r", encoding="utf-8") as file:
    # Itera sobre cada linha do arquivo
    for line in file:
        # Remove espaços em branco no final da linha (incluindo a quebra de linha) e adiciona o nome à lista
        names.append(line.rstrip())

# Ordena a lista de nomes alfabeticamente e exibe uma mensagem personalizada para cada nome
for name in sorted(names):
    print(f"Olá, {name}!")