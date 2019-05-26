print("")
listatele = {}
def menu():
    print("")
    print("Lista Telefônica:")
    print("...Menu...")
    print("(1) Inserir Nome e Número")
    print("(2) Remover um Nome")
    print("(3) Alterar um Número")
    print("(4) Visualizar a lista")
    print("(5) Pesquisar um Número pelo Nome")
    print("")
    opcao = input("Opção: ")
    if opcao == "1":
        nome = input("Nome a ser inserido: ")
        numero = input("Número a ser inserido: ")
        listatele[nome] = numero
        print("Nome e número inseridos...")
        print("")
        menu()
    elif opcao == "2":
        nome = input("Nome a ser removido: ")
        del listatele[nome]
        print("Nome removido da lista...")
        print("")
        menu()
    elif opcao == "3":
        nome = input("Nome correspondente ao número: ")
        numero = input("Novo número a ser atribuido: ")
        listatele[nome] = numero
        print("Número atualizado")
        print("")
        menu()
    elif opcao == "4":
        print("A lista telefônica possui os seguintes registros: ")
        print(listatele)
        menu()
    elif opcao == "5":
        nome = input("Nome correspondente ao número: ")
        print("O número localizado foi",listatele[nome])
        menu()
    else:
        print("Opção Inválida...")
menu()

