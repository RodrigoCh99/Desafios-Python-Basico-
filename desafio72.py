"""
    Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por externso, de
    zero até vinte.
    Seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostra-lo por extenso.
"""

nome = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezeseis','dezesete','dezoito','dezenove','vinte')
print('--'*20)
while True:
    algarismo = int(input('Insira um algarismo entre 0 e 20: '))
    if algarismo <= 20 and algarismo >= 0:
        print(f'O numero digitado foi {nome[algarismo]}')
        break
    else:
        print('tente novamente, ',end='')
print('Obrigado Por Jogar!')
