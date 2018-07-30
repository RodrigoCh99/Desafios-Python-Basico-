"""
    Melhore o desafio 61,perguntando para o usuario se ele quer mostrar mais alguns termos.
     O programa encerra quando ele disser que quer mostrar 0 termos.
"""
print('\nESSE PROGRAMA AJUDA A RESOLVER EXERCICIOS DE P.A! (3.0')
print('-='*10)
primeiro = int(input('Primeiro Termo: '))
razão = int(input('Razão da P.A: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} > '.format(termo),end='')
        termo += razão
        cont += 1
    print('PAUSA...')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('-=' * 10)
print('Progressão finalizada com {} termos'.format(total))
print('FIM DO PROGRAMA!')
