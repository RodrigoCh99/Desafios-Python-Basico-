"""

    Maior e Menor Valores em Tupla:
     Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
     Depois disso, mostre a listagem de números gerados e também indique o menor e o
     maior valor que estão na tupla.

"""
cont = 0
maior = 0
menor = 0
from random import randint
num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
for cont in range(0, len(num)):
    if cont == 0:
        maior = num[cont]
        menor = num[cont]
    elif cont != 0:
        if num[cont] > maior:
            maior = num[cont]
        elif num[cont] < menor:
            menor = num[cont]
print(f'Os valores sorteados foram {num}')
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
