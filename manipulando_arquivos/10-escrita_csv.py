import csv


name = input("Informe o nome da linguagem que deseja aprender\n")
category = input("Qual a categoria que a linguagem se encaixa?\n")

with open("manipulando_arquivos/dados/courses.csv", "a", encoding="utf-8") as file:
    writer = csv.writer(file, lineterminator="\n")
    writer.writerow([name, category])