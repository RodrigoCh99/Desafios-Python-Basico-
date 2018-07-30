"""
 Crie um programa que leia o noem de uma cidade e diga se ela começa ou não com o nome "SANTO"
"""
print("\nESSE PROGRAMA INFORMA SE VOCE VIVE OU NÃO EM UMA CIDADE QUE COMEÇA O NOME COM A PALAVRA 'SANTO'!")

nome = str(input('\nEm que cidade você mora? '))
nome.strip()
print('\nA respota se essa cidade começa com santo no nome é: {} '.format('SANTO'in nome.upper().split()[0]))

