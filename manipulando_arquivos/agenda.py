# Agenda de Contatos

# Desenvolva uma agenda de contatos persistindo as informações em arquivo. O programa deve seguir as especificidades:

# Criar o arquivo Agenda contendo quatro métodos: 

# Um método para adicionar contato.

# Um método para listar contatos.

# Um método para remover contatos.

# Criar um arquivo principal para a aplicação que importar o módulo de agenda e chamar cada um dos métodos desenvolvidos de acordo com a opção escolhida.

import os

def add_contact():
    name = input("Informe o nome do contato:\n")
    address = input("Informe o endereço:\n")
    phone = input("Informe o telefone\n")
    
    contact = f"Nome: {name} \nEndereço: {address} \nTelefone: {phone} \n"
    with open("manipulando_arquivos/dados/contacts.txt", "a", encoding="utf-8") as file:
        file.write(contact)
        
def view_contacts():
    if not os.path.exists("manipulando_arquivos/dados/contacts.txt"):
        print("Lista de contatos está vazia.")
        return
    
    with open("manipulando_arquivos/dados/contacts.txt", "r", encoding="utf-8") as file:
        contacts = file.read()
    
    print("Lista de Contatos:")
    print(contacts)
        
def delete_contacts():
    if not os.path.exists("manipulando_arquivos/dados/contacts.txt"):
        print("Lista de contatos vazia")
        return
    with open ("manipulando_arquivos/dados/contacts.txt", "w", encoding="utf-8") as file:
        file.write("")
    print("Contatos excluidos com sucesso")
        