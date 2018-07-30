"""
    Escreva um programa que leia dois numeros inteiros e compare-os
     mostrando na tela a mensagem:
    EX:
    > O primeiro valor é maior
    > O segundo valor é maior
    > Não existe valor maior, os dois são iguais
"""

print('\ESSE PROGRAMA COMPARA 2 NÚMEROS INTEIROS!')

n1 = int(input('\nInforme o valor do primeiro número: '))
n2 = int(input('Informe o valor do segundo número: '))

if n1 > n2:
    print('\nO numero {} é o maior'.format(n1))
elif n2 > n1:
    print('\nO número {} é o maior'.format(n2))
else:
    print('\nOs número informados são iguais, portanto nenhum é maior que o outro')