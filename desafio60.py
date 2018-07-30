"""
    Faça um programa que leia um número qualquer e mostre o seu fatorial.
     EX:
       5! = 5 * 4 * 3 * 2 * 1 = 120.
"""

num = int(input('\nInforme um número: '))
cont = num
multi = 1
print('{}! = '.format(num),end='')
while cont >= 1:
    print('* {} '.format(cont),end='')
    multi = cont * multi
    cont = cont - 1
print('= {}'.format(multi))




