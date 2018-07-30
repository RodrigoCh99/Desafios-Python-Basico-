"""
    Escreva um programa que leia um número inteiro qualquer e peça para o usuario escolher
    qual será a base de conversão:
"""
print('\nESSE PROGRAMA É UM CONVERSOR DE BASES!')

print('*'*25)
print('Os codigos das bases são:')
print('1 para binario,\n2 para octal\n3 para hexadecimal')
print('*'*25)

num = int(input('\nInsira um valor para ser convertido: '))
base = int(input('Insira um codigo de base para conversão: '))

if base == 1:
    print('\nO valor {} em decimal \nEquivale a: {} em binario'.format(num, bin(num)[2:]))
elif base == 2:
    print('\nO valor {} em decimal \nEquivale a: {} em octal'.format(num, oct(num)[2:]))
elif base == 3:
    print('\nO valor {} em decimal equivale a: {} em hexadecimal'.format(num,hex(num)[2:]))
else:
    print('\nVoce digitou um codigo invalido!\nPor favor tente denovo!')