"""
    Elabore um programa que calcule o preço a ser pago por um produto
     considerando o seu preço normal e condição de pagamento

    EX:
     > A vista DINHEIRO: 10% de desconto
     > A vista no CARTÃO: 5% de desconto
     > Em até 2x no CARTÃO: preço normal
     > 3X ou mais no CARTÃO: 20% de juros
"""

print('\nESSE PROGRAMA CALCULA O VALOR A SER PAGO POR UM PRODUTO DE ACORDO COM A FORMA DE PAGAMENTO!')
produto = float(input('\nQuanto custa o produto que voce quer comprar? '))
print('-'*25)
print("""|[1] a vista no DINHEIRO |
|[2] a vista no CARTÃO   |
|[3] 2X no CARTÃO        |
|[4] 3X ou mais no CARTÃO|""")
print('-'*25)
pagamento = int(input('\nEscolha sua forma de pagamento de acordo com a tabela: '))
if pagamento == 1:
    print('O produto sairá a: {:.2f}'.format(produto - (produto/100)*10))
elif pagamento == 2:
    print('O produto sairá a: {:.2f}'.format(produto - (produto/100)*5))
elif pagamento == 3:
    print('O produto sairá a: {:.2f}'.format(produto))
elif pagamento == 4:
    print('O produto sairá a: {:.2f}'.format(produto + ((produto/100)*20)))
else:print('Opção invalida de pagamento')