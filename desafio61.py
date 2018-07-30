"""
    Refaça o desafio 51, lendo o primeiro termo de uma P.A, mostrando
     os 10 primeiros termos da progressão usando a estrutura while.
"""

'''
print('\nESSE PROGRAMA AJUDA A RESOLVER EXERCICIOS DE P.A! (2.0)')

a1 = int(input('\nInforma o valor do primeiro termo da P.A: '))
r = int(input('\nInfome a razão da P.A: '))
c = 0
while c < 10:
    print('{}'.format(a1),end=' > ')
    a1 = a1 + r
    c = c + 1
print('FIM')
'''
#outra solução possivel(com a orientação do professor):

print('Gerador de P.A')
print('-='*10)
primeiro = int(input('Primeiro Termo: '))
razão = int(input('Razão da P.A: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} > '.format(termo),end='')
    termo += razão
    cont += 1
print('FIM')