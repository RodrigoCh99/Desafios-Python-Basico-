"""
    Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
     jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'pPiI':
        tipo = str(input('PAR ou IMPAR[P/I]: ')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o computador {computador}. Total de {total} ',end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCE VENCEU')
            v = v + 1
        else:
            print('VOCE PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCE VENCEU!')
            v = v + 1
        else:
            print('VOCE PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Voce ganhou {v} vezes')

""" #primeiro modo, sem ajuda do professor!
from random import randint
valorj = 0
valorpc = randint(0,10)
c = 1
cont = 0
escolha = str('')
print('\nJOGO DE PAR OU IMPAR CONTRA O COMPUTADOR!')
while c > 0:
    valorj = int(input('Digite um valor: '))
    escolha = str(input('PAR OU IMPAR?[P/I] ')).upper()

    if (valorj + valorpc) % 2 == 0: #par
        if escolha == 'P':
            print(f'\nVoce jogou {valorj} e o computador {valorpc} . Total deu {valorj + valorpc} ou seja PAR ')
            print('Parabéns pela vitoria!\n\nVAMOS JOGAR NOVAMENTE!')
            cont += 1
            valorpc = randint(0, 10)
        if escolha == 'I':
            print(f'\nVoce jogou {valorj} e o computador {valorpc} . Total deu {valorj + valorpc} ou seja PAR ')
            print('\nVoce perdeu!')
            break
    elif (valorj + valorpc) % 2 == 1: #impar
        if escolha == 'P':
            print(f'\nVoce jogou {valorj} e o computador {valorpc} . Total deu {valorj + valorpc} ou seja IMPAR ')
            print('\nVoce perdeu!')
            break
        elif escolha == 'I':
            print(f'\nVoce jogou {valorj} e o computador {valorpc} . Total deu {valorj + valorpc} ou seja IMPAR ')
            print('Parabéns pela vitoria!\nVAMOS JOGAR NOVAMENTE!')
            cont += 1
            valorpc = randint(0, 10)
print(f'Voce ganhou {cont} de nossas partidas! ')
"""








