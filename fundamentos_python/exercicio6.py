string = "Escreva uma função Python que Receba uma String e conte o número de letras maiúsculas e minúsculas desta string."

maiusculas = 0
minusculas = 0

for letra in string:
    if letra.isupper():
        maiusculas += 1
    else:
        minusculas += 1
print(f"Letras maiúsculas: {maiusculas}")
print(f"Letras minúsculas: {minusculas}")

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = []
impares = []

for numero in lista_numeros:
    if numero % 2 == 0:
        pares.append(numero)
    
    else:
        impares.append(numero)

print(pares)
print(impares)