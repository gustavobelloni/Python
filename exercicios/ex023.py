num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analizando o número {num}')
print(f'''Unidade: {u}
Dezena: {d}
Centena: {c}
Milhar: {m}''')


