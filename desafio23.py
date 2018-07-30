"""
 Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.

 ex:
 digite um numero: 1834

 unidades:4
 dezenas:3
 centenas:8
 milhar:1

"""

print('\nEsse programa informa as casas decimais de um numero informado!')
n = str(input('\nInforme um numero: ')).zfill(4)
n = '0000' + str(n)
print('*'* 20)
print('{} unidades'.format(n[-1]))
print('{} dezenas'.format(n[-2]))
print('{} centenas'.format(n[-3]))
print('{} milhares'.format(n[-4]))
print('*'*20)







