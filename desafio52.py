num = int(input('Insira um número inteiro: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        total += 1
if total == 2:
    print('\nEsse número é primo!')
else:
    print('\nEsse número não é primo!')

