frase = str(input('\nInsira uma frase: ')).upper()#frase digitada pelo usuario
flimpa = ''.join(frase.split())#frase sem espaços inuteis
totals = len(flimpa) #total de caracteries da frase
cont = totals #contador para contar de tras para frente as letras
fnova = str('') #frase nova que será a invertida com 0 strings declaradas
for c in range(0, totals): #contador que vai do 0 até o total de stings da frase sem espaços inuteis
    cont = cont -1 #contador correndo ao inverso do laço para guardar os caracteries da string
    fnova = fnova + flimpa[cont] #a frase invertida recebdo os caracteries invertidos
print('Essa frase de tras para frente é: {}'.format(fnova)) #a frase invertida sendo printada para o usuario
if fnova == flimpa: #verificação se ambas as frases são iguais
    print('\nEssa frase é um palídromo!')
else:
    print('\nEssa frase não é um palídromo!')


"""
    modo do professor:


frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('temos um palídromo!')
else:
    print('A frase não é um palídromo')
"""














