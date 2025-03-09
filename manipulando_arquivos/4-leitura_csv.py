# Abre o arquivo CSV contendo os dados dos cursos
with open("manipulando_arquivos/dados/courses.csv", "r", encoding="utf=8") as file:
    # Itera sobre cada linha do arquivo
    for line in file:
        # Divide a linha em duas partes: language e category, usando a vírgula como separador
        language, category = line.rstrip().split(",")
        
        # Exibe o conteúdo formatado: "linguagem - categoria"
        print(f"{language} - {category}")