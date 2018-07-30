print('Esse programa calcula o peso de 5 pessoas e mostra a mais pesada!')
pesado = 0
leve = 0
for c in range(1,6):
    peso = float(input('Informe o peso da {}° pessoa: '.format(c)))
    if c == 1:
        pesado = peso
        leve = peso
    else:
        if peso > pesado:
            pesado = peso
        elif peso < leve:
            leve = peso
print('\nA pessoa mais pesada pesa: {} Kg'.format(pesado))
print('A pessoa mais leve pesa: {} Kg'.format(leve))