"""
    Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores
     'M'ou'F'. Caso esteja errado, peça a digitação novamente
      até ter um valor correto.
"""
sexo = str(input('Digite seu sexo[M/F]: ')).strip().upper()[0]

while sexo != 'M' and sexo != 'F':
    print('\nVOCE DIGITOU ERRADO! \npor favor responda+ novamente!')
    sexo = str(input('Digite seu sexo[M/F]: ')).strip().upper()[0]

if sexo == 'M':
    print('\nVoce é um homem pois seu sexo é ({})'.format(sexo))
elif sexo == 'F':
    print('\nVoce é uma mulher pois seu sexo é ({})'.format(sexo))

