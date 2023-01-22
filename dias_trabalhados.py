import datetime

# Criando uma função que recebe a data de admissão e demissão, e retorna a quantidade de dias trabalhados.

def dias_trabalhados(data_admissao, data_demissao):
    data_admissao_formatada = datetime.datetime.strptime(data_admissao, "%d/%m/%Y")
    data_demissao_formatada = datetime.datetime.strptime(data_demissao, "%d/%m/%Y")
    quantidade_de_dias = abs((data_demissao_formatada - data_admissao_formatada).days)
    return quantidade_de_dias

# Pedindo os dados do usuário

print("<--------------- Quantidade de dias trabalhados -------------->\n")

data_nascimento = input("Insira a data em que você nasceu (dd/mm/aaaa): ")
numero_trabalhos = int(input("Insira o número de trabalhos que você já teve: \n"))
dias_totais_trabalhados = 0

if(numero_trabalhos == 0):
    print("Você ainda não trabalhou, portanto não temos como calcular a quantidade de dias trabalhados.")

for i in range(numero_trabalhos):
    data_admissao = input(f"Insira a data em que você foi admitido do trabalho {i+1} (dd/mm/aaaa): ")
    data_demissao = input(f"Insira a data em que você foi demitido do trabalho {i+1}(dd/mm/aaaa): \n")
    dias_totais_trabalhados += dias_trabalhados(data_admissao, data_demissao)

print("Você trabalhou por", dias_totais_trabalhados, "dias!")