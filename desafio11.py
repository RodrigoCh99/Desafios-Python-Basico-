print('\nEsse programa calcula a área de uma parede e a tinta necessária para pinta-lá')
largura = float(input('informe a largura da sua parede: '))
altura = float(input('informe a altura da sua parede: '))
area = altura * largura
tinta = area/2
print('\nA área de uma parede com {} de largura e {} de altura é igual á: {} '.format(largura,altura,area))
print('para pintar essa parede vão ser necessarios {:.2f} litros de tinta\npois cada litro de tinta pinta 2 metros quadrados'.format(tinta))