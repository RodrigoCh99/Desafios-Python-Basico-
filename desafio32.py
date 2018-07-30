"""
    Faça um programa que leia um ano e descubra se ele é bissexto!
"""
print('\nESSE PROGRAMA DESCOBRE SE UM ANO É BISSEXTO!')
ano = int(input('\nInsira um ano: '))
if (ano % 4) == 0 and (ano % 100)!= 0 or (ano % 400) == 0:
    print('\nEsse ano é bissexto!')
else:
    print('\nEsse ano não é bissexto!')