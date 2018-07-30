"""
    Desenvolva uma lógica que leia o peso e a altura de uma pessoa
     e calcule seu IMC e mostre seu status, de acordo com a tabela
     abaixo:

     > Abaixo de 18.5: ABAIXO DO PESO
     > Entre 18.5 e 25: PESO IDEAL
     > 25 até 30: SOBREPESO
     > 30 até 40: OBESIDADE
     > Acima de 40: OBESIDADE MÓRBIDA
"""
from math import pow
print('\nESSE PROGRAMA CALCULA O SEU IMC E INFORMA SEU STATUS DE ACORDO COM OS PADRÕES DE SAÚDE!')
peso = float(input('Insira o seu peso: '))
altura = float(input('Insira a sua altura: '))
imc = peso/(pow(altura, 2))
print('\nO seu I.M.C é igual a: {:.1f}'.format(imc))
if imc < 18.5:
    print('Voce está Abaixo do peso')
elif 18.5 <= imc < 25.0:
    print('Voce está no Peso ideal!')
elif 25 <= imc < 30:
    print('Voce está com Sobrepeso')
elif 30 <= imc <= 40:
    print('\nVoce está em Obesidade')
else:
    print('\nVoce está em Obesidade Morbida')