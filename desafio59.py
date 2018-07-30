"""
    Crie um programa que leia dois valores e mostre um menu na tela:
        [1] SOMAR
        [2] MULTIPLICAR
        [3] MAIOR
        [4] NOVOS NÚMEROS
        [5] SAIR DO PROGRAMA
    Seu programa deverá realizar a operação solicitada em cada caso.
"""
#variaveis
n1 = int(input('\nInforme um número: '))
n2 = int(input('Informe outro número: '))
opção = 0


#laço de repetição
while opção != 5:
    print('=-='*10)
    print("""    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA""")
    opção = int(input('Qual é a sua opção? '))

#estruturas de decisão dentro do laço
    if opção == 1:
        print('A soma dos números informados é: {}'.format(n1+n2))
    elif opção == 2:
        print('A multiplicação dos números informados é: {}'.format(n1*n2))
    elif opção == 3:
        if n1 > n2:
            print('O número {} é o maior!'.format(n1))
        elif n2 > n1:
            print('O número {} é o maior'.format(n2))
        else:
            print('Os números são iguais')
    elif opção == 4:
        print('Informe os número novamente! ')
        n1 = int(input('\nInforme um número: '))
        n2 = int(input('Informe outro número: '))
    elif opção == 5:
        print('\nFinalizando!')

print('\nFim do programa!')