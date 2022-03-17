n = int(input('Digite um número para \n'
                'calcular seu fatorial: '))
f = 1
c = n
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')