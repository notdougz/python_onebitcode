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

# Exibe a lista completa de cursos
print(courses)

# Função para obter o nome da linguagem de programação do curso
def get_language(course):
    return course["language"]

# Função para obter a categoria do curso
def get_category(course):
    return course["category"]

# Percorre a lista de cursos e imprime cada um no formato "Linguagem - Categoria"
print("\nLista de Cursos:")
for course in courses:
    print(f"{course['language']} - {course['category']}")

# Ordena os cursos por categoria em ordem decrescente e exibe novamente
print("\nLista de Cursos Ordenados por Categoria (Decrescente):")
for course in sorted(courses, key=get_category, reverse=True):
    print(f"{course['language']} - {course['category']}")
