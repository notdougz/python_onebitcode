import glob, os, zipfile

# 1 - Diretorio de trabalho atual
os.getcwd()

# 2 - Listar todos os arquivos .txt

for file in glob.glob("manipulando_arquivos/dados/*.txt"):
    print(file)
    
# 3 - Listar todos os arquivos .csv

for file in glob.glob("manipulando_arquivos/dados/*.csv"):
    print(file)
    
# 4 - Compactar arquivos .txt

with zipfile.ZipFile("names.zip", "w") as zip:
    for file in glob.glob("manipulando_arquivos/dados/*.txt"):
        zip.write(file)
        
# 5 - Compactar arquivos .zip

with zipfile.ZipFile("courses.zip", "w") as zip:
    for file in glob.glob("manipulando_arquivos/dados/*.csv"):
        zip.write(file)
        
 # 6 - Compactar todos os arquivos
 
with zipfile.ZipFile("code.zip", "w") as zip:
    for file in glob.glob("*"):
        zip.write(file)