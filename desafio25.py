"""
 Crie um programa que leia o nome de uma pessoa e diga se ela tem "silva" no nome
"""
print('\nESSE PROGRAMA INFORMA SE VOCÊ TEM OU NÃO SILVA NO NOME!')

nome = str(input('\nQual o seu nome: ')).upper().strip()
print('\nA resposta se o seu nome tem ou não silva é: {}'.format('SILVA'in nome))
