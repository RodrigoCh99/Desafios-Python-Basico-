"""
    Crie um programa que leia duas notas de um aluno e calcule sua média,
     mostrando uma mensagem no final, de acordo com a média atingida:

    EX:
     > média a baixo de 5.0:
      REPROVADO.
     > média entre 5.0 e 6.9:
      RECUPERAÇÃO.
     > média 7.0 ou superior:
      APROVADO.
"""
print('\nESSE PROGRAMA DIZ SE O USUARIO FOI OU NÃO APROVADO DE ACORDEO COM SUA MÉDIA!')
n1 = float(input('\nInsira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
média = (n1 + n2) / 2
print('tirando {:.2f} e {:.2f}, a média do aluno é: {:.2f}'.format(n1, n2, média))

if média < 5.0:
    print('\nVoce foi \nREPROVADO!')
elif 5.0 <= média <= 6.9:
    print('\nVoce está de RECUPERAÇÃO!')
else:
    print('\nMeus parabens voce foi\nAPROVADO!')
