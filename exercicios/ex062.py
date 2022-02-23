print('Gerador de PA')
print('-=' * 8)
n = int(input('Primeiro termo: '))
r = int(input('Razão da PA:'))
termo = n
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        n += r
        print(f'{n}', end=' -> ')
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados')
