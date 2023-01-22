"""Crie um programa que controlará a fila de atendimentos em uma recepção. O usuário deverá escolher entre:
Consultar a fila atual: Mostra quem está na fila no momento, por ordem de chegada.
Incluir alguém na fila: Coloca o nome e RG de um cliente na fila.
Atender ao próximo cliente: Quando selecionada esta opção, o primeiro cliente da fila será retirado desta e será mostrada a mensagem “Atendendo ao cliente nome do cliente — RG: RG do cliente”. Se a fila estiver vazia, exibir “Nenhum cliente a atender”."""

# Criando função para limpar tela
def limpa_tela():
    print("\033[H\033[J")

def verifica_fila_vazia(fila):
    if(len(fila) == 0):
        print("Fila está vazia!")
    else:
        print("Fila: ", fila)

def inclui_cliente(nome_cliente, rg_cliente, fila):
    fila.append([nome_cliente, rg_cliente])
    print("Cliente incluído com sucesso!")

def atende_proximo_cliente(fila):
    if(len(fila) == 0):
        print("Nenhum cliente a atender!")
    else:
        print("Atendendo ao cliente", fila[0][0], "— RG:", fila[0][1])
        fila.pop(0)



