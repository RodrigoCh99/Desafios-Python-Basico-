"""
    Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
     o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
    EX:
        A) Quantas pessoas têm mais de 18 anos.
        B) Quantos homens foram cadastrados.
        C) Quantas mulheres têm menos de 20 anos.
"""
 # SEM AJUDA DO PROFESSOR
idade = 0
sexo = str('')
c = 0
c2 = 0
continuar = str('')
mulheres = 0
while True:
    print('--'*20)
    idade = int(input('Qual a sua idade: '))
    if idade > 18:
        c += 1
    sexo = str(input('Qual o seu sexo[M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        c2 += 1
    elif sexo == 'F' and idade < 20:
        mulheres += 1
    continuar = str(input('Quer continuar[S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break

print('--' * 20)
print(f'\nForam cadastradas: {c} pessoas com mais de 18 anos.')
print(f'Foram cadastrados {c2} homens')
print(f'Foram cadastrados {mulheres} mulheres com menos de 20 anos.')









