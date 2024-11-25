gamesTuple = ("Fifa 23", "Red Dead 2", "Star Wars,"
              "Mario Odissey", "The Legend of Zelda")
print(gamesTuple)
print(type(gamesTuple))
#name = ("Rodrigo",)
#print(type(name))

# 1 - Buscar os dois primeiros itens da tupla
print(gamesTuple[:2])

# 2 - Buscar o ultimo item da lista
print(gamesTuple[-1])

# 3 - Buscar jogos até uma determinada posiçao
print(gamesTuple[:3])

# 4 - Buscar jogos de uma posiçao em diante
print(gamesTuple[2:])

# 5 - Recuperar um item da tupla pelo indice
print(gamesTuple.index("Red Dead 2"))

# - Não possibilita adicionar valores na tupla
# - Não possibilita remover valores na tupla
# - Não possibilita ordenar valores na tupla
