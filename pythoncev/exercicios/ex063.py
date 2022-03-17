print('-' * 15)
print('Sequência de Fibonacci')
print('-' * 15)
termos = int(input('Quantos termos você quer mostrar?'))
t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end=' -> ')
cont = 1
while cont <= termos:
    t3 = t1 + t2
    print(f'{t3}', end=' -> ')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')
