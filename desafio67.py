"""
    Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
     pelo usuário. O programa será interrompido quando o número solicitado for negativo.
"""
while True:
    n = int(input('Quer ver a tabuada de qual valor: '))
    if n < 0:
        break
    print('--' * 15)
    for c in range(1, 11):
        print(f'{n:2} * {c:2} = {n*c:2}')
    print('--'*15)
print('FECHANDO...')

""" # OUTRO MODO DE FAZER!
print('\nEsse programa informa a tabuada!(3.0)')
print('Digite um número negatico para fechar\n')
print('-='*20)
c = 0
num = True
num2 = 0
while True:
    if c < 11:
        num = int(input('Informe a tabuada que deseja ver: '))
        if num < 0:
            break
        while c < 11:
            print(f'{num} * {num2:2} = {num * num2:2}')
            num2 = num2 + 1
            c = c + 1
    elif c == 11:
        num2 = 0
        c = 0
        print('-=' * 20)

print('FECHANDO....')

"""
