"""

    Maior e Menor Valores na Lista:
     Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre
     qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

"""
num = []
maior = 0
menor = 0
for c in range(0, 5):
    num.append(int(input(f'Informe um numero para a posição {c}: ')))
    if c == 0:
        maior = num[c]
        menor = num[c]
    else:
        if num[c] > maior:
            maior = num[c]
        elif num[c] < menor:
            menor = num[c]
print('--'*20)
print(f'Voce digitou os valores {num}')
print(f'O maior deles foi {maior} nas posições: ', end='')
for i, v in enumerate(num):
    if v == maior:
        print(f'{i}...', end='')
print(f'\nO menor deles foi {menor} nas posições: ', end='')
for i, v in enumerate(num):
    if v == menor:
        print(f'{i}...', end='')



