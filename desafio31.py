"""
     Desenvolva um programa que pergunta a distancia de uma viagem em Km.
     Calcule o preço da passagem, cobrando R$0.50 por Km para viagens até 200Km
     e R$0.45 para viagens mais longas
"""
print('\nEsse programa calcula o preço da passagem de uma viagem!')
dist = float(input('\nInforme a distancia da viagem em Km: '))
if dist <= 200:
    print('\nO preço da viagem será: R${:.2f}'.format(dist*0.50))
else:
    print('\nO preço da viagem será: R${:.2f}'.format(dist*0.45))