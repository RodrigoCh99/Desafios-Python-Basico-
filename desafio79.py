"""

    Valores Únicos em uma Lista
     Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
     Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os
     valores únicos digitados, em ordem crescente.

"""
n = 0
num = []
escolha = ' '
print('--'*15)
while True:
    n = (int(input('Insira um número: ')))
    if n not in num:
        num.append(n)
    else:
        print('número duplicado. Não será adicionado!', end='\n')
    escolha = str(input('Deseja continuar[S/N]: ')).upper()[0]
    print('--'*15)
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar[S/N]: ')).upper()[0]
    if escolha == 'N':
        break
num.sort()
print(f'Os números infoemados em ordem são: {num}')