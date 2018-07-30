"""
    Crie um Programa que faça o computador jogar
     pedra papel tesoura com voce!
"""
from random import randint
print('\nVamos jogar pedra, papel e tesoura?')
numc = randint(1,3)
print('-'*25)
print('Escolha [1] para pedra\nEscolha [2] para papel\nEscolha [3] para tesoura')
print('-'*25)
numj = int(input('qual a sua escolha? '))
if numj == 1:
    if numc == 1:
        print('\nEMPATE!\nNós 2 jogamos pedra')
    elif numc == 2:
        print('\nEU GANHEI!\nEu joguei papel e voce pedra')
    else:
        print('\nVOCE GANHOU!\nEu joguei tesoura e voce pedra')
elif numj == 2:
    if numc == 1:
        print('\nVOCE GANHOU!\nEujoguei pedra e voce papel')
    elif numc ==2:
        print('\nEMPATE!\nNós dois jogamos papel')
    else:
        print('\nEU GANHEI!\nVoce escolheu papel e eu tesoura')
else:
    if numc == 1:
        print('\nEU GANHEI!\nEU escolhi pedra e voce tesoura')
    elif numc == 2:
        print('\nVOCE GANHOU!\nEu escolhi papel e voce tesoura')
    else:
        print('\nEMPATE!\nNós dois escolhemos tesoura')

