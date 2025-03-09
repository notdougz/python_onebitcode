# Lista vazia para armazenar os cursos
courses = []

# Abre o arquivo CSV contendo os dados dos cursos
with open("manipulando_arquivos/dados/courses.csv", "r", encoding="utf=8") as file:
    # Itera sobre cada linha do arquivo
    for line in file:
        # Remove espaços em branco no final da linha e divide a linha em duas partes: language e category
        language, category = line.rstrip().split(",")
        
        # Formata os dados e adiciona à lista de cursos
        courses.append(f"{language} - {category}")
        
        # Exibe a lista de cursos atualizada a cada iteração (para fins de depuração)
        print(courses)

# Ordena a lista de cursos em ordem decrescente (reverse=True) e imprime cada curso
for course in sorted(courses, reverse=True):
    print(course)