"""
 Faça um programa que leia o nome completo de uma pessoa,
 mostrando em seguida o primeiro e o ultimo nome separadamente

 ex: Ana Maria de Souza
 primeiro = Ana
 segundo = Souza
"""

print('\nESSE PROGRAMA É REPONSAVEL POR DAR BOAS VINDAS!')
nome = str(input('Qual o seu nome? ')).strip()
print('Prazer em te conhecer {}'.format(nome))
print('Eu sei que seu nome é {}'.format(nome.split()[0]))
print('Eu sei que o seu último nome é: {}'.format(nome.split()[-1]))
