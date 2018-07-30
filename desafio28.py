"""
    Escreva um programa que faça o computador pensar em um numero entre 0 e 5
    e peça para o usuario tentar descobrir qual foi o número escolhido pelo computador.

    O programa deve escrever na tela se o jogador venceu ou perdeu a partida.

"""
import random
print('\nDescubra o numero que eu estou pensando!')
num = random.randint(0, 5)
pal = int(input("\nQual o seu palpite? "))
if pal == num:
    print('\nVoce acertou parabéns!!')
else:
    print('\nErrado!, eu pensei no número {} tente novamente!'.format(num))
