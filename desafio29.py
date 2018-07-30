"""
    Escreva um programa que leia a velocidade de um carro.
    Se ele ultrapassar 80km/h.mostre uma mensagem dizendo que ele foi multado.
    A multa vai custar R$:7,00 por cada km acima do limite.
"""

print('\nESSE PROGRAMA CALCULA SE A PESSOA FOI MULTADA E O VALOR DA MULTA!')
velo = float(input('\nInforme a valocidade que voce estava: '))
limit = 80
if velo >= limit:
    print('Voce foi multado!')
    print('O valor da multa será de: {:.2f}'.format((velo - 80)*7.00))
else:
    print('\nVoce não foi multado!')