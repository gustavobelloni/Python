lista = list()
par = list()
ímpar = list()
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        ímpar.append(num)
    continuar = str(input('Quer continuar: [S/N] ')).upper()[0].strip()
    if continuar == 'N':
        break
print('-=' * 20)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {ímpar}')

