smedia = 0 #soma da media para a primeira pergunta
velho = 0 #variavel com a maior idade masculina
nvelho = str('')
novas = 0
for pessoas in range(1,5):

    print('==== {}ª pessoa ===='.format(pessoas)) #cadastro

    nome = str(input('NOME: ')).strip()  #cadastro
    idade = int(input('IDADE: ')) #cadastro
    sexo = str(input('SEXO[M/F]: ')).strip() #cadastro

    smedia = smedia + idade #soma das idade para o calculo da media para a primeira pergunta:

    if sexo in 'Mm': #segunda pergunta
        if idade > velho:
            velho = idade
            nvelho = nome
    elif sexo in 'Ff': #terceira pergunta
        if idade < 20:
            novas += 1

print('\nA média de idade do grupo é: {} anos'.format(smedia/4)) #resposta da primeira pergunta

if velho == 0:
    print('nenhum homem foi informado!')
else:
    print('O homem mais velho é o {} pois sua idade é: {}'.format(nvelho,velho)) #resposta da segunda pergunta
print('Neste grupo existem {} mulhere(s) com menos de 20 anos!'.format(novas)) #resposta da terceira pergunta
