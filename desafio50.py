s = 0
for c in range(0, 6):
    num = int(input('insira um número: '))
    if num % 2 == 0:
        s += num
print('\nA soma dos números pares informados é: {}'.format(s))

