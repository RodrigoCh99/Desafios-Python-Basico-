"""
    A Confederação Nacional de Natação precisa de um programa que leia
     o ano de nascimento de um atleta e mostre sua categoria
     de acordo com a idade.

    EX:
     > Até 9 anos: MIRIM
     > Até 14 anos: INFANTIL
     > Até 19 anos: JUNIOR
     > Até 20 anos: SÊNIOR
     > Acima: MASTER
"""
print('ESSE PROGRAMA MOSTRA SUA CATEGORIA NA NATAÇÃO DE ACORDO COM A IDADE INFORMADA!')
data = int(input('\nQual o seu ano de nascimento? '))
idade = 2018 - data
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <=19:
    print('JUNIOR')
elif idade <=20:
    print('SÊNIOR')
else:
    print('\nParabéns voce é um\nMASTER!')
