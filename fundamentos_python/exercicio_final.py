times = {}
fim = False

# Função para listar times
def listar_times():
    print("Times Listados:")
    for i, time in enumerate(times.values()):
        print(f"{i+1}. {time['nome']} ({len(time['jogadores'])} jogadores)")

# Função para listar jogadores de um time
def listar_jogadores_time(time):
    print(f"Jogadores do {time['nome']}")
    for i, jogador in enumerate(time['jogadores']):
        print(f"{i+1}.{jogador}")

while not fim: 
    # Opcões do programa
    print("O que você deseja fazer?")
    print("1. Adicionar um time")
    print("2. Remover um time")
    print("3. Listar times")
    print("4. Adicionar jogador em um time")
    print("5. Remover jogador em um time")
    print("6. Listar jogadores de um time")
    print("7. Sair")
    
    opcao = input("Escolha uma opção\n")

    if opcao == "1":
        nome_time = input("Digite o nome do time\n")
        times[nome_time] = {'nome': nome_time, 'jogadores': []}
        print("Time adicionado!")
    
    elif opcao == "2":
        listar_times()
        numero_time = int(input("Digite no número do time que deseja remover\n"))
        if numero_time <= len(times):
            nome_time = list(times.keys())[numero_time -1]
            del times[nome_time]
            print("Time removido!")
        else:
            print("Número do time invalido")
    
    elif opcao == "3":
        listar_times()
    
    elif opcao == "4":
        listar_times()
        numero_time = int(input("Digite o número do time que deseja adicionar o jogador\n"))
        if numero_time <= len(times):
            nome_time = list(times.keys())[numero_time -1]
            nome_jogador = input("Informe o nome do jogador \n")
            times[nome_time]['jogadores'].append(nome_jogador)
            print("Jogador adicionado no time")
        else:
            print("Número do time invalido")
    
    elif opcao == "5":
        listar_times()
        numero_time = int(input("Digite o número do time que deseja remover o jogador\n"))
        if numero_time <= len(times):
            nome_time = list(times.keys())[numero_time -1]
            listar_jogadores_time(times[nome_time])
            numero_jogador = int(input("Informe o número do jogador que deseja remover\n"))
            if numero_jogador <= len(times[nome_time]['jogadores']):
                del times[nome_time]['jogadores'][numero_jogador -1]
                print("Jogador removido do time")
            else:
                print("Número do time inválido")
    
    elif opcao == "6":
        listar_times()
        numero_time = int(input("Digite o número do time que deseja listar os jogadores\n"))
        if numero_time <= len(times):
            nome_time = list(times.keys())[numero_time -1]
            listar_jogadores_time(times[nome_time])
        else:
            print("Nome do time inválido")
    
    elif opcao == "7":
        fim = True
        
    else:
        print("Opcão invalida.")
    