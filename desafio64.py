"""
    Crie um programa que leia vários números inteiros pelo teclado. O programa
     só vai ser parado quando o usuario digitar 999, que é a condição de parada.
     No final mostre quantos números foram digitados e qual foi a soma entre eles
     (DESCONCIDERANDO O FLAG[999]).
"""
print('Digite [999] para parar')
num = 0
soma = 0
cont = 0
num = int(input('Digite um número: '))
while num != 999:
    soma = soma + num
    cont += 1
    num = int(input('Digite um número: '))
print('\nVocê digitou {} números e a soma entre eles foi {}'.format(cont, soma))
print('FIM')
