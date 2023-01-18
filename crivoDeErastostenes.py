"""
O crivo de Erastóstenes é um dos mais antigos métodos para encontrar números primos. Basicamente, ele consiste em
Receber o valor limite, ou seja, o número até o qual você deseja encontrar todos os primos menores que ele.
Calcular sua raíz quadrada: se não for exata, arrendondar para baixo.
Criar uma lista de booleanos, com índices variando de 2 até o valor limite e incialmente todos com o valor True.
Fazer um loop com uma variável de controle, digamos i, variando de 2 até a raíz quadrada do valor limite, em que, a cada iteração, se o valor de i for True, então:
Faça um loop interno com varíavel de controle j; de i+1 até o valor limite e, a cada interação, marque o elemento de índice j na lista do item 3 como False.
Ao final da execução, todos os números marcados com True na lista do item 3 são primos.

Implemente o crivo na forma de um programa em Python, que perguntará ao usuário qual valor limite e imprimirá todos os primos entre 2 (inclusive) e o limite.
"""

# Importando bibliotecas
import math 
import pprint

limite = int(input("Diga o valor limite: "))
numeros = [True] * (limite + 1)
numeros[0], numeros[1] = False, False
raiz = int(math.sqrt(limite))
ehPrimo = []

# Criando loop

for i in range(2, limite):
    if(numeros[i] == True):
        ehPrimo.append(i)
        for j in range(i*2, limite, i):
            numeros[j] = False
pprint.pprint(ehPrimo, width=100)
print("A quantidade de números primos é: ", len(ehPrimo))
        
    

