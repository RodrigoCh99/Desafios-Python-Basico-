"""
  crie um programa que leia o nome completo de uma pessoa e mostre:

  > O nome com todas as letras maiusculas
  > O nome com todas as letras minusculas
  > Quantas letras ao tem ao todo (sem contar os espaços)
  > Quantas letras tem o primeiro nome
  >
"""
print('\nESSE PROGRAMA MOSTRA INFORMAÇÕES SOBRE O SEU NOME!')
nome = str(input('\nInforme o seu nome: '))

print('O seu nome com todas as letras em maiusculo fica: {}'.format(nome.upper()))
print('O seu nome com todas as letras em minusculo fica: {}'.format(nome.lower()))
print('O total de letras do seu nome é: {}'.format(len(nome)- nome.count(' ')))
print('O total de letras do seu primeiro nome é: {}'.format(len(nome.split()[0])))

