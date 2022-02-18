cores = {'limpar': '\033[m',
         'verde': '\033[32m',
         'amarelo': '\033[33m'}
n = int(input('Me diga um número qualquer: '))
resultado = n % 2
if resultado == 0:
    print(f'O número {n:.0f} é {cores["verde"]}PAR{cores["limpar"]}')
else:
    print(f'O número {n:.0f} é {cores["amarelo"]}ÍMPAR{cores["limpar"]}')
