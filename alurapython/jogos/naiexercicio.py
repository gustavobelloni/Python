inicio = 1

for contador in range(2, 2022):
    print(f'{inicio} + {contador}', end=' = ')
    inicio += contador
    contador += 1
    print(f'{inicio}')

# print(f'1 + 2 + 3 + ... + 2021 = {inicio}')
