""""
    kilo = float(input('Digite um peso em kilos: '))
    grama = kilo * 1000
    miligrama = grama * 1000
    print('O valor informado é igual a: {} kilos \nigual a: {} em gramas\nigual a:{} em miligramas'.format(kilo,grama,miligrama))
"""

metro = float(input('Digite um valor em metros: '))
cent = metro * 100
mili = metro * 1000
print('\nO valor informado: {:.2f}\nEm metros corresponde a: {:.2f} m\nEm centimetros corresponde a: {:.2f} cm\nEm milimetros corresponde a: {:.2f} mm'.format(metro,metro,cent,mili))