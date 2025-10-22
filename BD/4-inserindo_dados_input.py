import sqlite3

# 1 - Conectando no BD
connection = sqlite3.connect("title.db")

# 2 - Criando um cursor
cursor = connection.cursor()

# 3 - Solicitando dados do usuario

name = input("Digite o nome do filme: ")
year = int(input("Digite o ano de lançamento do filme: "))
score = float(input("Digite a nota do filme: "))

# 4 - Inserindo dados

cursor.execute("""
    INSERT INTO movies (name, year, score)
    VALUES (?, ?, ?)
               """, (name, year, score))

# 5 - Gravando dados no BD
connection.commit()
print("Dados inseridos com sucesso!")

# 6 - Fechando a conexão
connection.close()