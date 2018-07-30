"""
    Dividindo Valores em Várias Listas
     Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, cria duas listas extras que vão
     conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das
     três listas geradas.

"""

n = 0
escolha = ' '
num = []
pares = []
impares = []
while True:
    print('--'*15)
    n = int(input('Insira um valor: '))
    num.append(n)
    if n % 2 == 0:
        pares.append(n)
    elif n % 2 != 0:
        impares.append(n)
    escolha = str(input('Deseja continuar[S/N]: ')).upper()
    if escolha not in 'SN':
        escolha = str(input('Deseja continuar[S/N]: ')).upper()
    elif escolha == 'N':
        break
print('--'*15)
print(f'A lista de números gerados foi: {num} ')
print(f'A lista de numeros PARES foi: {pares} ')
print(f'A lista de numeros impares foi: {impares} ')