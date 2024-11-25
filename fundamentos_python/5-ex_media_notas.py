# Lê a quantidade de alunos na turma
quantidade_alunos = int(input("Digite a quantidade de alunos na turma: "))

# Inicializa a soma das notas
soma_notas = 0

# Loop para ler a nota de cada aluno e somá-las
for i in range(quantidade_alunos):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    soma_notas += nota

# Calcula a média das notas
media = soma_notas / quantidade_alunos

# Exibe o resultado
print("A média das notas da turma é:", media)