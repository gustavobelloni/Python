números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar: [S/N] ')).upper()[0].strip()
    if r in 'N':
        break
print('-=' * 30)
números.sort()
print(f'Você digitou os valores {números}')
