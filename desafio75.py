"""
    Análise de Dados em uma Tupla
     Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

    A) Quantas vezes apareceu o valor 9.
    B) Em que posição foi digitado o primeiro valor 3.
    C) Quais foram os números pares.

"""
num = (int(input('Digite um número: ')),
       int(input('Digite Outro número: ')),
       int(input('Digite Mais um número: ')),
       int(input('Digite O ultimo número: '))
)
print('--'*25)
print(f'Voce digitou os valores {num}')
print(f'O número 9 apareceu {num.count(9)} vezes')
if num.count(3) == 0:
    print('O número 3 não foi digitado portanto não aparece em nenhuma posição')
else:
    print('O numero 3 aparece pela primira vez na {}ª posição'.format(num.index(3)+1))
print(f'Os valores pares digitados foram ',end='')
for n in num:
    if n % 2 == 0:
        print(n , end=' ')


