numero = int(input("Digite o número da tabuada\n"))
inicio = int(input("A tabuada começa em qual número?\n"))
fim = int(input("E acaba em qual número?\n"))

print(f"\nTabuada do número {numero} de {inicio} a {fim}.")
for i in range(inicio, fim + 1):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
