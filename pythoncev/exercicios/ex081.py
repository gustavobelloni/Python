valor = []
elem = 0
while True:
    num = int(input('Digite um valor: '))
    valor.append(num)
    elem += 1
    continuar = str(input('Quer continuar: [S/N] ')).upper()[0].strip()
    if continuar == 'N':
        break
print('-=' * 20)
print(f'Você digitou {elem} elementos.')
valor.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valor}')
if 5 in valor:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
