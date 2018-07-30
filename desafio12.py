print('\nESSE PROGRAMA CALCULA DESCONTOS!')
produto = float(input('\nInforme o preço do produto: R$:'))
descontado = (produto/100)*5
print('Esse produto com 5% de desconto é igual a: R$:{:.2f}'.format(produto-descontado))