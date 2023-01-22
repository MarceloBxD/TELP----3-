# Importando biblioteca datetime
import datetime

# Funcao aposentadoria é possivel ou não
flag_aposentadoria = None

# Dias no ano
dias_no_ano = 365

def tempo_para_aposentadoria(idade, tempo_contribuicao, sexo):
    if(sexo == "m"):
        if(idade < 65 and tempo_contribuicao < (35 * dias_no_ano)):
            tempo_para_aposentadoria_por_idade = 65 - idade
            tempo_para_aposentadoria_por_tempo_contribuicao = (35 * dias_no_ano) - tempo_contribuicao
            print(f"Você ainda não pode se aposentar, faltam {tempo_para_aposentadoria_por_idade} anos e {tempo_para_aposentadoria_por_tempo_contribuicao} para você se aposentar p/ idade.")
        elif (idade < 65 and tempo_contribuicao >= (35 * dias_no_ano)):
            tempo_para_aposentadoria_por_idade = 65 - idade
            print(f"Você ainda não pode se aposentar por idade, faltam {tempo_para_aposentadoria_por_idade} anos para você se aposentar.")
        elif (idade >= 65 and tempo_contribuicao < (35 * dias_no_ano)):
            tempo_para_aposentadoria_por_tempo_contribuicao = (35 * dias_no_ano) - tempo_contribuicao
            print(f"Você ainda não pode se aposentar por tempo de contribuição, faltam {tempo_para_aposentadoria_por_tempo_contribuicao} dias para você se aposentar.")
        else:
            print("Você já pode se aposentar!")
    elif(sexo == "f"):
        if(idade < 62 and tempo_contribuicao < (30 * dias_no_ano)):
            tempo_para_aposentadoria_por_idade = 62 - idade
            tempo_para_aposentadoria_por_tempo_contribuicao = (30 * dias_no_ano) - tempo_contribuicao
            print(f"Você ainda não pode se aposentar, faltam {tempo_para_aposentadoria_por_idade} anos e para você se aposentar.")
        elif (idade < 62 and tempo_contribuicao >= (30 * dias_no_ano)):
            tempo_para_aposentadoria_por_idade = 62 - idade
            print(f"Você ainda não pode se aposentar por idade, faltam {tempo_para_aposentadoria_por_idade} anos e para você se aposentar.")
        elif (idade >= 62 and tempo_contribuicao < (30 * dias_no_ano)):
            tempo_para_aposentadoria_por_tempo_contribuicao = (30 * dias_no_ano) - tempo_contribuicao
            print(f"Você ainda não pode se aposentar por tempo de contribuição, faltam {tempo_para_aposentadoria_por_tempo_contribuicao} dias para você se aposentar.")
        else:
            print("Você já pode se aposentar!")

# Função para calcular o número de dias trabalhados
def dias_trabalhados(data_admissao, data_demissao):
    data_admissao_formatada = datetime.datetime.strptime(data_admissao, "%d/%m/%Y")
    data_demissao_formatada = datetime.datetime.strptime(data_demissao, "%d/%m/%Y")
    quantidade_de_dias = abs((data_demissao_formatada - data_admissao_formatada).days)
    return quantidade_de_dias

# Main do programa

# Pedindo dados ao usuário
genero = input("Digite o seu sexo: [m]asculino [f]eminino: ").lower()
idade = int(input("Digite a sua idade: "))
quantidade_empregos = int(input("Digite a quantidade de empregos que você já teve: "))

# Criando variável dias_totais_trabalhados e inicializando como 0
dias_totais_trabalhados = 0

if(quantidade_empregos == 0):
    print("Você ainda não trabalhou, portanto não temos como calcular a quantidade de dias trabalhados.")

for i in range(quantidade_empregos):
    data_admissao = input(f"Insira a data em que você foi admitido do trabalho {i+1} (dd/mm/aaaa): ")
    data_demissao = input(f"Insira a data em que você foi demitido do trabalho {i+1}(dd/mm/aaaa): ")
    dias_totais_trabalhados += dias_trabalhados(data_admissao, data_demissao)

# Chamando a função tempo_para_aposentadoria
tempo_para_aposentadoria(idade, dias_totais_trabalhados, genero)




