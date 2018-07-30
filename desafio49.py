num = int(input('\nInsira um número para saber sua tabuada: '))
for c in range(0, 11):
    print('{} X {:2} = {} '.format(num, c, num * c))