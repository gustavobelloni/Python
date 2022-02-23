print("""Gerador de PA
-=-=-=-=-=-=-=-=-=""")
n = int(input('Primeiro termo: '))
r = int(input('Razão da PA:'))
c = 1
while c <= 10:
    n += r
    print(f'{n}', end=' -> ')
    c += 1
print('FIM')
