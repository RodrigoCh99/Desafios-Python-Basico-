"""
    Desenvolva um programa que leia o comprimento de 3 retas
    e diga ao usuario se elas podem ou não formar um triangulo.
"""

print('\nEsse programa responde se as retas informadas podem ou nção formar um triangulo!')
r1 = float(input('\nInforme o comprimento da primeira reta: '))
r2 = float(input('Informe o comprimento da segunda reta: '))
r3 = float(input('Informe o comprimento da terceira reta: '))
if (r2 - r3) < r1 < (r2 + r3) and (r1-r3) < r2 < (r1 + r3) and (r1 - r2) < r3 < (r1 + r2):
    print('\nEssas retas formam um triangulo!')
else:
    print('\nEssas retas não formam um triangulo!')
