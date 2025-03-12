from agenda import add_contact, view_contacts, delete_contacts

def main():
    while True:
        print("\nAgenda de contatos")
        print("1. Adicionar Contato")
        print("2. Ver Contatos")
        print("3. Remover Contatos")
        print("4. Sair")
        
        choice = input("Escolha uma opção (1-4) \n")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            delete_contacts()
        elif choice == "4":
            break
        else:
            print("Opção inválida")
        
main()