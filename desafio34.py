"""
    Escreva um programa que pergunte o salario e calcule o valor do aumento.
        para salarios superiores a R$1250.00,calcule o aumento de 10%.
        para os inferiores ou iguais, o aumento é de 15%
"""

print('\nESSE PROGRAMA CALCULA O AUMENTO NO SALARIO DOS FUNCIONARIOS!')
sal = float(input('Qual o seu salario: '))

if sal > 1250.00:
    print('\nO seu novo salario é: R${:.2f}'.format(sal + ((sal/100) * 10)))
else:
    print('\nOseu novo salario será: R${:.2f}'.format(sal + ((sal/100) * 15)))

