cores = {'verde': '\033[32m',
         'vermelho': '\033[31m'}
n = int(input('Digite um número: '))
cont = 0
for c in range(1, n+1):
    if n % c == 0:
        print(f'{cores["verde"]}{c}', end=' ')
        cont += 1
    else:
        print(f'{cores["vermelho"]}{c}', end=' ')
print('\n')
print(f'O número {n} foi divisível {cont} vezes')
if cont == 2:
    print('Por isso ele É um número PRIMO')
else:
    print('Por isso ele NÃO É um número PRIMO')
