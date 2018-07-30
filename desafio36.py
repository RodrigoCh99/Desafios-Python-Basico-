"""
        Escreva um programa para aprovar o emprestimo bancario para a compra de um casa.
         O programa vai perguntar o valor da casa, osalario do comprador e em quantos anos
         ele vai pagar.
        Calcule o valor da prestação mensa, sabendo que ela não pode sxceder 30% do salário
         ou então o emprestimo será negado.
"""
print('\nEsse programa aprova ou não o emprestimo bancario para a compra de uma casa!')

vcasa = float(input('\nInforme o valor da casa R$: '))
vsala = float(input('Informe o seu salário R$: '))
anos = float(input('Informe em quantos anos vai pagar R$: '))
prest = float(vcasa/(anos*12))

if prest > (vsala / 100) * 30:
    print('\nO valor da sua prestação será de R$:{:.2f} como esse valor ultrapassa 30% do seu salario R$:{:.2f}'.format(prest,(vsala/100)*30))
    print('Seu imprestimo foi negado!')
elif prest < (vsala / 100) * 30:
    print('\nO seu imprestimo foi aceito, parabens!')
    print('O valor da sua prestação será de R$:{:.2f}'.format(prest))
else:
    print('\nO seu imprestimo foi aceito, parabens!')
    print('\nO valor da sua prestação será de R$:{:.2f}'.format(prest))
    print('\nTome cuidado se seu salario diminuir ficará dificil de pagar as prestações!')





# print('sua prestação será {:.2f}'.format(prest))


