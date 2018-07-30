"""
    Faça um programa que leia o ano de nascimento de um jovem
     e informe de acordo com a idade:

    EX:
     > Se ele ainda vai se alistar
     > Se está na hora de se alistar
     > Se já passou o tempo do alistamento

    Seu programa tambem deverá mostrar:
     o tempo que falta ou que passou do prazo
"""
print('\nESSE PROGRAMA CALCULA O TEMPO PARA O ALISTAMENTO!')
ano = int(input('Em que ano voce nasceu: '))
ano2 = 2018 - ano

if ano2 < 18:
    print('\nVoce ainda não precisa se alistar!\nSó daqui {} ano(s).'.format(18-ano2))
elif ano2 > 18:
    print('\nVce já deveria ter se alistado \nVoce está {} ano(s) atrasado'.format(ano2-18))
else:
    print('\nEstá na hora! \nAliste-se o mais rapido possivel')
