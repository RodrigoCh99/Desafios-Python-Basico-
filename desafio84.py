"""
    DESAFIO 084: Lista Composta e Análise de Dados
     Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:

    A) Quantas pessoas foram cadastradas.
    B) Uma listagem com as pessoas mais pesadas.
    C) Uma listagem com as pessoas mais leves.

"""
cadastro = list()
dados = list()
escolha = ' '
pesado = 0
npesado = ' '
while True:
    dados.append(str(input('Qual o seu nome: ')))
    dados.append(float(input('Qual o seu peso: ')))

    if len(cadastro) == 0:
        pesado = dados[1]
        npesado = dados[0]
    else:
        if dados[1] > pesado:
            pesado = dados[1]
            npesado = dados[0]

    cadastro.append(dados[:])
    dados.clear()
    print('--'*15)
    escolha = str(input('Quer continuar[S/N]: ')).upper()
    print('--'*15)
    if escolha not in 'SN':
        escolha = str(input('Quer continuar[S/N]: ')).upper()
    elif escolha == 'N':
        break
print('=-'*15)
print(f'Foram cadastradas {len(cadastro)} pessoas!')
print(f'O maior peso foi {pesado} Kg de:')
for n in dados:
    if p[1] == pesado:
        print(f' - {p[0]}')
print('As pessoas mais leves cadastradas são: ')
for p in cadastro:
    if p[1] < pesado:
        print(f' - {p[0]}')

print('=-'*15)







#print(f'\nE são elas: {cadastro}')