"""
 Faça um programa que leia uma frase pelo teclado e mostre:

 > Quantas vezes aparece a letra 'A'
 > Em que posição ela aparece a primeira vez
 > Em que posição ela aparece pela ultima vez

"""
print('-'*50)
print('ESSE PROGRAMA MOSTRA INFORMAÇÕES SOBRE A LETRA A!')
print('-'*50)

nome = str(input('\nDigite uma frase: ')).strip().upper()
print('-'*50)

print('|A letra A aparece {} vezes ao longo da frase.'.format(nome.count('A')))
print('|A letra A aparece pela primeira vez na posição: {}'.format(nome.find('A')+1))
print('|A letra A aparece pela ultima vez na posição: {}'.format(nome.rfind('A')+1))
print('-'*50)