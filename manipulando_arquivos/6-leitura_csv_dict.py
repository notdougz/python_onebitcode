# Lista para armazenar os cursos lidos do arquivo
courses = []

# Abre o arquivo CSV que contém os cursos
with open("manipulando_arquivos/dados/courses.csv", "r", encoding="utf-8") as file:
    # Percorre cada linha do arquivo
    for line in file:
        # Remove espaços extras e divide a linha pelos caracteres de vírgula
        language, category = line.rstrip().split(",")

        # Cria um dicionário para armazenar as informações do curso
        course = {}
        course["language"] = language  # Armazena a linguagem de programação
        course["category"] = category  # Armazena a categoria do curso

        # Adiciona o dicionário na lista de cursos
        courses.append(course)

# Exibe a lista completa de cursos (formato de dicionário)
print(courses)

# Percorre a lista de cursos e imprime cada um no formato "Linguagem - Categoria"
print("\nLista de Cursos:")
for course in courses:
    print(f"{course['language']} - {course['category']}")
