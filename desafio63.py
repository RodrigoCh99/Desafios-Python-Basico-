"""
    Escreva um programa que leia um número 'n' inteiro qualquer e mostre na
     tela os 'n' primeiros elementos de uma sequencia de fibonacci.
    EX:
     0 > 1 > 1 > 2 > 3 > 5 > 8.
"""
c = 3
n1 = 0
n2 = 1
n3 = n1 + n2
quantidade = int(input('Quantos elementos você deseja ver? '))
print('{} -> {}'.format(n1,n2),end=' -> ')
while c <= quantidade:
    print('{}'.format(n3),end=' -> ')
    n1 = n2
    n2 = n3
    n3 = n1 + n2
    c += 1
print('FIM')






