"""
    Melhore o jogo do desafio 28 aonde o computador vai 'pensar' em um número
     entre 0 e 10. Só que agora o jogador vai tenatr adivinhar até acertar mos
     trando no final quantos palpites foram necessarios para vencer.
"""
from time import sleep
from random import randint
pc = randint(0,10)
jogador = -1
cont = 0
print('\nEsse proprama me permite ao jogador tentar adivinhar o n° em que o computador está pensando!')
sleep(1)
print('\nvamos começar!')
sleep(1)
print('VOU PENSAR EM UM NÚMERO DE 0 A 10...')
sleep(2)
print('PENSEI!')
while jogador != pc:
    jogador = int(input('\nQual o seu palpite? '))

    if jogador != pc:
        cont += 1
        if jogador > pc:
            print('\nMenos...')

        elif jogador < pc:
            print('\nMais...')

cont += 1
print('\nVoce acertou! o número que eu pensei era {}\nE voce só precisou de: {} palpites'.format(pc,cont))

