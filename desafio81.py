"""
    Extraindo Dados de uma Lista
     Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:

    A) Quantos números foram digitados.
    B) A lista de valores, ordenada de forma decrescente.
    C) Se o valor 5 foi digitado e está ou não na lista.

"""

lista = []
escolha = ' '
print('--'*15)
while True:
    lista.append(int(input('Insira um valor: ')))
    escolha = str(input('Deseja continuar[S/N]: ')).upper()[0]
    if escolha not in 'SN':
        escolha = str(input('Deseja continuar[S/N]: ')).upper()[0]
    elif escolha == 'N':
        break
    print('--'*15)
print('--'*15)
print(f'\nA lista formada pelos valores informados é {lista}')
print(f'Foram digitados {len(lista)} valores')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente é {lista}')
if 5 in lista:
    print('O valor 5 foi digitado!')
else:
    print('O valor 5 não foi digitado!')