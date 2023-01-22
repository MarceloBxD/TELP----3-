from fila import limpa_tela, verifica_fila_vazia, inclui_cliente, atende_proximo_cliente

# Criando lista para armazenar a fila
lista_fila = []

# Criando loop principal
while True:
    limpa_tela()
    print("<--------------- Atendimento de fila -------------->\n")
    print("1 - Consultar a fila atual")
    print("2 - Incluir alguém na fila")
    print("3 - Atender ao próximo cliente")
    print("4 - Sair")

    opcao = int(input("\nEscolha uma opção: "))
    if(opcao == 1):
        verifica_fila_vazia(lista_fila)
        input("Pressione ENTER para continuar...")
    elif(opcao == 2):
        nome_cliente = input("Insira o nome do cliente: ")
        rg_cliente = input("Insira o RG do cliente: ")
        inclui_cliente(nome_cliente, rg_cliente, lista_fila)
        input("Pressione ENTER para continuar...")
    elif(opcao == 3):
        atende_proximo_cliente(lista_fila)
        input("Pressione ENTER para continuar...")
    elif(opcao == 4):
        break
    else:
        print("Opção inválida!")
        input("Pressione ENTER para continuar...")