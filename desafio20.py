"""
 O mesmo professor do desafio anterior quer sortear a ordem de apresentação de
 trabalhos dos alunos. Faça um programa que leia o nome dos 4 alunos e mostre
 a ordem sorteada
"""

from random import shuffle
print('\nESSE PROGRAMA ESCOLHE EM QUAL ORDEM OS ALUNOS DEVEM APRESENTAR O TRABALHO') #titulo
a1 = str(input('\nInsira o nome do primeiro aluno: ')) #variaveis 1a4 lidas do teclado
a2 = str(input('Insia o nome do segundo aluno: '))
a3 = str(input('Insira o nome do terceiro aluno: '))
a4 = str(input('Insira o nome do quarto aluno: '))
lista = [a1, a2, a3, a4] # lista com as variaveis
shuffle(lista) # função do random para embaralhar
print('A ordem das apresentações será: {}'.format(lista)) #impresssão dos resultados

