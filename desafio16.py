"""
Desafio 16: Crie um programa que leia um número Real qualquer
pelo teclado e mostre na tela a sua porção inteira.

ex:
Digite um número:6.127
O numero 6.127 tem a parte inteira: 6

"""
from math import trunc #coloca a função trunc da biblioteca math no programa
num = float(input('Digite um número: ')) #coloca o valor copleto na variavel num
print('\nO número {} tem a parte inteira: {} '.format(num,trunc(num))) #informa o valor do numero e depois o valor usando a função math.trunc
