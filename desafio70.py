"""
    Crie um programa que leia o nome e o preço de vários produtos. O programa
     deverá perguntar se o usuário vai continuar. No final, mostre:
    EX:
        A) Qual é o total gasto na compra.
        B) Quantos produtos custam mais de R$ 1000.
        C) Qual é o nome do produto mais barato.
"""
total = 0
caros = 0 # produtos > 1000.00
pbarato = 0
nbarato = ''
c = 0
print('--'*7,'LOJA DO RODRIGO','--'*7)

while True:
    print('--'*20)
    nome = str(input('Informe o nome do produto: ')).strip().upper()
    preço = float(input('Informe o preço do produto: '))
    c += 1
    total += preço
    if c == 1:
        nbarato = nome
        pbarato = preço
        c += 1
    else:
        if preço < pbarato:
            pbarato = preço
            nbarato = nome
    if preço > 1000:
        caros += 1
    escolha = ' '

    print('--'*20)
    while escolha not in 'SN':
        escolha = str(input('Quer continuar?[S/N]: ')).strip().upper()[0]
    if escolha == 'N':
        break
print('--'*20)
print('--'*7,'INFORMAÇÕES DO CAIXA','--'*7,end='\n')
print(f'\nO total gasto na compra foi de: R$:{total:.2f}')
print(f'Temos {caros} produtos custando mais de R$:1000.00')
print(f'O produto mais barato foi {nbarato} que custa R$:{pbarato:.2f}')

