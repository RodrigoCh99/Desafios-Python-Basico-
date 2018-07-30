"""
Faça um programa que leia o comprimento do cateto oposto e do cateto
adjacente de um triângulo retãngulo. Calcule e mostre o comprimento
da hipotenusa

"""
""" primeiro modo:
from math import pow,sqrt,trunc  #importa algumas funções do modulo math
print('\nESSE PROGRAMA CALCULA O COMPRIMENTO DA HIPOTENUSA\nAPARTIR DO VALOR DO COMPRIMENTO DOS CATETOS!') #titulo

ca = float(input('\nInforme o valor do cateto adjacente: '))#insere o valor lido do teclado na variavel cateto adjacente
co = float(input('Informe o valor do cateto oposto: '))#insere o valor lido do teclado na variavel cateto oposto
hip = pow(ca, 2) + pow(co, 2)#calcula o valor da hipotenusa ao quadrado e inseere na variavel hip

print('A partir do cateto adjacente {} e do cateto oposto: {} é possivel descobrir uma hipotenusa igual á: {}'.format(ca,co,trunc(sqrt(hip)))) #mostra os valores lidos e a hipotenusa resultante de seus valores de forma arredondada
"""

#segundo modo:

import math #importa o modulo que será necessario para os calculos da questão.
print('\nESSE PROGRAMA CALULA A HIPOTENUSA APARTIR DOS SEUS CATETOS!') #titulo.

co = float(input('insira o valor do cateto oposto: '))#insere o valor lido do teclado na variavel.
ca = float(input('insira o valor do cateto adjacente: '))#insere o valor lido do teclado na vaiavel.
hi = math.hypot(co,ca) #utiliza funções especificas do modulo para fazer um calculo de maneira mais concisa.
print('\n\nO valor da hipotenusa é: {}'.format(math.trunc(hi)))#imprime o valor calculado na tela arredondado para cima.