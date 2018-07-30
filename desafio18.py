"""
 Faça um programa que leia um ãngulo qualquer e mostre na tela
 o valor do seno, cosseno e tangente desse angulo.
"""

import math
print('\nESSE PROGRAMA MOSTRA O SENO, COSSENO E A TANGENTE DE QUALQUER ÃNGULO!')

angulo = int(input('\nInsira um ãngulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('Os valores são: \nSeno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(seno,cosseno,tangente))
