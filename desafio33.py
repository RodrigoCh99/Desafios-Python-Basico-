"""
    Escreva um programa que leia 3 números inteiros e mostre qual é o maior e qual é o menor
"""

print('\nESSE PROGRAMA RECEBER 3 NÚMEROS E INFORMA O MAIOR E O MENOR!')
num1 = int(input('\nInsira o primeiro número: '))
num2 = int(input('Insira o segundo número: '))
num3 = int(input('Insira o terceiro número: '))
if num1 > num2:
    if num1 > num3:
        print('\nO número {} é o maior!'.format(num1))
    else:
        print('\nO número {} é o meior!'.format(num3))
elif num2 > num3:
        print('\nO número {} é o maior!'.format(num2))
else:
        print('\nO número {} é o maior!'.format(num3))
if num1 < num2:
    if num1 < num3:
        print('\nO número {} é o menor!'.format(num1))
    else:
        print('\nO número {} é o menor!'.format(num3))
elif num2 < num3:
        print('\nO número {} é o menor!'.format(num2))
else:
        print('\nO número {} é o menor!'.format(num3))






