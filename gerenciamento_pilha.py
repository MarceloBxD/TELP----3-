"""Crie um programa para gerenciar uma pilha de processos em python. Cada Processo possui um identificador único (id) e 
 uma descrição (string)
 Você deverá pedir ao usuário para escolher se deseja encerrar, incluir ou retirar um processo da pilha. 
 Se a operação for uma inclusão, colocar o processo
 na pilha e imprimir o novo estado dessa; se for uma exclusão,
 caso a pilha não esteja vazia, imprimir "removido o processo #identificador - Descrição
 da pilha" e mostrar o conteúdo atual dela; se a pilha estiver vazia, mostrar "pilha vazia". Se o usuário escolher encerrar, 
 encerre o programa!"""

pilha = []

while True:
    print("<---------- Gerenciador de Processos ---------->")
    print('''
    1 - Encerrar
    2 - Incluir
    3 - Retirar
    ''')
    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
        print("\t\t<---------- Encerrando ---------->\n")
        pilha.clear()
        print("Encerrando...")
        print(f"Pilha esvaziada: {pilha}")
        break
    elif opcao == 2:
        print("\t\t<---------- Incluindo item ---------->\n")
        id = int(input('Digite o id: '))
        if id in pilha:
            print("Id já existe")
            continue
        descricao = input('Digite a descrição: ').lower()
        if descricao in pilha:
            print("Descrição já existe")
            continue
        pilha.append(id)
        pilha.append(descricao)
        print(pilha)
    elif opcao == 3:
        print("\t\t<---------- Removendo item ---------->\n")
        if len(pilha) == 0:
            print("Pilha vazia")
        elif len(pilha) > 0:
            print("Removido o processo {} - {}".format(pilha[0], pilha[1]))
            pilha.pop(0)
            pilha.pop(0)
            print(pilha)

