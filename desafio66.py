"""
      Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando
      o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números
      foram digitados e qual foi a soma entre eles (desconsiderando o flag).
"""
print(f'DIGITE[999] PARA PARAR! ')
num = 0
soma = 0
c = 0
print('--'*20,)
while True:
    num = int(input('Digite um valor(999 para parar): '))
    if num == 999:
        break
    soma += num
    c += 1
print('--'*20,)
print(f'Foram digitados {c} números!')
print(f'A soma dos valores foi {soma}!')






