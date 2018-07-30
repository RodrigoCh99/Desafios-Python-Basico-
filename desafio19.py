"""
 Um professor quer sortear um dos seus quatro alunos para apagar
 o quadro. Faça um programa que ajude ele, lendo o nome do escolhido.
"""

import random
n1 = str(input('Insira o nome do primeiro aluno: ')) #variaveis 1-4
n2 = str(input('Insira o nome do segundo aluno: '))
n3 = str(input('Insira o nome do terceiro aluno: '))
n4 = str(input('Insira o nome do quarto aluno: '))
lista = [n1, n2,n3, n4] #lista de variaveis em python sempre tem couchetes
escolhido = random.choice(lista) # variavel recebe o valor de outra variavel presente na lista
print('\nO aluno escolhido para limpar o quadro foi: {}'.format(escolhido))