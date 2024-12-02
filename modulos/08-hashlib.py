import hashlib

# 1 - Verificar os algoritmos disponíveis
print(hashlib.algorithms_available)

# 2 - Algoritmos disponíveis de acordo com o SO
print(hashlib.algorithms_guaranteed)

# 3 - Utilizando o Sha256
algoritmo = hashlib.sha256()
print(algoritmo.digest())
mensagem = "A melhor forma de prever o futuro é criá-lo".encode()
print(algoritmo.hexdigest())

# 4 - Utilizando o MD5
md5 = hashlib.md5()
md5.update(mensagem)
print(md5.hexdigest())