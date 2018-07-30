"""
    Refaça o desafio 35 dos triangulos, acrecentando o recurso de mostrar
     que tipo de triãngulo será formado:

    > Equilatero: todos os lados iguais.
    > Isosceles: dois lados iguais.
    >Escaleno: Todos os lados diferentes.

"""
print('\nEsse programa responde se as retas informadas podem ou não formar um triangulo!')
print('E caso seja possivel, informa o tipo de tringulo!')
r1 = float(input('\nInforme o comprimento da primeira reta: '))
r2 = float(input('Informe o comprimento da segunda reta: '))
r3 = float(input('Informe o comprimento da terceira reta: '))

if (r2 - r3) < r1 < (r2 + r3) and (r1-r3) < r2 < (r1 + r3) and (r1 - r2) < r3 < (r1 + r2):
    print('\nEssas retas formam um triangulo!')
    if r1 == r2 == r3:
        print('Este tringulo inclusive é EQUILÁTERO!')
    elif r1 != r2 != r3 and r1 != r3:
        print('Esse tringulo inclusive é ESCALENO!')
    else:
        print('Esse tringulo inclusive é ISÓCELES!')
else:
    print('\nEssas retas não formam um triangulo!')


