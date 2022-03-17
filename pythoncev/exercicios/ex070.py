print('-' * 20)
print(' LOJA SUPER BARATÃO')
print('-' * 20)
totpreço = prod1000 = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$ '))
    cont += 1
    totpreço += preço
    if preço > 1000:
        prod1000 += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper()[0].strip()
    if continuar == 'N':
        break
print('-' * 20, 'FIM DO PROGRAMA', '-' * 20)
print(f'O total de compra foi R${totpreço:.2f}')
print(f'Temos {prod1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
