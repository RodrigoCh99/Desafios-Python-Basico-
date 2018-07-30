"""
    Lista de Preços com Tupla:
     Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
     na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""

print('--'*10,end='')
print(' Lista de Preços ',end='')
print('--'*10)
lista = ('Lapis', 1.75,
         'Borracha', 2.00,
         'Caderno', 15.90,
         'Estojo', 25.00,
         'Transferidor', 4.20,
         'Compasso', 9.90,
         'Mochila', 120.32,
         'Canetas', 22.30,
         'Livro', 34.90)
for l in range(len(lista)):
    if l % 2 == 0:
        print(f'{lista[l]:.<30}',end='')
    else:
        print(f'{lista[l]:.>30.2f}')
print('--'*30)
