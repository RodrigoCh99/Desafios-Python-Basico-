print('\nESSE PROGRAMA AJUDA A RESOLVER EXERCICIOS DE P.A!')
a1 = int(input('\nInforma o valor do primeiro termo da P.A: '))
r = int(input('\nInfome a razão da P.A: '))
n = a1 + (10 - 1) * r
for c in range(a1, n + r, r):
    print('{}'.format(c), end=' > ')
print('Fim')