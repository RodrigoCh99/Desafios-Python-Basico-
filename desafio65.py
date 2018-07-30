"""
    Crie um programa que leia vários números inteiros pelo teclado
     no final da execução, mostre a média entre todos os valores e qual
     foi o maior e o menor valores lidos. O programa deve perguntar ao
     usuario se ele quer ou não continuar a digitar valores.
"""
c = 0
num = 0
soma = 0
maior = 0
menor = 0
resposta = str('S')


while resposta != 'N':
    num = int(input('Informe um valor numerico: '))
    soma = soma + num
    if c == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    c += 1
    resposta = str(input('Quer continuar[s/n]? ')).upper()

print('\nvocê digitou {} números e a média entre eles é: {}'.format(c, (soma / c)))
print('O maior número digitado foi: {}'.format(maior))
print('O menor número digitado foi: {}'.format(menor))




