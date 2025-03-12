import csv  # Importa o módulo CSV para manipulação de arquivos no formato CSV.

# Lista que armazenará os cursos extraídos do arquivo CSV
courses = []

# Abre o arquivo 'courses.csv' localizado no diretório 'manipulando_arquivos/dados' para leitura
with open("manipulando_arquivos/dados/courses.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)  # Lê o arquivo CSV e converte cada linha em um dicionário
    for row in reader:  # Itera sobre cada linha do arquivo
        # Adiciona um dicionário com os campos 'language' e 'category' na lista 'courses'
        courses.append({"language": row["language"], "category": row["category"]})
        
        # Exibe a lista 'courses' a cada iteração, mostrando os cursos lidos até o momento
        print(courses)

for course in sorted(courses, key=lambda course: course["language"]):  # Ordena a lista de cursos pelo campo 'language'
    print(f"{course['language']} - {course['category']}")  # Exibe o curso formatado com a linguagem e a categoria